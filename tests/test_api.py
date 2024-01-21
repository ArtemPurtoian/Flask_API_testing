from http import HTTPStatus
from app import users


def test_get_status_code(client):
    url = "api/welcome"

    response = client.get(url)
    assert response.status_code == HTTPStatus.OK


def test_get_content_type(client):
    url = "api/welcome"

    response = client.get(url)
    assert response.headers["Content-Type"] == "application/json"


def test_get_message(client):
    url = "api/welcome"

    response = client.get(url)
    assert "message" in response.json


def test_get_message_data(client):
    url = "api/welcome"

    response = client.get(url)
    data = response.json
    assert data["message"] == "Hi, this is your API!"


def test_post_new_user_status_created(client):
    url = "api/users"
    user_data = {
        "user_name": 'alex',
        "gender": 'male',
        "age": 30
    }

    response = client.post(url, json=user_data)
    assert response.status_code == HTTPStatus.CREATED


def test_post_new_user_in_message(client):
    url = "api/users"
    user_data = {
        "user_name": 'bob',
        "gender": 'male',
        "age": 30
    }

    response = client.post(url, json=user_data)
    assert user_data['user_name'] in response.json['message']


def test_post_is_json(client):
    url = "api/users"
    user_data = {
        "user_name": 'steven',
        "gender": 'male',
        "age": 30
    }

    response = client.post(url, json=user_data)
    assert response.headers["Content-Type"] == "application/json"


def test_post_missing_fields_status_bad_request(client):
    url = "api/users"
    user_data = {
        "gender": "male"
    }

    response = client.post(url, json=user_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_post_missing_fields_error(client):
    url = "api/users"
    user_data = {
        "gender": "male"
    }

    response = client.post(url, json=user_data)
    assert 'error' in response.json


def test_post_missing_fields_message(client):
    url = "api/users"
    user_data = {
        "gender": "male"
    }

    response = client.post(url, json=user_data)
    assert 'Missing required fields' in response.json['error']


def test_post_duplicate_names_bad_request(client):
    url = "api/users"
    user_data = {
        "user_name": "john",
        "gender": "male",
        "age": 25
    }

    users.append(
        {"id": 1, "user_name": "john", "gender": "male", "age": 30}
    )

    response = client.post(url, json=user_data)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_post_duplicate_names_error(client):
    url = "api/users"
    user_data = {
        "user_name": "john_doe",
        "gender": "male",
        "age": 25
    }

    users.append(
        {"id": 1, "user_name": "john_doe", "gender": "female", "age": 30}
    )

    response = client.post(url, json=user_data)
    assert 'error' in response.json


def test_post_duplicate_names_message(client):
    url = "api/users"
    user_data = {
        "user_name": "john_doe",
        "gender": "male",
        "age": 25
    }

    users.append(
        {"id": 1, "user_name": "john_doe", "gender": "female", "age": 30}
    )

    response = client.post(url, json=user_data)
    assert (f"User '{user_data["user_name"]}' already exists"
            in response.json['error'])
