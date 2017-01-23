

class DatabaseConnection():

    def __init__(self, database_strategy):
        self.database_strategy = database_strategy

    def connect_to_db(self, host, user, passwd, db):
        status = self.database_strategy.dbconnection(host, user, passwd, db)
        return status
