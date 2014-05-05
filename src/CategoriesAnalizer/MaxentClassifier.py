import nltk
class MaxentClassifier(object):
    def __init__(self):
        print "MaxentClassifier"

    def trainClasifier(self, training_set):
        algorithm = nltk.classify.MaxentClassifier.ALGORITHMS[1]
        self.__classifier = nltk.MaxentClassifier.train(training_set, algorithm, max_iter=33)

    def testClasifier(self, test_set):
        print "testClasifier, accuracy:"
        print nltk.classify.accuracy(self.__classifier, test_set)
        self.__classifier.show_most_informative_features(8)

    def check_class(self, features_map):
        print "Todo check_class"
