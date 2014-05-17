from abc import ABCMeta, abstractmethod

class Configuration(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_configuration_map(self):
        raise Exception('Method get_configuration_map is not implemented')
