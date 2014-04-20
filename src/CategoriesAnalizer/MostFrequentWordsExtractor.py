from BTrees.OOBTree import OOBTree
from nltk import FreqDist
import transaction

class MostFrequentWordsExtractor(object):
    def __init__(self, database, database_structure):
        self.database_root = database
        self.database_structure = database_structure

    def get_most_frequent_words_from_db(self, feature_name='sentiment'):
        words_database = self.__get_feature_database(feature_name)
        return words_database['levels']

    def get_most_frequent_bigrams_from_db(self, feature_name='sentiment'):
        words_database = self.__get_feature_database(feature_name)
        return words_database['bigrams']

    def update_most_frequent_words_in_db(self, feature_name='sentiment', values=['negative', 'positive']):
        words_database = self.__get_feature_database(feature_name)
        self.__fillDatabaseWithMostFrequentWords(words_database, values)

    def __get_feature_database(self, feature_name):
        return self.database_root[feature_name+'_words'];

    def __fillDatabaseWithMostFrequentWords(self, words_database, values):
        self.__extractBigramWords(words_database['bigrams'], values)
        self.__extractLevelWords(words_database['levels'], '1', values)
        self.__extractLevelWords(words_database['levels'], '2', values)
        self.__extractLevelWords(words_database['levels'], '3', values)
        transaction.commit()

    def __extractBigramWords(self, bigrams, values):
        print "__extractBigramWords"
        for value in values:
            fdist = FreqDist(bigrams[value])
            print fdist.items()[:10]
            bigrams['most_frequent'][value] = fdist.items()[:40]
            bigrams._p_changed = True
            transaction.commit()

    def __extractLevelWords(self, levels_db, level, values):
        print "__extractLevelWords level: " + str(level)
        for value in values:
            fdist = FreqDist()
            print "value: " + value
            print 'len: ' + str(len(levels_db[level][value]))
            for word_dist in levels_db[level][value]:
                fdist.inc(word_dist[0], count = word_dist[1])

            print fdist.items()[:10]
            levels_db[level]['most_frequent'][value] = fdist.items()[:200]
            levels_db[level]._p_changed = True
            transaction.commit()
