import uvicorn
from fastapi import FastAPI
import search_takala
import pull_takalot


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
    return takala


@app.post("/mytakalot")
def my_board(USER: str):
    takala = pull_takalot.get_all_takalot_board(USER)
    return takala


@app.post("/teamtakalot")
def my_team_board(TEAM: str):
    takala = pull_takalot.get_all_team_takalot(TEAM)
    return takala


@app.post("/transfertakala")
def my_board(TEAM: str):
    return "ofir code here"


@app.post("/addtakalanotification")
def my_board(MESSAGE: str):
    return "yoav code here"




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)