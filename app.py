import uvicorn
from fastapi import FastAPI, File, Form, UploadFile, responses, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pull_takalot
import takala_status
import users
import new_takala
import shutil
import os

# create the app
app = FastAPI()

# allow CORS from other computers
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)

# rout to check weather the backend is up or not.
@app.get("/")
def is_alive():
    return {"status": "Alive"}

# use this route to create a new takala.
@app.post("/createIssue")
async def new_failure(takala_id: str = Form(...), status: str = Form(...), headline: str = Form(...),
                      symptom: str = Form(...), takalaContext: str = Form(...), VOIP: str = Form(...),
                      compName: str = Form(...), compUser: str = Form(...), compPass: str = Form(...)):
    takala_params = {"takala_id": takala_id, "status": status, "headline": headline, "takalaContext": takalaContext,
                     "Symptom": symptom, "VOIP": VOIP, "compName": compName, "compUser": compUser,
                     "compPass": compPass, "messages": []}
    print(takala_params)
    return new_takala.add_takala(takala_params)

# use this route to upload a file for a takala. takes one file.
@app.post("/uploadFileForIssue")
async def add_new_file(file: UploadFile = File(...), takala_id: str = Form(...)):
    os.mkdir(r"C:\Users\Garbi\PycharmProjects\bella-ciao-backend\{takalaid}".format(takalaid=takala_id))
    with open("{takalaid}/{filename}.".format(takalaid=takala_id, filename=file.filename), "wb") \
            as buffer:
        shutil.copyfileobj(file.file, buffer)
    print("saved file!")
    return "file saved."

# use this route to get takala json.
@app.get("/getTakala/{takala_id}")
async def search_takala_id(takala_id):
    try:
        takala_to_send = pull_takalot.get_takala(takala_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail="item not found")
    return takala_to_send

# use this route to get all takalot of one user
@app.get("/MytTakalot")
def my_board(user: str = Form(...)):
    return pull_takalot.get_all_takalot_board(user)

# use this route to get all takalot of one team. not implemented yet.
@app.post("/TeamTakalot")
def my_team_board(team: str):
    return pull_takalot.get_all_team_takalot(team)

# use this route to change the status of a takala
@app.post("/ChangeStatus")
def change_takala_status(takala_id: str, wanted_status: str, current_status: str):
    return takala_status.change_takala_status(takala_id, wanted_status, current_status)


@app.post("/TransferTakala")
def change_team(team: str):
    return "ofir code here"

# use this route to add a new message in the messages of the takala.
@app.post("/addMessage")
async def add_message(takala_id: str = Form(...), user_name: str = Form(...), msg: str = Form(...),
                      time_stamp: int = Form(...)):
    old_document = dict(pull_takalot.get_takala(takala_id))
    new_document = dict(pull_takalot.get_takala(takala_id))
    new_document["messages"].append({"user_name": user_name, "msg": msg, "time_stamp": time_stamp})
    return new_takala.update_messages(old_document, new_document)

# use this route to get a file of a takala.
@app.get("/getFile/{takala_id}")
async def get_file(takala_id):
    try:
        file_name = os.listdir(r"C:/Users/Garbi/PycharmProjects/bella-ciao-backend/{takala_id}".format(takala_id=takala_id))[0]
        file_path = r"C:/Users/Garbi/PycharmProjects/bella-ciao-backend/{takala_id}".format(takala_id=takala_id) + r"/"\
                    + file_name
        return responses.FileResponse(file_path, headers={"filename": file_name}, media_type=file_name,
                                      filename=file_name)
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)


# use to check if the user is in the db or not
@app.get("/userExists/{user_name}")
async def check_exists(user_name):
    return users.check_user_exists(user_name)

# use to create a new user in the system
@app.post("/newUser")
async def new_user(user_data: dict):
    return users.add_new_user(user_data)


@app.get("/userData/{user_name}")
async def get_user(user_name):
    user_data = users.get_user(user_name)
    if user_data == "user not exists!":
        raise HTTPException(status_code=404, detail="user not found")
    return user_data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
