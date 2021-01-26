import uvicorn
from fastapi import FastAPI
from search_takala import search_takala_in_mongo


app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "Alive"}


@app.post("/newtakala")
def new_takala():
    return "tair do your job please"


@app.post("/searchtakala")
def search_takala(ID: int):
    takala = search_takala_in_mongo(ID)
    return str(takala)


@app.post("/mytakalot")
def my_board():
    return "pashoshi?"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)