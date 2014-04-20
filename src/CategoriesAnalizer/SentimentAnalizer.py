from SentimentWordsDatabaseUpdater import SentimentWordsDatabaseUpdater
from MostFrequentWordsExtractor import MostFrequentWordsExtractor
class SentimentAnalizer(object):
    def __init__(self, database, database_structure):
        self.database_root = database.dbroot
        self.database_structure = database_structure
    def update_words_database(self):
        updater = SentimentWordsDatabaseUpdater(self.database_root, self.database_structure)
        updater.update_words_database()

    def update_most_frequent_words_in_db(self):
        most_frequent_extractor = MostFrequentWordsExtractor(self.database_root, self.database_structure)
        most_frequent_extractor.update_most_frequent_words_in_db()
