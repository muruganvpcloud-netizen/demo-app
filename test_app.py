from app import app
 
 
def test_health():
    response = app.test_client().get("/healthz")
    assert response.status_code == 200
    assert response.data == b"ok"
 
 
def test_home_page():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert b"Hello from GKE" in response.data
