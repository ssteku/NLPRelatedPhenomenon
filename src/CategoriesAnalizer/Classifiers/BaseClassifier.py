from abc import ABCMeta, abstractmethod

class BaseClassifier(object):
    __metaclass__ = ABCMeta

    def __init__(self, configuration_map):
        self.configuration_map = configuration_map

    @abstractmethod
    def trainClasifier(self, training_set):
        raise Exception('Method trainClasifier is not implemented')

    @abstractmethod
    def testClasifier(self, test_set):
        raise Exception('Method testClasifier is not implemented')

    @abstractmethod
    def check_class(self, features_map):
        raise Exception('Method check_class is not implemented')
