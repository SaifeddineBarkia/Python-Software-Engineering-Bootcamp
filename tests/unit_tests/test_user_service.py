import pytest

@pytest.mark.asyncio # mark the stest to be asynchrois
async def test_delete_user_works_properly(user_service, valid_user_id):
    await user_service.delete_user(valid_user_id)
    assert valid_user_id not in user_service.users_content
    assert valid_user_id not in user_service.profile_infos