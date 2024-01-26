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
def get_users_url(client):
    url = "api/users"
    response = client.get(url)
    return response


@pytest.fixture
def create_user(client):
    url = "http://localhost:5000/api/users"
    post_body = {"user_name": "alex", "gender": "male", "age": 30}

    response = client.post(url, json=post_body)
    yield response, post_body
    client.delete(url, json={"id": 1})


@pytest.fixture
def create_user_missing_fields(client):
    url = "http://localhost:5000/api/users"
    missing_fields = ["user_name", "age"]
    post_body = {"gender": "male"}

    response = client.post(url, json=post_body)
    yield response, missing_fields


@pytest.fixture
def create_user_already_exists(client):
    url = "http://localhost:5000/api/users"
    post_body = {"user_name": "alex", "gender": "male", "age": 30}

    client.post(url, json=post_body)
    response = client.post(url, json=post_body)
    yield response, post_body
    client.delete(url, json={"id": 1})


@pytest.fixture
def create_user_value_is_not_valid(client, post_body):
    url = "http://localhost:5000/api/users"
    response = client.post(url, json=post_body)
    yield response


@pytest.fixture
def update_user(client):
    url = "http://localhost:5000/api/users"
    post_body = {"user_name": "alex", "gender": "male", "age": 30}

    client.post(url, json=post_body)

    put_body = {"id": 1, "user_name": "john", "gender": "male", "age": 25}
    response = client.put(url, json=put_body)
    yield response, put_body
    client.delete(url, json={"id": 1})


@pytest.fixture
def update_user_missing_fields(client):
    url = "http://localhost:5000/api/users"
    post_body = {"user_name": "alex", "gender": "male", "age": 30}

    client.post(url, json=post_body)

    put_body = {"user_name": "john", "gender": "male", "age": 25}
    response = client.put(url, json=put_body)
    yield response
    client.delete(url, json={"id": 1})


@pytest.fixture
def update_user_already_exists(client):
    url = "http://localhost:5000/api/users"
    post_body = {"user_name": "alex", "gender": "male", "age": 30}

    client.post(url, json=post_body)

    put_body = {"id": 1, "user_name": "alex", "gender": "male", "age": 25}
    response = client.put(url, json=put_body)
    yield response
    client.delete(url, json={"id": 1})


@pytest.fixture
def update_user_value_is_not_valid(client):
    url = "http://localhost:5000/api/users"
    post_body = {"user_name": "alex", "gender": "male", "age": 30}

    client.post(url, json=post_body)

    put_body = {"id": "1", "user_name": "alex", "gender": "male", "age": 25}
    response = client.put(url, json=put_body)
    yield response
    client.delete(url, json={"id": 1})


@pytest.fixture
def delete_user(client):
    url = "http://localhost:5000/api/users"
    post_body = {"user_name": "alex", "gender": "male", "age": 30}

    client.post(url, json=post_body)

    delete_body = {"id": 1}
    response = client.delete(url, json=delete_body)
    yield response, post_body, delete_body


@pytest.fixture
def delete_user_not_found(client):
    url = "http://localhost:5000/api/users"
    post_body = {"user_name": "alex", "gender": "male", "age": 30}

    client.post(url, json=post_body)

    delete_body = {"id": 3}
    response = client.delete(url, json=delete_body)
    yield response, post_body, delete_body
    client.delete(url, json={"id": 1})


@pytest.fixture
def delete_user_missing_key(client):
    url = "http://localhost:5000/api/users"
    post_body = {"user_name": "alex", "gender": "male", "age": 30}

    client.post(url, json=post_body)

    delete_body = {"user_name": "alex"}
    response = client.delete(url, json=delete_body)
    yield response, post_body, delete_body
    client.delete(url, json={"id": 1})


@pytest.fixture
def delete_user_value_is_not_valid(client):
    url = "http://localhost:5000/api/users"
    post_body = {"user_name": "alex", "gender": "male", "age": 30}

    client.post(url, json=post_body)

    delete_body = {"id": "1"}
    response = client.delete(url, json=delete_body)
    yield response, post_body, delete_body
    client.delete(url, json={"id": 1})
