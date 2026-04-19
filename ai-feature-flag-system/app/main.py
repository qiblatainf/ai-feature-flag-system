from fastapi import FastAPI
from pydantic import BaseModel
import time

from app.router import route_request
from app.logger import log_event

app = FastAPI()

class Request(BaseModel):
    input: str
    user_id: str = "anon"

@app.post("/infer")
def infer(req: Request):
    start = time.time()

    variant, output = route_request(req.input)

    latency = int((time.time() - start) * 1000)

    log_event({
        "user_id": req.user_id,
        "variant": variant,
        "input": req.input,
        "output": output,
        "latency_ms": latency
    })

    return {
        "variant": variant,
        "output": output,
        "latency_ms": latency
    }