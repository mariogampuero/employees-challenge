from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def get_test():
    return {'message': 'Test GET OK'}

