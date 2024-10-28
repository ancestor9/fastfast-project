from fastapi import FastAPI, Body, Header
import pandas as pd       
import numpy as np   

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/hi")
def greet():
    return "Hi...... This is hi endpoint"

# path 와 query
@app.get("/hi/{who}")
def greet_who_path(who):
    return f"Hello! {who}?"

@app.get("/hi")
def greet_who_query(who):
    return f"Hello! {who}?"

# dataframe serialization
df = pd.DataFrame(np.arange(50).reshape(5,10), index=['A', 'B', 'C', 'D', 'E'])
print(df)
print(df.to_dict())

@app.get("/data")
def show_data():
    return f"Hello! {df.to_dict()}"

# post
@app.post("/hipostbody")
def greet_who_query_bodypost(who: str = Body(embed=True)):
    return f"Hello! {who}?"

# post
@app.post("/hipostheader")
def greet_who_query_headpost(who: str = Header(embed=True)):
    return f"Hello! {who}?"