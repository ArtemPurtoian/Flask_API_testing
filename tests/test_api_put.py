from http import HTTPStatus

from tests.data import (
    UPDATED_USER,
    VALID_USER,
    SECOND_USER,
    MISSING_AGE
)


def test_put_status_ok(client, created_user):
    response = client.put(
        "/api/users/1",
        json=UPDATED_USER
    )

    assert response.status_code == HTTPStatus.OK


def test_put_updates_user(client, created_user):
    response = client.put(
        "/api/users/1",
        json=UPDATED_USER
    )

    user = response.get_json()["user"]

    assert user["user_name"] == "john"
    assert user["age"] == 25


def test_put_user_not_found(client):
    response = client.put(
        "/api/users/999",
        json=UPDATED_USER
    )

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_put_missing_fields(client, created_user):
    response = client.put(
        "/api/users/1",
        json=MISSING_AGE
    )

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_put_duplicate_username(client):
    client.post("/api/users", json=VALID_USER)
    client.post("/api/users", json=SECOND_USER)

    response = client.put(
        "/api/users/2",
        json={
            "user_name": "alex",
            "gender": "male",
            "age": 20
        }
    )

    assert response.status_code == HTTPStatus.CONFLICT


def test_put_invalid_json(client):
    response = client.put(
        "/api/users/1",
        data='{"user_name":"john",}',
        content_type="application/json"
    )

    assert response.status_code == HTTPStatus.BAD_REQUEST
