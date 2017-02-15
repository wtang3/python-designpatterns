from abc import ABCMeta, abstractmethod

class PlaneFactoryAbs(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_plane(self):
        pass