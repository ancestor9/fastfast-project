from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hi")
def greet():
    return "Hi...... This is hi endpoint"

from fastapi import FastAPI