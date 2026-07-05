import requests

from api.shemas.unknown_shema import UserSchema
import pytest

headers = {"x-api-key": "pro_7f2da8d55e3dd1a5e4e9b4db2d9d6371fad0d285ac4ded33395bfff5112d64"}

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
        response = requests.post(url, json={
            "title": "foo",
            "body": "bar",
            "userId": 1
        })
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




