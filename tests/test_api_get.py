from http import HTTPStatus


""" GET welcome """


def test_get_welcome_status_ok(get_welcome_url):
    assert get_welcome_url.status_code == HTTPStatus.OK


def test_get_welcome_message(get_welcome_url):
    assert get_welcome_url.json["message"] == "Hi, this is your API!"


""" GET users """

# status


def test_get_users_status_ok(get_users_url):
    assert get_users_url.status_code == HTTPStatus.OK

# users present in response, content-type


def test_get_users_in_response(get_users_url):
    assert "users" in get_users_url.json
