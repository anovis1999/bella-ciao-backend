import uvicorn
from fastapi import FastAPI, File, Form, UploadFile, responses
from fastapi.middleware.cors import CORSMiddleware
import pull_takalot
import takala_status
import new_takala
import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


@app.get("/")
def is_alive():
    return {"status": "Alive"}


@app.post("/createIssue")
async def new_failure(takala_id: str = Form(...), status: str = Form(...), headline: str = Form(...),
                      symptom: str = Form(...), takalaContext: str = Form(...), VOIP: str = Form(...),
                      compName: str = Form(...), compUser: str = Form(...), compPass: str = Form(...)):
    takala_params = {"takala_id": takala_id, "status": status, "headline": headline, "takalaContext": takalaContext,
                     "Symptom": symptom, "VOIP": VOIP, "compName": compName, "compUser": compUser,
                     "compPass": compPass, "messages": []}
    print(takala_params)
    return new_takala.add_takala(takala_params)


@app.post("/uploadFileForIssue")
async def add_new_file(file: UploadFile = File(...), takala_id: str = Form(...)):
    os.mkdir(r"C:\Users\Garbi\PycharmProjects\bella-ciao-backend\{takalaid}".format(takalaid=takala_id))
    with open("{takalaid}/{filename}.".format(takalaid=takala_id, filename=file.filename), "wb") \
            as buffer:
        shutil.copyfileobj(file.file, buffer)
    print("saved file!")
    return "file saved."


@app.get("/getTakala/{takala_id}")
async def search_takala_id(takala_id):
    return str(pull_takalot.get_takala(takala_id))


@app.get("/MytTakalot")
def my_board(user: str = Form(...)):
    return pull_takalot.get_all_takalot_board(user)


@app.post("/TeamTakalot")
def my_team_board(team: str):
    return pull_takalot.get_all_team_takalot(team)


@app.post("/ChangeStatus")
def change_takala_status(takala_id: str, wanted_status: str, current_status: str):
    return takala_status.change_takala_status(takala_id, wanted_status, current_status)


@app.post("/TransferTakala")
def change_team(team: str):
    return "ofir code here"


@app.put("/addMessage")
async def add_message(takala_id: str = Form(...), message: str = Form(...), user: str = Form(...),
                      epoch: int = Form(...)):
    old_document = dict(pull_takalot.get_takala(takala_id))
    new_document = dict(pull_takalot.get_takala(takala_id))
    new_document["messages"].append({"user_name": user, "massage": message, "epoch_time": epoch})
    return new_takala.update_messages(old_document, new_document)


@app.get("/getFile")
async def get_file(takala_id: str = Form(...)):
    try:
        file_path = r"C:\Users\Garbi\PycharmProjects\bella-ciao-backend\{takala_id}".format(takala_id=takala_id) + "\\"\
                    + os.listdir(r"C:\Users\Garbi\PycharmProjects\bella-ciao-backend\{takala_id}".format(takala_id=takala_id))[0]
        return responses.FileResponse(file_path)
    except Exception as e:
        return "cannot fine files. reason: " + str(e)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
