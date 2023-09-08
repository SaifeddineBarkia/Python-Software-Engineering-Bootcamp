from fastapi.testclient import TestClient
from app.main import create_application
from app.schemas.user import    FullUserProfile
import pytest


@pytest.fixture(scope="function")
def testing_application() -> TestClient:
    app = create_application()
    testing_app = TestClient(app)
    return testing_app

@pytest.fixture(scope="function")
def testing_full_user_profile(users_content, profile_infos) -> FullUserProfile:

    full_user_profile = {
            **users_content[0],
            **profile_infos[0]
        }

    full_user_profile = FullUserProfile(**full_user_profile)
    return full_user_profile

@pytest.fixture
def testing_rate_limit()-> int:
    return 500
