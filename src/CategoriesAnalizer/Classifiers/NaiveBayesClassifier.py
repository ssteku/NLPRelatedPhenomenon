import nltk

from src.CategoriesAnalizer.Classifiers.BaseClassifier import BaseClassifier


class NaiveBayesClassifier(BaseClassifier):
    def __init__(self, configuration_map):
        super(NaiveBayesClassifier, self).__init__(configuration_map)

    def trainClasifier(self, training_set):
        self.classifier = nltk.NaiveBayesClassifier.train(training_set)

    def testClasifier(self, test_set):
        print("testClasifier, accuracy:")
        accuracy = nltk.classify.accuracy(self.classifier, test_set)
        print(accuracy)
        features_number = self.configuration_map['most_informative_features_number']
        # self.classifier.show_most_informative_features(features_number)
        return accuracy
    def get_most_informative_features(self):
        features_number = self.configuration_map['most_informative_features_number']
        return self.classifier.most_informative_features(features_number)

    def check_class(self, features_map):
        print("Todo check_class")
