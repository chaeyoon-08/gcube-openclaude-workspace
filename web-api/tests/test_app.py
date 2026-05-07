import pytest
import src.app
from src.app import app


@pytest.fixture
def client():
    src.app.todos.clear()
    src.app.next_id = 1
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_get_todos_empty(client):
    resp = client.get("/todos")
    assert resp.status_code == 200
    assert resp.get_json() == []


def test_create_todo(client):
    resp = client.post("/todos", json={"title": "Buy milk"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data["id"] == 1
    assert data["title"] == "Buy milk"
    assert data["done"] is False


def test_create_todo_missing_title(client):
    resp = client.post("/todos", json={})
    assert resp.status_code == 400


def test_get_todos_after_create(client):
    client.post("/todos", json={"title": "Task A"})
    client.post("/todos", json={"title": "Task B"})
    resp = client.get("/todos")
    assert resp.status_code == 200
    data = resp.get_json()
    assert len(data) == 2
    assert data[0]["title"] == "Task A"
    assert data[1]["title"] == "Task B"
