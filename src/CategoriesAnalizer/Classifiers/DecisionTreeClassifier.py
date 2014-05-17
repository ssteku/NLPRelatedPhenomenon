import nltk
from BaseClassifier import BaseClassifier
class DecisionTreeClassifier(BaseClassifier):
    def __init__(self, configuration_map):
        super(DecisionTreeClassifier, self).__init__(configuration_map)

    def trainClasifier(self, training_set):
        self.classifier = nltk.DecisionTreeClassifier.train(training_set)

    def testClasifier(self, test_set):
        print "testClasifier, accuracy:"
        accuracy =  nltk.classify.accuracy(self.classifier, test_set)
        print accuracy
        return accuracy

    def check_class(self, features_map):
        print "Todo check_class"
