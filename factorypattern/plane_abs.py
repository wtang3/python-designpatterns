from abc import ABCMeta, abstractmethod

class PlaneAbs(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    def landing(self):
        pass