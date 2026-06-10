from http import HTTPStatus


def test_404_route_not_found(client):
    response = client.get("/api/unknown")

    assert response.status_code == HTTPStatus.NOT_FOUND

    assert response.get_json()["error"] == \
           "Route not found. Please check the URL."


def test_405_method_not_allowed(client):
    response = client.post("/api/welcome")

    assert response.status_code == HTTPStatus.METHOD_NOT_ALLOWED

    assert response.get_json()["error"] == \
           "Method not allowed."
