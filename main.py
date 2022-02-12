from fastapi import FastAPI
import telegram_send

from pydantic import BaseModel

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    firstname: str
    lastname : str
    email : str
    phone : str
    message : str

@app.get("/")
def index():
    return "This is working"

@app.get("/test")
def test():
    telegram_send.send(messages=["Test success"])
    return "success"

@app.post("/message")
def message(message: Message):
    # telegram_send.send(messages=[message])
    print(message)
    return message


    