import requests


def test_get_200():
    response = requests.get("https://jsonplaceholder.typicode.com/users/2")
    data = response.json()
    assert response.status_code == 200
    assert data["name"] == "Ervin Howell"


def test_post_200():
    test_data = {
        "name": "Egor",
        "email": "khodakov@mail.com",
        "password": "asdgfgf##gfs",
    }

    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts", json=test_data
    )
    data = response.json()

    assert response.status_code == 201
    assert "name" in data
    assert data["email"] == "khodakov@mail.com"
