from WebReader.WebReader import WebReader
from CategoriesAnalizer.FeatureAnalizer import FeatureAnalizer
import urllib2
from BTrees.OOBTree import OOBTree
import re
from storage.DatabaseFacade import DatabaseFacade
from RawTextFeatureExtraction.FeatureExtractor import FeatureExtractor
from CategoriesAnalizer.NaiveBayesClasifier import NaiveBayesClasifier
import math

class FeatureAnalisys(object):
    def __init__(self, feature_name, feature_values):
        self.feature_name = feature_name
        self.feature_values = feature_values
        self.database = DatabaseFacade("./Database.fs")
        self.article_db = self.__create_articles_db(self.database.dbroot)
        self.database_structure = self.__get_databse_structure()

    def prepare_model(self):
        # self.__read_articles_from_web(self.article_db)
        feature_analizer = FeatureAnalizer(self.database, self.database_structure, feature=self.feature_name, values=self.feature_values)
        feature_analizer.update_words_database()
        feature_analizer.update_most_frequent_words_in_db()
        feature_db_name = self.feature_name + '_words'
        feature_db = self.database.dbroot[feature_db_name]
        self.__read_features_from_articles(self.article_db, feature_db)
        print  "Database contains %s articles parsed" % len(self.database.dbroot.keys())

    def __read_articles_from_web(self, database):
        reader = WebReader(database)
        links = [
            "http://cnn.com/"
        ]

        for link in links:
            print "Extracting information from link: ", link
            reader.extract_all_articles(link)

    def __read_features_from_articles(self, article_db, feature_db):
        extractor = FeatureExtractor(feature_db)
        calsifier = NaiveBayesClasifier()
        training_set = []
        for key in article_db.keys():
            if hasattr(article_db[key], self.feature_name):
                training_set.append(extractor.get_most_frequent_words_features(article_db[key], self.feature_name)['2'])
        if len(training_set) > 10:
            train_size = int(math.floor(len(training_set)*0.5))
            print "Data set size: " + str(len(training_set))
            print "Train size: " + str(train_size)
            print "Test size: " + str(len(training_set)-train_size)
            calsifier.trainClasifier(training_set[:train_size])
            calsifier.testClasifier(training_set[train_size:])
        else:
            print "To few elements in training set"

    def __get_databse_structure(self):
        database_structure = dict()
        database_structure['bigrams'] = []
        database_structure['levels'] = ['1', '2', '3']
        return database_structure
    def __create_articles_db(self, database_root):
        if not database_root.has_key('articles_db'):
            database_root['articles_db'] = OOBTree()
        return database_root['articles_db']


