import pytest
from endpoints import UserEndpoint, PostEndpoint, CommentEndpoint
from config_data import token
from faker import Faker


# parameterisera
# data driven tests
# edge cases

@pytest.mark.parametrize("input_data, expected_output", [
    ({"param": "value"}, {"expected_key": "expected_value"}),
    # Add more test
])
def test_api_functionality(api_client, input_data, expected_output):
    response = api_client.make_request(data=input_data)
    assert response.json() == expected_output



# @pytest.fixture
# def mock_requests():
#     with requests_mock.Mocker() as m:
#         # Mock responses for specific endpoints
#         m.get('https://gorest.co.in/public-api/users/123', json={'data': {'id': 123, 'name': 'John'}})
#         # Add more mocks for other endpoints
#
#         yield m



@pytest.fixture
def user_endpoint(auth):
    base_url = 'https://gorest.co.in'
    return UserEndpoint(base_url, auth)


@pytest.fixture
def posts_endpoint(auth):
    base_url = 'https://gorest.co.in'
    return PostEndpoint(base_url, auth)


@pytest.fixture
def comment_endpoint(auth):
    base_url = 'https://gorest.co.in'
    return CommentEndpoint(base_url, auth)


@pytest.fixture
def api_auth():
    with open(token, 'r') as file:
        auth_token = file.read().strip()

    return auth_token


@pytest.fixture
def auth(api_auth):
    header = {
        "Authorization": f"Bearer {api_auth}"
    }
    return header


@pytest.fixture
def post_data():
    post_text = {'title': "Detta är ett test", 'body': 'Detta är ett test'}
    return post_text


user_data = {
    "name": "t ton",
    "email": "telt@tesampe.com",
    "gender": "male",
    "status": "active"
}

fake = Faker()
random_user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "gender": fake.random_element(["male", "female"]),
    "status": "active"
}


def test_get_user(user_endpoint):
    user_id = 4377183
    response = user_endpoint.get_user(user_id)

    assert response.status_code == 200, f"Expected {response.status_code} to be equal to {200}, but they are not."
    json_data = response.json()

    assert json_data['id'] == user_id
    print(json_data)


def test_get_all_users_ids(user_endpoint):
    response = user_endpoint.get_all_users()
    assert response.status_code == 200
    json_data_list = response.json()

    for user in json_data_list:
        assert 'id' in user, "'id' key not in user data"
        user_id = user['id']
        print(f"User ID: {user_id}")


def test_create_user(user_endpoint):
    response = user_endpoint.create_user(random_user_data)
    assert response.status_code == 201


def test_update_user(user_endpoint):
    user_id = 4377183
    user_update_data = {'name': 'herr test', 'email': 'test-email@test.test'}
    response = user_endpoint.update_user(user_id, user_update_data)
    assert response.status_code == 200


def test_create_and_delete_user(user_endpoint):
    create_response = user_endpoint.create_user(random_user_data)
    assert create_response.status_code == 201

    user_info = create_response.json()
    user_id = user_info['id']
    print(user_id)

    # TODO hur verifierar jag att delete funkar med assert?
    delete_response = user_endpoint.delete_user(user_id)
    print(delete_response.status_code)
    # assert delete_response.status_code == 202
    # print(delete_response.status_code)

    # if delete_response.status_code == 404:
    #     print("User already deleted")


def test_get_post(posts_endpoint):
    user_id = 4400612
    response = posts_endpoint.get_post(user_id)
    assert response.status_code == 200
    json_data_list = response.json()

    for k in json_data_list:
        print(k)


def test_create_post(posts_endpoint, post_data):
    user_id = 4400612
    response = posts_endpoint.create_post(user_id, post_data)
    json_data_list = response.json()
    assert response.status_code == 201
    # TODO how to print values?
    for k in json_data_list:
        print(k)


def test_get_comment(comment_endpoint):
    post_id = 60838
    response = comment_endpoint.get_comment(post_id)
    assert response.status_code == 200
    json_data_list = response.json()

    for k in json_data_list:
        print(k)


def test_create_comment(comment_endpoint):
    user_id = 49976
    comment_data = {'body': ' detta är ett test'}
    response = comment_endpoint.post_comment(user_id, comment_data)