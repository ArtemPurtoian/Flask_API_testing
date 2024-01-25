import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def get_welcome_url(client):
    url = "api/welcome"
    response = client.get(url)
    return response


@pytest.fixture
def create_user(client, post_body):
    url = "api/users"
    response = client.post(url, json=post_body)
    return response
