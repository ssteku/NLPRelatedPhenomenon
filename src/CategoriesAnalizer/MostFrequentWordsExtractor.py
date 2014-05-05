from BTrees.OOBTree import OOBTree
from nltk import FreqDist
import transaction

class MostFrequentWordsExtractor(object):
    def __init__(self, database, database_structure, configuration_map):
        self.database_root = database
        self.database_structure = database_structure
        self.__configuration_map = configuration_map

    def get_most_frequent_words_from_db(self, feature_name):
        words_database = self.__get_feature_database(feature_name)
        return words_database['levels']

    def get_most_frequent_bigrams_from_db(self, feature_name):
        words_database = self.__get_feature_database(feature_name)
        return words_database['bigrams']

    def update_most_frequent_words_in_db(self, feature_name, values):
        words_database = self.__get_feature_database(feature_name)
        self.__fillDatabaseWithMostFrequentWords(words_database, values)

    def __get_feature_database(self, feature_name):
        return self.database_root[feature_name+'_words'];

    def __fillDatabaseWithMostFrequentWords(self, words_database, values):
        self.__extract_bigram_words(words_database['bigrams'], values)
        self.__extract_level_words(words_database['levels'], '1', values)
        self.__extract_level_words(words_database['levels'], '2', values)
        self.__extract_level_words(words_database['levels'], '3', values)
        transaction.commit()

    def __extract_bigram_words(self, bigrams, values):
        bigrams_number_per_value = self.__configuration_map["most_frequent_bigrams_number_per_value"]
        for value in values:
            fdist = FreqDist(bigrams[value])
            bigrams['most_frequent'][value] = fdist.items()[:bigrams_number_per_value]
            bigrams._p_changed = True
            transaction.commit()

    def __extract_level_words(self, levels_db, level, values):
        words_number_per_value = self.__configuration_map["most_frequent_words_number_per_value"]
        for value in values:
            fdist = FreqDist()
            for word_dist in levels_db[level][value]:
                fdist.inc(word_dist[0], count = word_dist[1])

            levels_db[level]['most_frequent'][value] = fdist.items()[:words_number_per_value]
            levels_db[level]._p_changed = True
            transaction.commit()
