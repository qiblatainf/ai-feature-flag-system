import random
from app.models import model_a, model_b
from app.config import load_flags

def select_variant():
    config = load_flags()
    variants = config["variants"]

    r = random.random()
    cumulative = 0

    for v in variants:
        cumulative += v["weight"]
        if r < cumulative:
            return v["name"]

def route_request(input_text: str, context: dict = None):
    # Example: long input → better model
    if len(input_text) > 100:
        return "model_b", model_b(input_text)

    variant = select_variant()

    if variant == "model_a":
        return variant, model_a(input_text)

    return variant, model_b(input_text)
