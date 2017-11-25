
class FeatureExtractor(object):
    def __init__(self, most_frequent_words):
        print("FeatureExtractor")
        self.__most_frequent_words = most_frequent_words

    def get_most_frequent_words_features(self, article_record, feature_name):
        levels = article_record.frequency_distribution_levels
        if hasattr(article_record, feature_name):
            feature_value = getattr(article_record, feature_name)
        else:
            feature_value = None
            raise Exception('No feature found for article')
        features_for_levels = dict()
        for level in self.__most_frequent_words['levels'].keys():
            most_frequent_for_values = self.__most_frequent_words['levels'][level]
            article_most_frequent = levels[level]
            articles_features_map = self.__get_most_freq_map(article_most_frequent, dict())
            features_map = self.__get_features_for_level(most_frequent_for_values)
            # print "Feature map len : " + str(len(features_map))
            features_for_levels[level] = (self.__create_feature_map(articles_features_map, features_map), feature_value)

        return features_for_levels

    def __create_feature_map(self, articles_features_map, features_map):
        feature_vector = dict()
        for keyword in features_map:
            if articles_features_map.has_key(keyword):
                feature_vector[keyword] = True
            else:
                feature_vector[keyword] = False
        return feature_vector

    def __get_features_for_level(self,  most_frequent_for_values):
        features_map = dict()
        for value in most_frequent_for_values.keys():
            self.__get_most_freq_map(most_frequent_for_values[value], features_map)
        return features_map

    def __get_most_freq_map(self, most_freq_list, most_freq_map):
        for element in most_freq_list:
            most_freq_map[element[0]] = False
        return most_freq_map

