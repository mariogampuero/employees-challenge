from fastapi import FastAPI, UploadFile, File
from db_connection import DbConnection
from pyspark.sql import SparkSession
from utils import Utils
app = FastAPI()

spark = SparkSession.builder \
    .appName("Globant Challenge") \
    .config("spark.jars", "file:///C:/Spark/spark-3.5.5-bin-hadoop3/jars/mysql-connector-j-9.2.0.jar") \
    .getOrCreate()
@app.get("/")
def get_test():
    return {'message': 'Test GET OK'}

@app.post("/upload_csv/")
async def upload_csv_to_db(file: UploadFile = File(...), table: str = None):
    db = DbConnection()
    utils = Utils()
    db.create_challenge_database()
    db.create_challenge_tables()
    temporary_path = await utils.create_temporary_file(file)
    df = spark.read.csv(temporary_path, header=True, inferSchema=True)
    df.show()
    return {'message': 'CSV read in PySpark!'}
