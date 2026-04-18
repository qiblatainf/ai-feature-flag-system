# tests/test_router.py
from app.router import route_request

def test_routing():
    result = route_request("user_123")
    assert result in ["model_a", "model_b"]