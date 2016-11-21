from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtSql import QSqlQuery\

class DbConnection:

    def __init__(self,dbname):
         self.db_connection=QSqlDatabase.addDatabase("QSQLITE")
         self.db_connection.setDatabaseName(dbname)
         self.db_connection.open()
         self.DBquery = QSqlQuery()