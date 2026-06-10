import pytest
import app
from tests.data import VALID_USER


@pytest.fixture(autouse=True)
def reset_state():
    """
    Reset application state before each test.
    """
    app.users.clear()
    app.user_id_counter = 1

    yield

    app.users.clear()
    app.user_id_counter = 1


@pytest.fixture
def client():
    app.app.config["TESTING"] = True

    with app.app.test_client() as client:
        yield client


@pytest.fixture
def user_payload():
    return VALID_USER.copy()


@pytest.fixture
def created_user(client, user_payload):
    response = client.post(
        "/api/users",
        json=VALID_USER
    )

    return response.get_json()["user"]
