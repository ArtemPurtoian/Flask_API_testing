import pytest
from http import HTTPStatus


""" POST user """

# statuses


def test_post_status_created(create_user):
    response = create_user[0]
    assert response.status_code == HTTPStatus.CREATED


def test_post_status_bad_request_missing_fields(create_user_missing_fields):
    response = create_user_missing_fields[0]
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_post_status_bad_request_already_exists(create_user_already_exists):
    response = create_user_already_exists[0]
    assert response.status_code == HTTPStatus.BAD_REQUEST


@pytest.mark.parametrize("post_body, expected_status_code",
                         [({"user_name": 1, "gender": "male", "age": 30},
                           HTTPStatus.BAD_REQUEST)])
def test_post_status_bad_request_value_is_not_valid(
        create_user_value_is_not_valid, post_body, expected_status_code):
    assert create_user_value_is_not_valid.status_code == expected_status_code


# message, errors, data types


def test_post_message_created_successfully(create_user):
    response, post_body = create_user
    assert (response.json["message"] ==
            f"User '{post_body["user_name"]}' created successfully")


def test_post_error_missing_fields(create_user_missing_fields):
    response, missing_fields = create_user_missing_fields
    assert response.json["error"] == f"Missing {missing_fields} fields"


def test_post_error_already_exists(create_user_already_exists):
    response, post_body = create_user_already_exists
    assert (response.json["error"] ==
            f"User '{post_body["user_name"]}' already exists")


@pytest.mark.parametrize("post_body, expected_error",
                         [({"user_name": 1, "gender": "male", "age": 30},
                           "'user_name' must be a string"),
                          ({"user_name": "alex", "gender": 1, "age": 30},
                           "'gender' must be a string"),
                          ({"user_name": "alex", "gender": "male", "age": "30"},
                           "'age' must be an integer")])
def test_post_error_value_is_not_valid_parametrized(
        create_user_value_is_not_valid, post_body, expected_error):
    assert (create_user_value_is_not_valid.json["error"] ==
            expected_error)
