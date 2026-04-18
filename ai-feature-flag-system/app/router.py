import hashlib
from app.config import load_config

def route_request(user_id: str):
    config = load_config()
    rollout = config["rollout_percentage"]

    hash_val = int(hashlib.md5(user_id.encode()).hexdigest(), 16)
    bucket = hash_val % 100

    if bucket < rollout:
        return "model_b"
    return "model_a"