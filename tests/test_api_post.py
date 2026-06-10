from http import HTTPStatus

from tests.data import (
    VALID_USER,
    INVALID_USERNAME_TYPE,
    INVALID_GENDER_TYPE,
    INVALID_AGE_TYPE,
    MISSING_USERNAME,
    MISSING_GENDER,
    MISSING_AGE,
    EMPTY_PAYLOAD
)


def test_post_status_created(client):
    response = client.post(
        "/api/users",
        json=VALID_USER
    )

    assert response.status_code == HTTPStatus.CREATED


def test_post_message_created_successfully(client):
    response = client.post(
        "/api/users",
        json=VALID_USER
    )

    assert response.get_json()["message"] == \
           "User 'alex' created successfully."


def test_post_returns_created_user(client):
    response = client.post(
        "/api/users",
        json=VALID_USER
    )

    user = response.get_json()["user"]

    assert user["id"] == 1
    assert user["user_name"] == "alex"
    assert user["gender"] == "male"
    assert user["age"] == 30


def test_post_duplicate_username(client):
    client.post("/api/users", json=VALID_USER)

    response = client.post(
        "/api/users",
        json=VALID_USER
    )

    assert response.status_code == HTTPStatus.CONFLICT
    assert response.get_json()["error"] == \
           "User 'alex' already exists."


def test_post_missing_username(client):
    response = client.post(
        "/api/users",
        json=MISSING_USERNAME
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_post_missing_gender(client):
    response = client.post(
        "/api/users",
        json=MISSING_GENDER
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_post_missing_age(client):
    response = client.post(
        "/api/users",
        json=MISSING_AGE
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_post_empty_payload(client):
    response = client.post(
        "/api/users",
        json=EMPTY_PAYLOAD
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_post_invalid_username_type(client):
    response = client.post(
        "/api/users",
        json=INVALID_USERNAME_TYPE
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_post_invalid_gender_type(client):
    response = client.post(
        "/api/users",
        json=INVALID_GENDER_TYPE
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_post_invalid_age_type(client):
    response = client.post(
        "/api/users",
        json=INVALID_AGE_TYPE
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_post_invalid_json(client):
    response = client.post(
        "/api/users",
        data='{"user_name":"alex",}',
        content_type="application/json"
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response.get_json()["error"] == "Invalid JSON"
