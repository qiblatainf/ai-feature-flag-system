import json

def load_config():
    with open("config/flags.json") as f:
        return json.load(f)