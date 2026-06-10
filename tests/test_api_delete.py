from http import HTTPStatus


def test_delete_status_ok(client, created_user):
    response = client.delete("/api/users/1")

    assert response.status_code == HTTPStatus.OK


def test_delete_message_successfully(client, created_user):
    response = client.delete("/api/users/1")

    assert response.get_json()["message"] == \
           "User 'alex' deleted successfully."


def test_delete_user_not_found(client):
    response = client.delete("/api/users/999")

    assert response.status_code == HTTPStatus.NOT_FOUND


def test_delete_removes_user(client, created_user):
    client.delete("/api/users/1")

    response = client.get("/api/users")

    assert response.get_json()["users"] == []
