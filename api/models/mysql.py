import pymysql.cursors



class DB:
    def __init__(self,config):
        self.cnx = pymysql.connect(**config)
        self.cur = self.cnx.cursor()

    def test_connect(self):
        return self.cnx.open

    def list_db(self):
        sql="show databases;"
        return self._exec_sql(sql)

    def _exec_sql(self,sql):
        self.cur.execute(sql)
        return  self.cur.execute(sql)

    def __del__(self):
        self.cnx.close()
