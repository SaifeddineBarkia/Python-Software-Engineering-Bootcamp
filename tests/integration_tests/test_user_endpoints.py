

def test_delete_user_sucess(testing_application, valid_user_id):
    response = testing_application.delete(f'/user/{valid_user_id}')
    assert response.status_code == 200

def test_double_delete_user_sucess(testing_application, valid_user_id):
    response = testing_application.delete(f'/user/{valid_user_id}')
    assert response.status_code == 200

    second_response = testing_application.delete(f'/user/{valid_user_id}')
    assert second_response.status_code == 404
    assert second_response.json() == "User doesn't exist"

def test_delete_user_invalid(testing_application, invalid_user_id):
    response = testing_application.delete(f'/user/{invalid_user_id}')
    assert response.status_code == 404
    assert response.json() == "User doesn't exist"


def test_put_user_success(testing_application, valid_user_id, testing_full_user_profile):
    response = testing_application.put(f'/user/{valid_user_id}', json=testing_full_user_profile.model_dump() )
    assert response.status_code == 200

def test_get_user_success(testing_application, valid_user_id):
    response = testing_application.get(f'/user/{valid_user_id}')

    assert response.status_code == 200
    assert response.json()['long_bio'] == "This longer"



def test_rate_limit_works(testing_application, testing_rate_limit, valid_user_id):
    for i in range(testing_rate_limit+33):
        response = testing_application.get(f'/user/{valid_user_id}')
        if 'X-app-rate-limit' not in response.headers:
            assert response.status_code == 429
