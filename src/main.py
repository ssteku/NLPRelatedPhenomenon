from WebReader.WebReader import WebReader
from CategoriesAnalizer.SentimentAnalizer import SentimentAnalizer
import urllib2
import re
from storage.DatabaseFacade import DatabaseFacade
database = DatabaseFacade("./Database.fs")
reader = WebReader(database)
sentiment_analizer = SentimentAnalizer(database)
sentiment_analizer.updateWordsDatabase()
sentiment_analizer.updateMostFrequentWordsInDb()
# links = [
#     "http://cnn.com"
# ]

# for link in links:
#     print "Extracting information from link: ", link
#     reader.extractAllArticles(link)
   
print  "Database contains %s articles parsed" % len(database.dbroot.keys())
        


#connect to a URL
