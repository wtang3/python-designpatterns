from strategypattern.database_connection import DatabaseConnection
from strategypattern.mysql_strategy import MysqlStrategy
from strategypattern.mongodb_strategy import MongoDbStrategy

import unittest

class Tests(unittest.TestCase):

    def test_db_mysql_connection(self):
        # Potentially use dependency injection here
        strategy = MysqlStrategy()
        connection = DatabaseConnection(strategy)
        status = connection.connect_to_db("host", "user", "passwd", "db")
        self.assertTrue(status)

    def test_db_mongodb_connection(self):
        # Potentially use dependency injection here
        strategy = MongoDbStrategy()
        connection = DatabaseConnection(strategy)
        status = connection.connect_to_db("host", "user", "passwd", "db")
        self.assertTrue(status)

if __name__ == '__main__':
    unittest.main()
