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
  
## Design
### System capabilities, interactions, integration.

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
