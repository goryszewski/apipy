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

    def get_params(self,paramType):
        sql="select * from params where paramType =?"
        return self._exec_sql_tuple(self,sql,paramType)

    def add_params(self,paramType,paramValue,modifyDate):
        sql = """
                insert into `params` (paramType,paramValue,modifyDate)
                values (?, ?, ?)
              """
        dataTuple=(paramType,paramValue,modifyDate)
        return self._exec_sql_tuple(sql,dataTuple)

    def _exec_sql_tuple(self,sql,dataTuple):
        return  self.cur.execute(sql,dataTuple)

    def _exec_sql(self,sql):
        return  self.cur.execute(sql)

    def __del__(self):
        self.cnx.close()
