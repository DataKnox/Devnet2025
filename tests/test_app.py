from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Simple API"}

def test_create_item():
    test_item = {
        "name": "Test Item",
        "description": "A test item",
        "price": 10.99,
        "tax": 1.99
    }
    response = client.post("/items/", json=test_item)
    assert response.status_code == 200
    data = response.json()
    assert data["item"]["name"] == test_item["name"]
    assert data["item"]["price"] == test_item["price"]
    assert data["total_price"] == test_item["price"] + test_item["tax"]

def test_create_item_without_tax():
    test_item = {
        "name": "Test Item",
        "description": "A test item",
        "price": 10.99
    }
    response = client.post("/items/", json=test_item)
    assert response.status_code == 200
    data = response.json()
    assert data["item"]["name"] == test_item["name"]
    assert data["item"]["price"] == test_item["price"]
    assert data["total_price"] == test_item["price"] 