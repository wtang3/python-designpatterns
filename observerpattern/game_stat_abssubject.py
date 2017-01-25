from abc import ABCMeta, abstractmethod
from observerpattern.game_stat_absobserver import GameStateAbsObserver

class GameStateAbsSubject(object):
    __metaclass__ = ABCMeta
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, GameStateAbsObserver):
            raise TypeError('Wrong type')
        self._observers.add(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, value=None):
        for observers in self._observers:
            if value is None:
                observers.update()
            else:
                observers.update(value)
