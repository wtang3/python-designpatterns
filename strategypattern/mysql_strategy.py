import sys
from strategypattern.database_strategy import DatabaseStrategy

class MysqlStrategy(DatabaseStrategy):

    def dbconnection(self, host, user, passwd, db):
        try:
            print("connecting to mysql")
            print("connected")

            return True
        except Exception:
            print("Unexpected error:", sys.exc_info()[0])
        finally:
            print("close db")

        return False
