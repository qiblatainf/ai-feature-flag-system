# fast api app
from fastapi import FastAPI
from pydantic import BaseModel
import time

from app.router import route_request
from app.models import model_a, model_b
from app.logger import log_event

app = FastAPI()

class Request(BaseModel):
    user_id: str
    input: str

@app.post("/infer")
def infer(req: Request):
    start = time.time()

    model_name = route_request(req.user_id)

    if model_name == "model_a":
        output = model_a(req.input)
    else:
        output = model_b(req.input)

    latency = int((time.time() - start) * 1000)

    log_event({
        "user_id": req.user_id,
        "model": model_name,
        "latency_ms": latency
    })

    return {
        "response": output,
        "model_used": model_name,
        "latency_ms": latency
    }