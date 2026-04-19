import json

def load_flags():
    with open("config/flags.json") as f:
        return json.load(f)