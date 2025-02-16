# tests/test_app.py
import pytest
from app.app import app

@pytest.fixture
def client():
    return app.test_client()

def test_hello_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello DevOps!" in response.data
