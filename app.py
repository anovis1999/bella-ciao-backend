import uvicorn
from fastapi import FastAPI
import search_takala
import pull_takalot
import takala_status
import hashlib
import time
from fastapi.encoders import jsonable_encoder
from mongodb_api import mongodb
import takala

app = FastAPI()


@app.get("/")
def is_alive():
    return {"status": "Alive"}


@app.post("/random")
def get_random_id():
    hash = hashlib.sha1()
    hash.update(str(time.time()).encode("utf-8"))
    return hash.hexdigest()[:10]

@app.post("/newtakala")
def new_failure(params: takala.Item):
    my_mongodb = mongodb("mongodb://localhost:27017/", "bella-ciao", "takala")
    conn = my_mongodb.mongo_get_connection()
    my_mongodb.mongo_insert_document(conn, jsonable_encoder(params))

    return "tair do your job pls"


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