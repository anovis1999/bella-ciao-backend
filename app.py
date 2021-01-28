import uvicorn
from fastapi import FastAPI
import search_takala
import pull_takalot
import takala_status
import new_takala
import takala

app = FastAPI()


@app.get("/")
def is_alive():
    return {"status": "Alive"}


@app.post("/random")
def get_random_id():
    return new_takala.get_random_takala_id()


@app.post("/newtakala")
def new_failure(params: takala.Item):
    return new_takala.add_takala(params)


@app.post("/searchtakala")
def search_takala_id(takala_id: str):
    takala = search_takala.search_takala_in_mongo(takala_id)
    return takala


@app.post("/mytakalot")
def my_board(user: str):
    takala = pull_takalot.get_all_takalot_board(user)
    return takala


@app.post("/teamtakalot")
def my_team_board(team: str):
    takala = pull_takalot.get_all_team_takalot(team)
    return takala


@app.post("/changestatus")
def change_takala_status(takala_id: str ,wanted_status: str, current_status: str):
    takala = takala_status.change_takala_status(takala_id,wanted_status, current_status)
    return takala


@app.post("/transfertakala")
def change_team(team: str):
    return "ofir code here"


@app.post("/addtakalanotification")
def add_notification(takala_id: str,message: str):
    return "yoav code here"

@app.post("/returntakalanotifications")
def get_notifications(takala_id: str,message: str):
    return "yoav code here"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
