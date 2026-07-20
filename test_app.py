from fastapi.testclient import TestClient

from app import app, somma


client = TestClient(app)


def test_somma():
    assert somma(5, 3) == 8
    assert somma(-2, 2) == 0


def test_stato():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}