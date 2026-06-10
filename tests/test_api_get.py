from http import HTTPStatus


def test_get_welcome_status_ok(client):
    response = client.get("/api/welcome")

    assert response.status_code == HTTPStatus.OK


def test_get_welcome_message(client):
    response = client.get("/api/welcome")

    assert response.get_json()["message"] == "Hi, this is your API!"


def test_get_users_status_ok(client):
    response = client.get("/api/users")

    assert response.status_code == HTTPStatus.OK


def test_get_users_returns_empty_list(client):
    response = client.get("/api/users")

    assert response.get_json()["users"] == []


def test_get_users_returns_users(client, created_user):
    response = client.get("/api/users")

    users = response.get_json()["users"]

    assert len(users) == 1
    assert users[0]["user_name"] == "alex"
