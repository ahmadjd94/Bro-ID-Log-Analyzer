from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtSql import QSqlQuery
class DBconnection:

def __init__(self):
    self.db_connection =QSqlDatabase.addDatabase("QSQLITE")
    self.DBquery=QSqlQuery()
