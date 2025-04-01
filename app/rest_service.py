from fastapi import FastAPI, UploadFile, File
from db_connection import DbConnection
from pyspark.sql import SparkSession
from utils import Utils
from constants import Constants
app = FastAPI()

spark = SparkSession.builder \
    .appName("Globant Challenge") \
    .config("spark.jars", "../spark/mysql-connector-j-9.2.0.jar") \
    .getOrCreate()
@app.get("/")
def get_test():
    return {'message': 'Test GET OK'}

@app.post("/upload_csv/")
async def upload_csv_to_db(file: UploadFile = File(...), table: str = None):
    print(table)
    db = DbConnection()
    utils = Utils()
    db.create_challenge_database()
    db.create_challenge_tables()
    temporary_path = await utils.create_temporary_file(file)
    if table == Constants.DEPARTMENTS_TABLE:
            schema = utils.get_departments_schema()
    elif table == Constants.JOBS_TABLE:
            schema = utils.get_jobs_schema()
    elif table == Constants.EMPLOYEES_TABLE:
            schema = utils.get_employees_schema()
    else:
        return {'error': 'Must provide a table name'}

    df = spark.read.csv(temporary_path, header=False, inferSchema=False, schema=schema)
    utils.write_dataframe_to_mysql_database(df, table)
    return {'status': 'OK', 'message': f'CSV written into {table} Table'}
