import time

def model_a(input_text: str):
    time.sleep(0.1)  # fast
    return f"[FAST MODEL] {input_text}"

def model_b(input_text: str):
    time.sleep(0.3)  # slower but "better"
    return f"[SMART MODEL] {input_text.upper()}"