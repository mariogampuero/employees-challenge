import pymysql
from db_queries import DbQueries
class DbConnection:

    def create_connection(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database=None
        )
        return connection

    def create_challenge_database(self):
        connection = self.create_connection()
        try:
            cursor = connection.cursor()
            cursor.execute(DbQueries.CREATE_DATABASE_QUERY)
            cursor.close()
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            connection.close()
