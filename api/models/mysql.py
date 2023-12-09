import mysql.connector
from mysql.connector import errorcode

# config = {
#   'user': 'user',
#   'password': 'password',
#   'host': '127.0.0.1',
#   'database': 'database',
#   'raise_on_warnings': True
# }

class DB:
    def __init__(self,config):
        self.cnx = mysql.connector.connect(**config)

    def test_connect(self):
        return self.cnx.is_connected()
    
    def _exec_sql(self,sql):
        return self.cnx.execute(sql)

    def __del__(self):
        self.cnx.close()