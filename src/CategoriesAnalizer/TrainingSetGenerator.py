from FeatureExtractor import FeatureExtractor
from Classifiers.NaiveBayesClassifier import NaiveBayesClassifier
class TrainingSetGenerator(object):
    def __init__(self, feature_name, configuration_map):
        print "Set gen"
        self.feature_name = feature_name
        self.__configuration_map = configuration_map

    def get_training_set(self, article_db, most_frequent_words, level):
        training_set = []
        extractor = FeatureExtractor(most_frequent_words)
        for key in article_db.keys():
            if hasattr(article_db[key], self.feature_name):
                most_frequent_words = extractor.get_most_frequent_words_features(article_db[key], self.feature_name)[level]
                training_set.append(most_frequent_words)
        if self.__configuration_map['filter_best_features']:
            return self.__get_most_informative_features(training_set)
        else:
            return training_set


    def __get_most_informative_features(self, training_set):
        classifier = NaiveBayesClassifier(self.__configuration_map)
        classifier.trainClasifier(training_set)
        best_features = classifier.get_most_informative_features()
        best_features_list = self.__get_best_features_list(best_features)
        result_features = []
        for feature_data in training_set:
            result_map = {}
            for feature in feature_data[0]:
                if feature in best_features_list:
                    result_map[feature] = feature_data[0][feature]
            result_features.append((result_map, feature_data[1]))
            # print "result_map len: " + str(len(result_map))
        return result_features

    def __get_best_features_list(self, best_features):
        result_list = []
        for feature in best_features:
            result_list.append(feature[0])
        return result_list
