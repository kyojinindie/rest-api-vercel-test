from fastapi import FastAPI, Header
import os
from langchain.llms import OpenAI
from pydantic import BaseModel


class Request(BaseModel):
    prompt: str


app = FastAPI()

"""
A health check endpoint.

Returns:
    dict: The status of the health check.
"""
@app.get("/health")
async def health_check():
    return {"status": "ok"}

"""
An asynchronous function that handles POST requests to the "/api/v1/text-davinci-003" endpoint.

Args:
    request (Request): The incoming request object.
    OPENAI_API_KEY (str): The API key for OpenAI.

Returns:
    dict: A dictionary containing the response message.
"""
@app.post("/api/v1/text-davinci-003")
async def text_davinci_003(request: Request, OPENAI_API_KEY: str = Header(...)):
    prompt = request.prompt
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    llm = OpenAI(model_name="text-davinci-003")
    response = llm(prompt)
    return {"message": response}
