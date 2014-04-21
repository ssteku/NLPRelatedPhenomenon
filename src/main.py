from WebReader.WebReader import WebReader
from CategoriesAnalizer.SentimentAnalizer import SentimentAnalizer
import urllib2
from BTrees.OOBTree import OOBTree
import re
from storage.DatabaseFacade import DatabaseFacade
from RawTextFeatureExtraction.FeatureExtractor import FeatureExtractor
def read_articles_from_web(database):
    reader = WebReader(database)
    links = [
        "http://cnn.com"
    ]

    for link in links:
        print "Extracting information from link: ", link
        reader.extract_all_articles(link)

def read_features_from_articles(article_db, feature_db):
    extractor = FeatureExtractor(feature_db)
    for key in article_db.keys():
        extractor.get_most_frequent_words_features(article_db[key])
def get_databse_structure():
    database_structure = dict()
    database_structure['bigrams'] = []
    database_structure['levels'] = ['1', '2', '3']
    return database_structure
def create_articles_db(database_root):
    if not database_root.has_key('articles_db'):
        database_root['articles_db'] = OOBTree()
    return database_root['articles_db']

database = DatabaseFacade("./Database.fs")
article_db = create_articles_db(database.dbroot)
sentiment_db = database.dbroot['sentiment_words']
database_structure = get_databse_structure()
read_features_from_articles(article_db, sentiment_db)
# read_articles_from_web(article_db)
sentiment_analizer = SentimentAnalizer(database, database_structure)
sentiment_analizer.update_words_database()
sentiment_analizer.update_most_frequent_words_in_db()
print  "Database contains %s articles parsed" % len(database.dbroot.keys())



#connect to a URL
