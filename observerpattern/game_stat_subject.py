from abc import ABCMeta, abstractmethod
from observerpattern import game_stat_observer

class GameStateSubject(object):
    __metaclass__ = ABCMeta
    _observers = set()

    def attach(self, observer):

    def detach(self, observer):

    def notify(self, value=None):

