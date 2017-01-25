from abc import ABCMeta, abstractmethod

class GameStateAbsObserver(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, value):
        pass
