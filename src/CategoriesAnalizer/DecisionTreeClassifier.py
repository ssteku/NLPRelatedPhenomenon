import nltk
class DecisionTreeClassifier(object):
    def __init__(self):
        print "DecisionTree"

    def trainClasifier(self, training_set):
        self.classifier = nltk.DecisionTreeClassifier.train(training_set)

    def testClasifier(self, test_set):
        print "testClasifier, accuracy:"
        print nltk.classify.accuracy(self.classifier, test_set)

    def check_class(self, features_map):
        print "Todo check_class"
