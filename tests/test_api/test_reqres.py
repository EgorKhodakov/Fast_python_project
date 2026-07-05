import requests

from api.shemas.unknown_shema import ColorShema

class TestReqres:

    def test_year_more_than_200(self):
        url = "https://app.reqres.in/playground?path=/api/unknown&method=GET"
        response = requests.get(url)
        data = response.json()

        colors = [ColorShema(**item) for item in data["data"]]

        assert response.status_code == 200
        assert all(color.year >= 2000 for color in colors)
        assert all(color.name for color in colors)

