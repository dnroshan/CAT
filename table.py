
import pymysql
import config

class Table:
    def connect(self):
        return pymysql.connect(host=config.HOST,
                               user=config.USER,
                               passwd=config.PASSWORD,
                               db=config.DATABASE)

