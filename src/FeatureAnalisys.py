from WebReader.WebReader import WebReader
from CategoriesAnalizer.FeatureAnalizer import FeatureAnalizer
import urllib2
from BTrees.OOBTree import OOBTree
import re
from storage.DatabaseFacade import DatabaseFacade
from CategoriesAnalizer.Classifier import Classifier

class FeatureAnalisys(object):
    def __init__(self, feature_name, feature_values, configuration):
        self.feature_name = feature_name
        self.feature_values = feature_values
        self.database = DatabaseFacade(configuration['database_path'])
        self.article_db = self.__create_articles_db(self.database.dbroot, configuration)

    def prepare_model(self, configuration_map):
        print  "Database contains %s articles parsed" % len(self.database.dbroot.keys())
        feature_analizer = FeatureAnalizer(
            self.database,
            feature=self.feature_name, values=self.feature_values,
            configuration_map = configuration_map)
        feature_data = feature_analizer.update_words_database()
        most_frequent_words = feature_analizer.update_most_frequent_words_in_db(feature_data)
        classifier = Classifier(self.feature_name, configuration_map)
        return classifier.classify(self.article_db, most_frequent_words)

    def __read_articles_from_web(self, configuration_map):
        reader = WebReader(self.article_db, configuration_map)
        links = configuration_map['webpages_list']

        for link in links:
            print "Extracting information from link: ", link
            reader.extract_all_articles(link)


    def __create_articles_db(self, database_root, configuration_map):
        articles_db_name = configuration_map['articles_database_name']
        if not database_root.has_key(articles_db_name):
            database_root[articles_db_name] = OOBTree()
        return database_root[articles_db_name]


