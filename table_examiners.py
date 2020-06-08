
import pymysql
import config

class TableExaminers:
    def __connect(self):
        return pymysql.connect(host=config.HOST,
                               user=config.USER,
                               passwd=config.PASSWORD,
                               db=config.DATABASE)

    def add(self, data):
        connection = self.__connect()

        with connection as cursor:
            query = 'INSERT INTO examiners VALUES(%s, %s, %s, %s, %s);'
            cursor.execute(query, tuple(data.values()))
            connection.commit()

    def get(self, username):

        connection = self.__connect()

        with connection as cursor:
            query = 'SELECT * FROM examiners WHERE username = %s;'
            cursor.execute(query, username)
            data = cursor.fetchall()

            if not data:
                return None

            data = data[0]

            return {
                'username'  : data[0],
                'first_name': data[1],
                'last_name' : data[2],
                'subject'   : data[3],
                'school'    : data[4]
            }
            

            
