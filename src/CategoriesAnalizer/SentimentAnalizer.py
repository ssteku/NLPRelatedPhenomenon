from SentimentWordsDatabaseUpdater import SentimentWordsDatabaseUpdater
from MostFrequentWordsExtractor import MostFrequentWordsExtractor
class SentimentAnalizer(object):
    def __init__(self, database):
        self.database_root = database.dbroot

    def updateWordsDatabase(self):
        updater = SentimentWordsDatabaseUpdater(self.database_root)
        updater.updateWordsDatabase()

    def updateMostFrequentWordsInDb(self):
        most_frequent_extractor = MostFrequentWordsExtractor(self.database_root)
        most_frequent_extractor.updateMostFrequentWordsInDb()
 