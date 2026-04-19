import json
from datetime import datetime

LOG_FILE = "data/logs.jsonl"

def log_event(data: dict):
    data["timestamp"] = datetime.utcnow().isoformat()

    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")