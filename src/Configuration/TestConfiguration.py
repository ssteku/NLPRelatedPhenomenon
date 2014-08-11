from Configuration import Configuration
from pybrain.structure.modules   import LinearLayer,StateDependentLayer,GaussianLayer,SoftmaxLayer, SigmoidLayer,LSTMLayer, TanhLayer
from SetSizeConfig import SetSizeConfig
from EpochsNumberConfig import EpochsNumberConfig
from MostFreqWordsConfig import MostFreqWordsConfig
from MostInformativeFeaturesConfig import MostInformativeFeaturesConfig
from MaxentItersConfig import MaxentItersConfig
class TestConfiguration(Configuration):
    def __init__(self):
        super(TestConfiguration, self).__init__()
        self.__create_test_conf()

    def get_configuration_map(self):
            return self.test_conf

    def __create_test_conf(self):
        self.test_conf = {
            'test_plan' : {
                # 'epochs_test' : {
                #     'description' : "Chart of relation between number of learning epochs and classification accuracy for Multi Layer Perceptron",
                #     'title' : "hidden_node_test",
                #     'min_value' : 1,
                #     'max_value' : 20,
                #     'step' : 1,
                #     'x_title' : 'Number of training epochs for Multi Layer Perceptron',
                #     'y_title' : 'Average accuracy',
                #     'classifiers' : ['MLPClassifier'],
                #     'param_name' : ['mlp_classifier_config', 'epochs'],
                #     'results' : {
                #         'levels' : {
                #             '1' : {},
                #             '2' : {},
                #             '3' : {},
                #         },
                #         'bigrams' : {}
                #     },
                #     'config' : EpochsNumberConfig()
                # },

                # 'maxent_iter_test' : {
                #     'description' : "Chart of relation between number of learning iterations and classification accuracy for Maxent classifier",
                #     'title' : "maxent_iter_test",
                #     'min_value' : 1,
                #     'max_value' : 20,
                #     'step' : 1,
                #     'x_title' : 'Number of training iterations for Maxent classifier',
                #     'y_title' : 'Average accuracy',
                #     'classifiers' : ['MaxentClassifier'],
                #     'param_name' : ['maxent_classifier_config', 'max_iter'],
                #     'results' : {
                #         'levels' : {
                #             '1' : {},
                #             '2' : {},
                #             '3' : {},
                #         },
                #         'bigrams' : {}
                #     },
                #     'config' : MaxentItersConfig()
                # },

                # 'most_frequent_words_number_per_value test' : {
                #     'description' : "Chart of relation between number of most frequent words used as a feature vector and accuracy",
                #     'title' : "most_frequent_words_number_per_valuetest",
                #     'min_value' : 100,
                #     'max_value' : 2000,
                #     'step' : 100,
                #     'x_title' : 'Number of most frequent words used as a feature vector',
                #     'y_title' : 'Average accuracy',
                #     'classifiers' : ['NaiveBayesClassifier', 'MLPClassifier', 'DecisionTreeClassifier', 'MaxentClassifier'],
                #     'param_name' : ['most_frequent_words_number_per_value'],
                #     'results' : {
                #         'levels' : {
                #             '1' : {},
                #             '2' : {},
                #             '3' : {},
                #         },
                #         'bigrams' : {}
                #     },
                #     'config' : MostFreqWordsConfig()
                # },

                # 'most_frequent_words_number_per_small_value test' : {
                #     'description' : "Chart of relation between number of most frequent words used as a feature vector and accuracy",
                #     'title' : "most_frequent_words_number_per_small_valuetest",
                #     'min_value' : 1,
                #     'max_value' : 20,
                #     'step' : 1,
                #     'x_title' : 'Number of most frequent words used as a feature vector',
                #     'y_title' : 'Average accuracy',
                #     'classifiers' : ['NaiveBayesClassifier', 'MLPClassifier', 'DecisionTreeClassifier', 'MaxentClassifier'],
                #     'param_name' : ['most_frequent_words_number_per_value'],
                #     'results' : {
                #         'levels' : {
                #             '1' : {},
                #             '2' : {},
                #             '3' : {},
                #         },
                #         'bigrams' : {}
                #     },
                #     'config' : MostFreqWordsConfig()
                # },

                # 'most_informative_features_number_test' : {
                #     'description' : "Chart of relation between number of most informative words used as a feature vector and accuracy",
                #     'title' : "most_informative_features_number test",
                #     'min_value' : 1,
                #     'max_value' : 20,
                #     'step' : 1,
                #     'x_title' : 'Number of most informative words used as a feature vector',
                #     'y_title' : 'Average accuracy',
                #     'classifiers' : ['NaiveBayesClassifier', 'MLPClassifier', 'DecisionTreeClassifier', 'MaxentClassifier'],
                #     'param_name' : ['most_informative_features_number'],
                #     'results' : {
                #         'levels' : {
                #             '1' : {},
                #             '2' : {},
                #             '3' : {},
                #         },
                #         'bigrams' : {}
                #     },
                #     'config' : MostInformativeFeaturesConfig()
                # },
                # 'most_informative_features_number_test2' : {
                #     'description' : "Chart of relation between number of most informative words used as a feature vector and accuracy",
                #     'title' : "most_informative_features_number test2",
                #     'min_value' : 10,
                #     'max_value' : 200,
                #     'step' : 10,
                #     'x_title' : 'Number of most informative words used as a feature vector',
                #     'y_title' : 'Average accuracy',
                #     'classifiers' : ['MLPClassifier'],
                #     'param_name' : ['most_informative_features_number'],
                #     'results' : {
                #         'levels' : {
                #             '1' : {},
                #             '2' : {},
                #             '3' : {},
                #         },
                #         'bigrams' : {}
                #     },
                #     'config' : MostInformativeFeaturesConfig()
                # },

                #  'most_informative_features_number_test_bayes' : {
                #     'description' : "Chart of relation between number of most informative words used as a feature vector and accuracy",
                #     'title' : "most_informative_features_number_test_bayes",
                #     'min_value' : 10,
                #     'max_value' : 200,
                #     'step' : 10,
                #     'x_title' : 'Number of most informative words used as a feature vector',
                #     'y_title' : 'Average accuracy',
                #     'classifiers' : ['NaiveBayesClassifier'],
                #     'param_name' : ['most_informative_features_number'],
                #     'results' : {
                #         'levels' : {
                #             '1' : {},
                #             '2' : {},
                #             '3' : {},
                #         },
                #         'bigrams' : {}
                #     },
                #     'config' : MostInformativeFeaturesConfig()
                # },
                # 'training_to_test_set_size_ratio_test' : {
                #     'description' : "Chart of relation of training set size to accuracy of classification.",
                #     'title' : "training_to_test_set_size_ratio_test",
                #     'min_value' : 0.05,
                #     'max_value' : 1.0,
                #     'step' : 0.05,
                #     'x_title' : 'Ratio of training set size to test set size',
                #     'y_title' : 'Average accuracy',
                #     'classifiers' : ['NaiveBayesClassifier', 'MLPClassifier', 'DecisionTreeClassifier', 'MaxentClassifier'],
                #     'param_name' : ['training_to_test_set_size_ratio'],
                #     'results' : {
                #         'levels' : {
                #             '1' : {},
                #             '2' : {},
                #             '3' : {},
                #         },
                #         'bigrams' : {}
                #     },
                #     'config' : SetSizeConfig()

                # }

            }
        }