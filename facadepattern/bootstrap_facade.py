from abc import ABCMeta, abstractmethod

class BootstrapFacade:
    __metaclass__ = ABCMeta

    @abstractmethod
    def bootstrap(self):
        pass