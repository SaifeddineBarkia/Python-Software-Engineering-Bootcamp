from aioresponses import aioresponses
from sample_requests.async_requests import sample_request_async
import pytest

@pytest.mark.asyncio
async def test_async_requests_get_and_parse_user():
    base_url = "https://api.github.com"
    endpoint_prefix = "/user/"
    user_id = 123456789

    with aioresponses() as m:
        m.post(f"{base_url}{endpoint_prefix}{user_id}",
        status=200,
        payload={"AZziiz": [1,2,3]})

        status, json  = await sample_request_async(base_url, endpoint_prefix, user_id)

    assert json == {"AZziiz": [1,2,3]}
    assert status==200