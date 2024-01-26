from http import HTTPStatus


""" DELETE user """

# status


def test_delete_status_ok(delete_user):
    response = delete_user[0]
    assert response.status_code == HTTPStatus.OK


# messages, errors, data types


def test_delete_message_successfully(delete_user):
    response, post_body, delete_body = delete_user
    assert (response.json["message"] ==
            f"User '{delete_body["id"]}' ('{post_body["user_name"]}') "
            f"deleted successfully")


def test_delete_error_not_found(delete_user_not_found):
    response = delete_user_not_found[0]
    assert response.json["error"] == "User not found"


def test_delete_error_missing_key(delete_user_missing_key):
    response = delete_user_missing_key[0]
    assert response.json["error"] == "'id' is required in the request body"


def test_delete_error_value_is_not_valid(delete_user_value_is_not_valid):
    response = delete_user_value_is_not_valid[0]
    assert response.json["error"] == "'id' must be an integer"
