from http import HTTPStatus


""" PUT user """

# status


def test_put_status_ok(update_user):
    response = update_user[0]
    assert response.status_code == HTTPStatus.OK


def test_put_status_bad_request_missing_fields(update_user_missing_fields):
    assert update_user_missing_fields.status_code == HTTPStatus.BAD_REQUEST


def test_put_status_bad_request_already_exists(update_user_already_exists):
    assert update_user_already_exists.status_code == HTTPStatus.BAD_REQUEST


def test_put_status_bad_request_value_is_not_valid(update_user_value_is_not_valid):
    assert update_user_value_is_not_valid.status_code == HTTPStatus.BAD_REQUEST


# messages, errors, data types


def test_put_message_changed_successfully(update_user):
    response, put_body = update_user
    assert (response.json["message"] ==
            f"Username with ID '{put_body['id']}' changed "
            f"to '{put_body['user_name']}'")
