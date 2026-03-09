from fastapi import FastAPI
from pydantic import BaseModel
from agent import troubleshoot

app = FastAPI()

class LogInput(BaseModel):
    log: str


@app.post("/analyze")
def analyze_log(input: LogInput):

    result = troubleshoot(input.log)

    return {"analysis": result}