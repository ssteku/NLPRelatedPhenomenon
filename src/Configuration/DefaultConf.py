from Configuration import Configuration
from pybrain.structure.modules   import LinearLayer,StateDependentLayer,GaussianLayer,SoftmaxLayer, SigmoidLayer,LSTMLayer, TanhLayer

class DefaultConf(Configuration):
    def __init__(self):
        super(DefaultConf, self).__init__()
        self.__create_default_conf()

    def get_configuration_map(self):
            return self.default_conf

    def __create_default_conf(self):
        self.default_conf = {
            'database_path' : '/home/ssteku/Database/Database.fs',
            'feature_db_name_suffix' : '_words',
            'articles_database_name' : 'articles_db',
            'most_frequent_bigrams_number_per_value' : 40,
            'most_frequent_words_number_per_value' : 5,
            'minimal_training_set_size' : 100,
            'training_to_test_set_size_ratio' : 0.9,
            'extracted_bigrams_number' : 40,
            'bigrams_cleaning_level' : 3,
            'related_words_minimum_similarity_level' : 0.9,
            'related_words_maximum_path_distance' : 2,
            'language_match_minimum_probability' : 0.85,
            'article_minimum_words_number' : 200,
            'number_of_words_extracted_from_article' : 40,
            'most_informative_features_number' : 40,
            'filter_best_features' : False,
            'repeat_test_count' : 100,
            'classifiers' : ['MLPClassifier', 'NaiveBayesClassifier'],
            'database_structure' : {'bigrams' : [], 'levels': ['1', '2', '3']},
            'webpages_list' : [
                "http://news.yahoo.com/",
                "http://bbc.com/",
                "http://cnn.com"
            ],
            'mlp_classifier_config' : {
                'hidden_nodes' : 15,
                'learningRateArg' : 0.004,
                'momentumArg' : 0.99,
                'biasArg' : True,
                'recurrentArg' : True,
                'hiddenclassArg' : SoftmaxLayer,
                'outclassArg' : SoftmaxLayer,
                'epochs' : 11,
                'continueEpochs' : 12,
                'verbose' : False
            }
        }