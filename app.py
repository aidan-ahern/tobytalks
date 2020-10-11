"""
DialogFlow Echo Response Fulfillment
Run ngrok:
https://ngrok.com/download
./ngrok http 8080
Setup:
pip install fastapi uvicorn
Run:
uvicorn --port 8080 app:app
"""

from typing import Any, Dict

from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

# Using PyDantic to parse/validate the request body from DF

class Intent(BaseModel):
    displayName: str

class Request(BaseModel):
    intent: Intent
    parameters: Dict[str, Any]

# See the docs for the Body syntax used here
# https://fastapi.tiangolo.com/tutorial/body-multiple-params/#embed-a-single-body-parameter

@app.post("/")
async def home(queryResult: Request = Body(..., embed=True)):
    intent = queryResult.intent.displayName
    count = len(queryResult.parameters)
    with open('through_the_looking_glass.txt', encoding='utf8') as file:
        data = file.read().replace('\n', '')
        """        
        for lines in range (10):
            data = file.readline()
        """
    text = f"I'm going to read {intent} for you: {data}"
    return {"fulfillmentText": text}