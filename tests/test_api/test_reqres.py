import pytest
import requests

from api.shemas.unknown_shema import UserSchema


@pytest.mark.api
class TestReqres:

    def test_users_have_name(self):
        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)
        data = response.json()

        users = [UserSchema(**user) for user in data]

        assert response.status_code == 200
        assert all(user.name for user in users)
        assert all(user.id >= 1 for user in users)

    def test_create_post(self):
        url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.post(url, json={"title": "foo",
                                            "body": "bar",
                                            "userId": 1}
                                 )
        data = response.json()

        assert response.status_code == 201
        assert "id" in data
        assert data["id"] == 101

    def test_list_users(self):
        url = "https://jsonplaceholder.typicode.com/users"
        response = requests.get(url)
        data = response.json()

        assert response.status_code == 200
        assert len(data) == 10
