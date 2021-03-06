from BTrees.OOBTree import OOBTree

from src.CategoriesAnalizer.Classifier import Classifier
from src.CategoriesAnalizer.FeatureAnalizer import FeatureAnalizer
from src.WebReader.WebReader import WebReader


class FeatureAnalisys(object):
    def __init__(self, feature_name, feature_values, database):
        self.feature_name = feature_name
        self.feature_values = feature_values
        self.database = database

    def prepare_model(self, configuration_map):
        article_db = self.__create_articles_db(self.database.dbroot, configuration_map)
        feature_analizer = FeatureAnalizer(
            self.database,
            feature=self.feature_name, values=self.feature_values,
            configuration_map = configuration_map)
        feature_data = feature_analizer.update_words_database()
        most_frequent_words = feature_analizer.update_most_frequent_words_in_db(feature_data)
        classifier = Classifier(self.feature_name, configuration_map)
        return classifier.classify(article_db, most_frequent_words)

    def __read_articles_from_web(self, configuration_map):
        article_db = self.__create_articles_db(self.database.dbroot, configuration_map)
        reader = WebReader(article_db, configuration_map)
        links = configuration_map['webpages_list']

        for link in links:
            print("Extracting information from link: ", link)
            reader.extract_all_articles(link)


    def __create_articles_db(self, database_root, configuration_map):
        articles_db_name = configuration_map['articles_database_name']
        if not database_root.has_key(articles_db_name):
            database_root[articles_db_name] = OOBTree()
        return database_root[articles_db_name]


