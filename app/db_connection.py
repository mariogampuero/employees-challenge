import pymysql
from db_queries import DbQueries
from constants import Constants
class DbConnection:

    def create_connection(self, database=None):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database=database
        )
        return connection

    def execute_queries(self, connection, queries):
        try:
            cursor = connection.cursor()
            for query in queries:
                cursor.execute(query)
            cursor.close()
        except pymysql.MySQLError as e:
            print(f"Error: {e}")
        finally:
            connection.close()
    def create_challenge_database(self):
        connection = self.create_connection()
        self.execute_queries(connection, [DbQueries.CREATE_DATABASE_QUERY])

    def create_challenge_tables(self):
        connection = self.create_connection(Constants.DATABASE_NAME)
        self.execute_queries(connection, [
            DbQueries.CREATE_DEPARTMENTS_TABLE_QUERY,
            DbQueries.CREATE_JOBS_TABLE_QUERY,
            DbQueries.CREATE_EMPLOYEES_TABLE_QUERY
        ])