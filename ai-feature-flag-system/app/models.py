def model_a(input_text: str):
    return f"[A] Simple response: {input_text[:20]}"

def model_b(input_text: str):
    return f"[B] Advanced response: {input_text.upper()}"