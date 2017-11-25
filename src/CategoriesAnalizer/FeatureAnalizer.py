from src.CategoriesAnalizer.FeatureWordsDatabaseUpdater import FeatureWordsDatabaseUpdater
from src.CategoriesAnalizer.MostFrequentWordsExtractor import MostFrequentWordsExtractor
class FeatureAnalizer(object):
    def __init__(self, database, feature, values, configuration_map):
        self.database_root = database.dbroot
        self.feature = feature
        self.values = values
        self.__configuration_map = configuration_map
    def update_words_database(self):
        updater = FeatureWordsDatabaseUpdater(self.database_root, self.__configuration_map['database_structure'])
        return updater.update_words_database(feature_name=self.feature, values=self.values)

    def update_most_frequent_words_in_db(self, feature_data):
        most_frequent_extractor = MostFrequentWordsExtractor(
            feature_data, self.__configuration_map)
        return most_frequent_extractor.update_most_frequent_words_in_db(feature_name=self.feature, values=self.values)
