import uvicorn
import fastapi


from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"status": "Alive"}

@app.post()
def new_takala():
    return "tair do your job please"

@app.post()
def search_takala():
    return "ofir where are you?"

@app.post()
def my_board():
    return "pashoshi?"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)