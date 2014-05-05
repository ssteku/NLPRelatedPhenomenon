import nltk
class NaiveBayesClassifier(object):
    def __init__(self):
        print "Bayes"

    def trainClasifier(self, training_set):
        self.classifier = nltk.NaiveBayesClassifier.train(training_set)

    def testClasifier(self, test_set):
        print "testClasifier, accuracy:"
        print nltk.classify.accuracy(self.classifier, test_set)
        # TODO configuration value
        self.classifier.show_most_informative_features(8)

    def check_class(self, features_map):
        print "Todo check_class"
