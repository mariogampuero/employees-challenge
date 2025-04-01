from fastapi import FastAPI
from db_connection import DbConnection

app = FastAPI()
@app.get("/")
def get_test():
    return {'message': 'Test GET OK'}

@app.get("/upload_csv")
def upload_csv_to_db():
    db = DbConnection()
    db.create_challenge_database()
    db.create_challenge_tables()
    return {'message': 'Database and tables created!'}
