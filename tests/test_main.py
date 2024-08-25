from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/api/v1/items/", json={"name": "Item1", "description": "Description", "price": 10.5, "in_stock": True})
    assert response.status_code == 200
    assert response.json()["name"] == "Item1"

def test_read_item():
    response = client.get("/api/v1/items/valid_id")
    assert response.status_code == 200
    assert response.json()["name"] == "Item1"

def test_update_item():
    response = client.put("/api/v1/items/valid_id", json={"price": 12.5})
    assert response.status_code == 200
    assert response.json()["price"] == 12.5

def test_delete_item():
    response = client.delete("/api/v1/items/valid_id")
    assert response.status_code == 200
    assert response.json()["name"] == "Item1"
