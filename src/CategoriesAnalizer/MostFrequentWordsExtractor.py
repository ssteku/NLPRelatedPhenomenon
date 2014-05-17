from BTrees.OOBTree import OOBTree
from nltk import FreqDist
import transaction

class MostFrequentWordsExtractor(object):
    def __init__(self, feature_data, configuration_map):
        self.feature_data = feature_data
        self.__configuration_map = configuration_map

    def get_most_frequent_words_from_db(self, feature_name):
        return self.feature_data['levels']

    def get_most_frequent_bigrams_from_db(self, feature_name):
        return self.feature_data['bigrams']

    def update_most_frequent_words_in_db(self, feature_name, values):
        return self.__fillDatabaseWithMostFrequentWords(self.feature_data, values)


    def __fillDatabaseWithMostFrequentWords(self, words_database, values):
        most_frequent_data = {}
        most_frequent_data['bigrams'] = self.__extract_bigram_words(words_database['bigrams'], values)
        most_frequent_data['levels'] = {}
        most_frequent_data['levels']['1'] = self.__extract_level_words(words_database['levels'], '1', values)
        most_frequent_data['levels']['2'] = self.__extract_level_words(words_database['levels'], '2', values)
        most_frequent_data['levels']['3'] = self.__extract_level_words(words_database['levels'], '3', values)
        return most_frequent_data

    def __extract_bigram_words(self, bigrams, values):
        bigrams_number_per_value = self.__configuration_map["most_frequent_bigrams_number_per_value"]
        most_frequent_bigrams = {}
        for value in values:
            fdist = FreqDist(bigrams[value])
            most_frequent_bigrams[value] = fdist.items()[:bigrams_number_per_value]
        return most_frequent_bigrams

    def __extract_level_words(self, levels_db, level, values):
        words_number_per_value = self.__configuration_map["most_frequent_words_number_per_value"]
        most_freq_words = {}
        for value in values:
            fdist = FreqDist()
            for word_dist in levels_db[level][value]:
                fdist.inc(word_dist[0], count = word_dist[1])

            most_freq_words[value] = fdist.items()[:words_number_per_value]
        return most_freq_words
