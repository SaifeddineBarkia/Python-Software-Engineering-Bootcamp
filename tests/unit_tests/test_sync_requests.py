import responses

from sample_requests.sync_requests import get_and_parse_user

@responses.activate
def test_sync_requests_get_and_parse_user():
    base_url = "https://api.github.com"
    endpoint_prefix = "/user/"
    user_id = 123456789

    responses.add(
        responses.GET,
        f"{base_url}{endpoint_prefix}{user_id}",
        status=200,
        json={"AZziiz": [1,2,3]})

    responses.add(
        responses.POST,
        f"{base_url}{endpoint_prefix}{user_id}",
        status=200,
        json={"AZziiz": [1,2,3]})

    response = get_and_parse_user(base_url, endpoint_prefix, user_id)

    assert response.json() == {"AZziiz": [1,2,3]}
    assert response.status_code==200