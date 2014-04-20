from MostFrequentWordsExtractor import MostFrequentWordsExtractor

class FeatureExtractor(object):
    def __init__(self, feature_database):
        print "FeatureExtractor"
        self.__feature_database = feature_database

    def get_most_frequent_words_features(self, article):
        print "get_most_frequent_words_features article: " + article.title
        freqExtractor = MostFrequentWordsExtractor()
        levels = freqExtractor.get_most_frequent(article.text, 100)
        levels_db = self.__feature_database['levels']
        for level in levels_db.keys():
            print level


