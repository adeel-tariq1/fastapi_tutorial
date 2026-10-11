from fastapi.testclient import TestClient
from apitest import app

client = TestClient(app)
#testing home route
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"APi is connected"}

#testing add route
def test_add():
    response = client.get("/add?a=13&b=5")
    assert response.status_code == 200
    assert response.json() =={"result":18}