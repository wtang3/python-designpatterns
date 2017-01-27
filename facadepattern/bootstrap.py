from abc import ABCMeta, abstractmethod

class Bootstrap:
    __metaclass__ = ABCMeta

    @abstractmethod
    def bootstrap(self):
        pass