import uvicorn
from fastapi import FastAPI
import search_takala
import my_takalot


app = FastAPI()


@app.get("/")
def is_alive():
    return {"status": "Alive"}


@app.post("/newtakala")
def new_takala():
    return "tair do your job please"


@app.post("/searchtakala")
def search_takala_id(ID: int):
    takala = search_takala.search_takala_in_mongo(ID)
    return str(takala)


@app.post("/mytakalot")
def my_board(USER: str):
    takala = my_takalot.get_all_takalot_board(USER)
    return takala


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)