import mysql.connector
from mysql.connector import errorcode
class Connection(object):
    def __init__(self,host='127.0.0.1',database='blog',user='root',password='',port='3306',pool_size=5):
        config = {
            'host':host,
            'database':database,
            'user':user,
            'password':password,
            'port':port,
            'pool_size':pool_size,
            'charset':'utf8'
        }
        try:
            self.con = mysql.connector.connect(**config)
            self.cursor = self.con.cursor(dictionary=True)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('user or password wrong')
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print('database does not exist')
            else:
                print(err)

    def all(self):
        sql = "select * from a"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def only_sql(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()