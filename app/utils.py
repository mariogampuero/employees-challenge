from tempfile import NamedTemporaryFile
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType
from fields import Fields
from constants import Constants

class Utils:
    async def create_temporary_file(self, file):
        with NamedTemporaryFile(delete=False, suffix=Constants.CSV_SUFIX) as temporary_file:
            temporary_path = temporary_file.name
            content = await file.read()
            temporary_file.write(content)
        return temporary_path

    def get_departments_schema(self):
        return StructType([
            StructField(Fields.ID_FIELD, IntegerType(), True),
            StructField(Fields.DEPARTMENT_FIELD, StringType(), True)
        ])

    def get_jobs_schema(self):
        return StructType([
            StructField(Fields.ID_FIELD, IntegerType(), True),
            StructField(Fields.JOB_FIELD, StringType(), True)
        ])

    def get_employees_schema(self):
        return StructType([
            StructField(Fields.ID_FIELD, IntegerType(), True),
            StructField(Fields.EMPLOYEE_NAME_FIELD, StringType(), True),
            StructField(Fields.HIRE_DATE_FIELD, DateType(), True),
            StructField(Fields.JOB_ID_FIELD, IntegerType(), True),
            StructField(Fields.DEPARTMENT_ID_FIELD, IntegerType(), True),
        ])

    def write_dataframe_to_mysql_database(self, df, table):
        df.write \
            .format("jdbc") \
            .option("url", f"jdbc:mysql://localhost:3306/{Constants.DATABASE_NAME}") \
            .option("dbtable", table) \
            .option("user", Constants.DB_USERNAME) \
            .option("password", Constants.DB_PASS) \
            .option("batchsize", Constants.BATCH_SIZE) \
            .mode("append") \
            .save()
