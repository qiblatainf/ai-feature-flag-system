# Logger (MLOps signal)
import json
from datetime import datetime

def log_event(data):
    data["timestamp"] = datetime.utcnow().isoformat()

    with open("data/logs.jsonl", "a") as f:
        f.write(json.dumps(data) + "\n")