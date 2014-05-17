from Configuration import Configuration
from pybrain.structure.modules   import LinearLayer,StateDependentLayer,GaussianLayer,SoftmaxLayer, SigmoidLayer,LSTMLayer, TanhLayer

class TestConfiguration(Configuration):
    def __init__(self):
        super(TestConfiguration, self).__init__()
        self.__create_test_conf()

    def get_configuration_map(self):
            return self.test_conf

    def __create_test_conf(self):
        self.test_conf = {
            'test_plan' : {
                # 'hidden_nodes_test' : {
                #     'description' : "Hidden node test!!",
                #     'title' : "hidden_node_test",
                #     'min_value' : 2,
                #     'max_value' : 200,
                #     'step' : 2,
                #     'classifiers' : ['MLPClassifier'],
                #     'param_name' : ['mlp_classifier_config', 'hidden_nodes'],
                #     'results' : {
                #         'levels' : {
                #             '1' : {},
                #             '2' : {},
                #             '3' : {},
                #         },
                #         'bigrams' : {}
                #     }
                # },

                # 'most_frequent_words_number_per_value test' : {
                #     'description' : "most_frequent_words_number_per_value test!!",
                #     'title' : "most_frequent_words_number_per_valuetest",
                #     'min_value' : 20,
                #     'max_value' : 2000,
                #     'step' : 20,
                #     'classifiers' : ['NaiveBayesClassifier', 'MLPClassifier'],
                #     'param_name' : ['most_frequent_words_number_per_value'],
                #     'results' : {
                #         'levels' : {
                #             '1' : {},
                #             '2' : {},
                #             '3' : {},
                #         },
                #         'bigrams' : {}
                #     }
                # },

                # 'most_informative_features_number_test' : {
                #     'description' : "most_informative_features_number test!!",
                #     'title' : "most_informative_features_number test",
                #     'min_value' : 2,
                #     'max_value' : 200,
                #     'step' : 2,
                #     'classifiers' : ['NaiveBayesClassifier', 'MLPClassifier'],
                #     'param_name' : ['most_informative_features_number'],
                #     'results' : {
                #         'levels' : {
                #             '1' : {},
                #             '2' : {},
                #             '3' : {},
                #         },
                #         'bigrams' : {}
                #     }
                # },
                'training_to_test_set_size_ratio_test' : {
                    'description' : "Relation of training set size to accuracy of classification.",
                    'title' : "training_to_test_set_size_ratio_test",
                    'min_value' : 0.05,
                    'max_value' : 1.0,
                    'step' : 0.05,
                    'x_title' : 'Ratio of training set size to test set size',
                    'y_title' : 'Average accuracy',
                    'classifiers' : ['NaiveBayesClassifier', 'MLPClassifier', 'DecisionTreeClassifier', 'MaxentClassifier'],
                    'param_name' : ['training_to_test_set_size_ratio'],
                    'results' : {
                        'levels' : {
                            '1' : {},
                            '2' : {},
                            '3' : {},
                        },
                        'bigrams' : {}
                    }
                }

            }
        }