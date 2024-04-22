import pickle
from flask import Flask, redirect, render_template, request, url_for
import nltk, math, string
import numpy as np
from numpy.linalg import norm

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    query = request.form.get('query')
    k = request.form.get('k')

    print(query, k)
    return render_template('index.html', x=processQuery(query, k))

with open('invIndex.pickle', 'rb') as file:
    invIndex = pickle.load(file)

with open('tokDocs.pickle', 'rb') as file:
    tokDocs = pickle.load(file)

with open('docTitles.pickle', 'rb') as file:
    docTitles = pickle.load(file)

def createKGramIndex(k, docs):
    kGramIndex = {}
    #print(len(docs))
    for termList in docs:
        for term in termList:
            term[0] = "$"+term[0]+"$"
            for i in range(len(term[0])-1):
                if term[0][i:k+i] in kGramIndex:
                    kGramIndex[term[0][i:k+i]].append(term[0])
                else:
                    kGramIndex[term[0][i:k+i]] = [term[0]]
    return kGramIndex

kGramIndex = createKGramIndex(2, tokDocs)

def tokenizeQuery(document): 
    document = document.translate(str.maketrans('','', string.punctuation)) # remove punctuation
    splitDoc = document.split() # split up the document
    for i in range(len(splitDoc)): #lowercase the strings
        splitDoc[i] = splitDoc[i].lower()
    typesList = list(set(splitDoc)) #remove repeated words from list 
    uniqueList = []
    for word in typesList:
        uniqueList.append(''.join(c for c in word if c.isalnum()))
    return uniqueList

def processQuery(query, k):
    query = tokenizeQuery(query)[0]
    print(query)
    #print(f"THIS IS THE VALUE OF K: {k} and its type {type(k)} ========================================================================================================")
    if len(k) <= 0 :
        execute()
        return "Please enter a value for K greater than 0"
    k = int(k)
    query = "$"+query+"$"
    kGrams = []
    for i in range(len(query)-1):
        kGrams.append(query[i:2+i])

    #print(kGrams)
    terms = []
    for kGram in kGrams:
        if(kGram in kGramIndex):
            terms.append(kGramIndex[kGram])
    #print(kGramIndex['re'])
    uniqueTerms = []
    for termList in terms:
        #print(f"Term List: {termList}")
        for word in termList:
            word = word[1:-1]
            if(word not in uniqueTerms):
                uniqueTerms.append(word)
    
    #print(f"Unique Terms: {uniqueTerms}")
    query = query[1:-1]
    searchTerm = ''
    spellingCorrections = []
    for term in uniqueTerms:
        ed = nltk.edit_distance(query, term)
        if(ed == 0):
            searchTerm = term
        elif(ed < 3):
            spellingCorrections.append(term)
    result = ''
    if(searchTerm != ''):
        docIDs = []
        if(searchTerm in invIndex):
                docIDs = (invIndex[searchTerm])
        
        docIDs.sort(key=lambda docIDs: docIDs[1], reverse=True)
        uniqueIDs = []
        for doc in docIDs:
            if(doc[2] not in uniqueIDs):
                uniqueIDs.append(doc[2])
        #print(uniqueIDs)
        tfidfScores = [0] * len(uniqueIDs)
        for doc in docIDs:
            tfidfScores[uniqueIDs.index(doc[2])] = tfidfScores[uniqueIDs.index(doc[2])] + doc[1]
        
        rankedDocScores = []
        for i in range(len(uniqueIDs)):
            rankedDocScores.append([uniqueIDs[i], tfidfScores[i]])
        
        rankedDocScores.sort(key=lambda rankedDocs: rankedDocs[1], reverse=True)
        #print(rankedDocScores)

        rankedDocTitles =  []
        for i in range(len(rankedDocScores)):
            rankedDocTitles.append(docTitles[rankedDocScores[i][0]][0])

        #print(rankedDocTitles[:10])
        result = f"Your query term was found in these document/(s) {rankedDocTitles[:k]}"
    else:
        result = f"Your query: ''{query}'' was not found in the index, did you mean any of these terms? {spellingCorrections}"
    execute()
    return result

def execute():
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run()