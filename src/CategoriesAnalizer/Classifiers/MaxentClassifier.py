import nltk
from BaseClassifier import BaseClassifier

class MaxentClassifier(BaseClassifier):
    def __init__(self, configuration_map):
        super(MaxentClassifier, self).__init__(configuration_map)

    def trainClasifier(self, training_set):
        algorithm = nltk.classify.MaxentClassifier.ALGORITHMS[1]
        self.__classifier = nltk.MaxentClassifier.train(training_set, algorithm, max_iter=11)

    def testClasifier(self, test_set):
        print "testClasifier, accuracy:"
        accuracy =  nltk.classify.accuracy(self.__classifier, test_set)
        print accuracy
        features_number = self.configuration_map['most_informative_features_number']
        self.__classifier.show_most_informative_features(features_number)
        return accuracy


    def check_class(self, features_map):
        print "Todo check_class"
