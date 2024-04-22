# CS429 Final Project

## Abstract
### Development summary, objectives, and next steps.
  This project was split up into four parts; The crawler, indexer, processor and report. Since some of these sections invovled the use of python libraries I was not familiar with, I started development by doing research on Scrapy by watching [videos][1] and reading the [documentation] [2]. I practiced some web scraping by scraping websites like
  <quotes.toscrape.com> and <books.toscrape.com>. Then started development on the web crawler. Once the web crawler was finished I moved onto development of the indexer. I referenced previous homeworks aas most of the work I have done before I just had to adapt some of the methods in order to parse the html format documents. Finally for the last 
  part of the coding section I had to research on Flask since I had never used it before. I looked at some [examples for gathering user input][3], [videos about forms][4], and [updating web pages][5]. With this I was able to make a simple but functional Flask application for my intent and purposes.  

  My objective with this project was to develop a flask app that you can enter a query into and specify the top-k results you want and get the documents most relevant to your query from most to least. That will be the user's experience but in the backend I wanted to develop a web scraping capable of gathering a sufficient variety of documents and to index them 
  using tf-idf scores.   

  The next steps would be improve on the efficiency of the system. Creating an inverted index takes a long time with the methods I used and there are more advanced methods able to speed up the process. Also to improve the user experience. The app is very primitive and not very intuitive on the capabilities of it. It has an acceptable level
  of functional in order to show that the system is operable but not a very efficient search engine. It is also limited by the amount of documents I was also to collect so it is possible some queries will have very few to no results. 
  
## Overview
### Solution outline, relevant literature, proposed system
  ![SolutionOutline](https://github.com/amorales27/CS429FinalProject/assets/77760301/82f2ddf0-ab6b-458f-870a-20c64a962776)

  The proposed system will be written in python. It will make use of numerous libraries. The web crawler will use Scrapy in order to be able to extract links and download the web content as HTML format. These files will then be stored in a directory for the indexer to be able to access. The indexer will use
  Sci-kit learn in order to calculate the cosine similarity and also use pickle in order to save the inverted index so it does not need to be recompiled. Finally the processor will use Flask to host a web application. This will allow the user to input the query and the amount of results they want back
  from the browser and get the results in the browser. The results will be a list document titles ranked from most to least relevant. 
  

## Design
### System capabilities, interactions, integration.
   The crawler is capable of crawling through links that lead to other wikipedia pages. I have limited to only wikipedia pages so the crawler doesn't follow references outside of wikipedia. Wikipedia pages are also mostly made up of text so a lot terms get extracted from wiki pages. The crawler only crawls to a
   depth of 10 links with a limit of 2500 so the crawler does not exceed 2500 web pages crawled. The interaction between the crawler and indexer is through the directory where the downloaded web pages are stored. The indexer goes through all the downloaded pages and parses them. The parsing is quite limited as it is
   difficult to filter out meaningful text relevant to the topic and class name and other html identifiers. So the indexer is capable of filtering out some HTML code and keeping text. It also tokenizes the documents by removing non-alphanumeric characters, removing puncuation, repeated characters and calculates
   the TF-IDF score for each term and saves that in the index. The inverted index is then stored in a pickle format so that the processor can use it rank documents. The indexer also stores the tokenized documents and the document titles in a pickle format. The processer uses Flask to host a local web application 
   that allows the user to input their query. The processor is only capable of handling single-word queries and digits for the number of k results. It does not handle numbers spelled in text. 
   
## Architecture
### Software components, interfaces, implementation.

## Operation
### Software commands, inputs, installation.

## Conclusion
### Success/Failure results, outputs, caveats/cautions.

## Data Sources
### Links, downloads, access information

## Test Cases
### Framework, harness, coverage.

## Source Code
###  Listings, documentation, dependencies (open-source).

## Bibliography
###  Reference citations (Chicago style- AMS/AIP or ACM/IEEE).
1. “Coding Web Crawler in Python with Scrapy.” YouTube, November 23, 2022. https://youtu.be/m_3gjHGxIJc?si=VdBeKBK5FtfxNRjy.
2. “Scrapy Tutorial¶.” Scrapy Tutorial - Scrapy 2.11.1 documentation, April 11, 2024. https://docs.scrapy.org/en/latest/intro/tutorial.html.
3. Lin, Liu Zuo. “Python Flask - Taking User Input Using Forms.” Medium, February 19, 2023. https://python.plainenglish.io/python-flask-taking-user-input-using-forms-5032bd2a5333. 
4. Schafer, Corey. “Python Flask Tutorial: Full-Featured Web App Part 3 - Forms and User Input.” YouTube, May 4, 2018. https://youtu.be/UIJKdCIEXUQ?si=kyCZSQpq1WKpVdfm. 
5. “Refresh Jinja HTML without Reloading the Page: Flask Tutorial.” YouTube, November 22, 2022. https://youtu.be/ATEGpAb8GWI?si=x-DqvzL7atgHGwj9. 

[1]: https://youtu.be/m_3gjHGxIJc?si=VdBeKBK5FtfxNRjy.
[2]: https://docs.scrapy.org/en/latest/intro/tutorial.html.
[3]: https://python.plainenglish.io/python-flask-taking-user-input-using-forms-5032bd2a5333
[4]: https://youtu.be/UIJKdCIEXUQ?si=kyCZSQpq1WKpVdfm
[5]: https://youtu.be/ATEGpAb8GWI?si=x-DqvzL7atgHGwj9
