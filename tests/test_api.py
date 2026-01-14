from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "TextAnalyzer AI"}
    
def test_analyze_positive():
    response = client.post("/analyze", params={"text": "This is a great day"})
    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"
