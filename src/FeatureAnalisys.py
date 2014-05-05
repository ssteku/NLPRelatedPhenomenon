from WebReader.WebReader import WebReader
from CategoriesAnalizer.FeatureAnalizer import FeatureAnalizer
import urllib2
from BTrees.OOBTree import OOBTree
import re
from storage.DatabaseFacade import DatabaseFacade
from RawTextFeatureExtraction.FeatureExtractor import FeatureExtractor
from CategoriesAnalizer.NaiveBayesClassifier import NaiveBayesClassifier
from CategoriesAnalizer.DecisionTreeClassifier import DecisionTreeClassifier
from CategoriesAnalizer.MaxentClassifier import MaxentClassifier
from CategoriesAnalizer.MLPClassifier import MLPClassifier
import math

class FeatureAnalisys(object):
    def __init__(self, feature_name, feature_values, configuration):
        self.feature_name = feature_name
        self.feature_values = feature_values
        self.database = DatabaseFacade("./Database.fs")
        self.article_db = self.__create_articles_db(self.database.dbroot)
        self.database_structure = self.__get_databse_structure()
        self.__configuration_map = configuration.get_configuration_map()

    def prepare_model(self):
        # self.__read_articles_from_web(self.article_db)
        feature_analizer = FeatureAnalizer(
            self.database, self.database_structure,
            feature=self.feature_name, values=self.feature_values,
            configuration_map = self.__configuration_map)
        feature_analizer.update_words_database()
        feature_analizer.update_most_frequent_words_in_db()
        feature_db_name = self.feature_name + '_words'
        feature_db = self.database.dbroot[feature_db_name]
        self.__read_features_from_articles(self.article_db, feature_db)
        print  "Database contains %s articles parsed" % len(self.database.dbroot.keys())

    def __read_articles_from_web(self, database):
        reader = WebReader(database, self.__configuration_map)
        links = [
            "http://news.yahoo.com/",
            "http://bbc.com/",
            "http://cnn.com"
        ]

        for link in links:
            print "Extracting information from link: ", link
            reader.extract_all_articles(link)

    def __read_features_from_articles(self, article_db, feature_db):
        for level in self.database_structure['levels']:
            print "------ Classification for level : " + level + " ------"
            training_set = self.__get_training_set(article_db, feature_db, level)
            self.__perform_clasification(training_set)


    def __get_training_set(self, article_db, feature_db, level):
        training_set = []
        extractor = FeatureExtractor(feature_db)
        for key in article_db.keys():
            if hasattr(article_db[key], self.feature_name):
                most_frequent_words = extractor.get_most_frequent_words_features(article_db[key], self.feature_name)[level]
                training_set.append(most_frequent_words)
        return training_set

    def __perform_clasification(self, training_set):
        if self.__is_training_set_proper(training_set):
            self.__classify_with_all_classifiers(training_set)
        else:
            print "Too less elements in training set"

    def __classify_with_all_classifiers(self, training_set):
        classifiers = [MLPClassifier(), NaiveBayesClassifier(), DecisionTreeClassifier()]
        minimal_training_set_size = self.__configuration_map['training_to_test_set_size_ratio']
        train_size = int(math.floor(len(training_set) * minimal_training_set_size))
        print "Data set size: " + str(len(training_set))
        print "Train size: " + str(train_size)
        print "Test size: " + str(len(training_set)-train_size)
        for classifier in classifiers:
            print "------ ------ Classifier: " + classifier.__class__.__name__ + '------'
            classifier.trainClasifier(training_set[:train_size])
            classifier.testClasifier(training_set[train_size:])

    def __is_training_set_proper(self, training_set):
        return len(training_set) > self.__configuration_map['minimal_training_set_size']

    def __get_databse_structure(self):
        database_structure = dict()
        database_structure['bigrams'] = []
        database_structure['levels'] = ['1', '2', '3']
        return database_structure
    def __create_articles_db(self, database_root):
        if not database_root.has_key('articles_db'):
            database_root['articles_db'] = OOBTree()
        return database_root['articles_db']


