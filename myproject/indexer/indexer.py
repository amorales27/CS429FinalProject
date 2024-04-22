import math
import pickle
import string
import numpy as np
from numpy.linalg import norm
from sklearn.metrics.pairwise import cosine_similarity
from os import listdir

arr = listdir('myproject\webcrawler\webcrawler\downloads')

#Going through downloaded documents and filtering out most non-relevant text like html code
i = 0
sub1 = ">"
sub2 = "<"
docs = []
#print(len(arr))
for fileName in arr:
    i += 1
    j = 0
    #print(fileName)
    f = open('myproject\webcrawler\webcrawler\downloads\\' + fileName, 'r', errors="ignore")
    lines = f.readlines()
    count = 0
    sentences = []
    for line in lines:
        filteredChars = []
        bracketStart = False
        bracketEnd = False
        for char in line:
            if char == '<':
                bracketStart = True
                bracketEnd = False
            if char == '>':
                bracketEnd = True
                bracketStart = False
            if(bracketEnd == True and bracketStart == False):
                if (char != '>') and (char != '\n'):
                    filteredChars.append(char)
        if(len(''.join(filteredChars))!=0 ): 
            sentences.append(''.join(filteredChars))
    
    docs.insert(i,sentences)

docTitles = []
for i in range(len(arr)):
    docTitles.append([arr[i], i])

#for i in range(len(docs)):
    #print(f"Length of {i+1} doc: {len(docs[i])}")


def createIndex(documents):
    docIndex = {}
    for doc in documents:
        for word in doc:
            if word[0] in docIndex:
                #print(f"This is the current document: {doc}")
                docIndex[word[0]].append([documents.index(doc), word[1], word[2]])
                #if(word[0] == 'nation'):
                    #print('---------------')
                    #print(docIndex[word[0]])
            else:
                #if(word[0] == 'nation'):
                    #print([documents.index(doc), word])
                docIndex[word[0]] = [[documents.index(doc), word[1], word[2]]]
    return docIndex

def tokenizeTFIDF(document, docID):
    document = document.translate(str.maketrans('','', string.punctuation)) # remove punctuation
    document = document.split() # split up the document
    documentListCopy = document.copy()
    for term in documentListCopy:
        #print(f"This is the current term: {term} in document {document} and its length {len(term)}")
        if (term.isalnum() == False) or (len(term) > 25):
            document.remove(term)
    #print(f"FINAL DOCUMENT: {document}")
    for i in range(len(document)): #lowercase the strings
        document[i] = document[i].lower()
    typesList = sorted(set(document), key=lambda x:document.index(x)) 
    uniqueList = []
    for word in typesList:
        uniqueList.append(''.join(c for c in word if c.isalnum()))
    
    for i in range(len(uniqueList)):
        temp = uniqueList[i]
        uniqueList[i] = [temp, round((float(document.count(temp)) / float(len(document))), 3), docID]
    return uniqueList
i = 0
tokDocs = []
docID = 0
for doc in docs:
    for s in doc:
        if docID < 250:
            tokDocs.append(tokenizeTFIDF(s, docID))
            i+=1
    docID += 1
#print(tokDocs)

invIndex = createIndex(tokDocs)
#print(invIndex)

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


def getQueryVector(query):
    idfValues = {}
    for term in query:
        idfValues[term] = (math.log10(1+(len(tokDocs)/ len(invIndex[term]))))
    
    #print(idfValues)
    return idfValues

def search(query):
    query = tokenizeQuery(query)
    queryFrequency = []
    for term in query:
        if term in invIndex:
            #print(invIndex[term])
            queryFrequency.append(len(invIndex[term]))
        else:
            queryFrequency.append(0)
    #print(queryVector)
    frequencies = []
    for key in invIndex:
        frequencies.append(len(invIndex[key]))
    
    #print(frequencies)
    maxFrequency = max(frequencies)
    #print(maxFrequency)
    normVector = []
    for i in range(len(queryFrequency)):
        normVector.append(queryFrequency[i]/maxFrequency)
    getQueryVector(query)
    #print(queryFrequency)

    cosineSim = np.dot(normVector, queryFrequency)/(norm(normVector)*norm(queryFrequency))
    #print(f"Cosine similary {cosineSim}")


#print(invIndex['mormon'])

with open('invIndex.pickle', 'wb') as file:
        pickle.dump(invIndex, file)

with open('tokDocs.pickle', 'wb') as file:
        pickle.dump(tokDocs, file)

with open('docTitles.pickle', 'wb') as file:
        pickle.dump(docTitles, file)