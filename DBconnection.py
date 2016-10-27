from PyQt5.QtSql import QSqlDatabase
def setup_connection ():
    try :
        connection =QSqlDatabase.addDatabase('QSQLITE')
    except:
        return False



    return connection