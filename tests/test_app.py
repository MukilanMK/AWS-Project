from app import create_app


def test_root():
    app = create_app()
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Latest Posts" in resp.data
