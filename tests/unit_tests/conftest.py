import pytest
from app.services.user import UserService

@pytest.fixture
def user_service(profile_infos, users_content):
    user_service = UserService(profile_infos, users_content)
    return user_service