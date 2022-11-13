import pytest
from api.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_index(client):
    assert client.get("/").status_code == 200

