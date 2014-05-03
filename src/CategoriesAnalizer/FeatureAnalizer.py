from FeatureWordsDatabaseUpdater import FeatureWordsDatabaseUpdater
from MostFrequentWordsExtractor import MostFrequentWordsExtractor
class FeatureAnalizer(object):
    def __init__(self, database, database_structure, feature, values):
        self.database_root = database.dbroot
        self.database_structure = database_structure
        self.feature = feature
        self.values = values
    def update_words_database(self):
        updater = FeatureWordsDatabaseUpdater(self.database_root, self.database_structure)
        updater.update_words_database(feature_name=self.feature, values=self.values)

    def update_most_frequent_words_in_db(self):
        most_frequent_extractor = MostFrequentWordsExtractor(self.database_root, self.database_structure)
        most_frequent_extractor.update_most_frequent_words_in_db(feature_name=self.feature, values=self.values)
