import pytest


@pytest.fixture(scope="session")
def valid_user_id() -> int:
    return 0

@pytest.fixture(scope="session")
def invalid_user_id() -> int:
    return 1

@pytest.fixture(scope="session")
def profile_infos():
    val =  {
        0:{
            "short_description":"This is short",
            "long_bio": "This longer"
        }
    }
    return val

@pytest.fixture(scope="session")
def users_content():
    val = {
        0: {
            "name": "A",
            "liked_posts": [1,2,3],
        }
    }
    return val