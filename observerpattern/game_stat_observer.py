from abc import ABCMeta, abstractmethod

class GameStateObserver(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self,value):
        pass
