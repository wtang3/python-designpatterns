from abc import ABCMeta, abstractmethod


class DatabaseStrategy(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def dbconnection(self, host, user, passwd, db):
        """ default db connection"""
        return False
