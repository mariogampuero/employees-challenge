from fastapi import FastAPI, UploadFile, File
from db_connection import DbConnection
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from utils import Utils
from constants import Constants
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
    print(table)
    db = DbConnection()
    utils = Utils()
    db.create_challenge_database()
    db.create_challenge_tables()
    temporary_path = await utils.create_temporary_file(file)
    match table:
        case Constants.DEPARTMENTS_TABLE:
            schema = StructType([
                StructField("id", IntegerType(), True),
                StructField("department", StringType(), True),
            ])
        case Constants.JOBS_TABLE:
            schema = StructType([
                StructField("id", IntegerType(), True),
                StructField("job", StringType(), True),
            ])
        case Constants.EMPLOYEES_TABLE:
            schema = StructType([
                StructField("id", IntegerType(), True),
                StructField("employee_name", StringType(), True),
                StructField("hire_date", DateType(), True),
                StructField("job_id", IntegerType(), True),
                StructField("department_id", IntegerType(), True),
            ])
        case _:
            return {'error': 'Must provide a table name'}

    df = spark.read.csv(temporary_path, header=False, inferSchema=False, schema=schema)
    df.write \
        .format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/challenge_db") \
        .option("dbtable", table) \
        .option("user", "root") \
        .option("password", "root") \
        .option("batchsize", 1000) \
        .mode("append") \
        .save()
    return {'status': 'OK', 'message': f'CSV written into {table} Table'}
