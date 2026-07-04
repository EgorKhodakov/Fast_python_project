from tests.cat_function import get_fact_of_cat
import responses


def test_get_fact_of_cat_mock(mocker):
    mock_get = mocker.patch("tests.cat_function.requests.get")
    mock_get.return_value.json.return_value = {
        "fact": "Рыжие коты невероятно тупые"
    }
    mock_get.return_value.status_code = 403
    result = get_fact_of_cat()
    data = get_fact_of_cat().json()

    assert data["fact"] == "Рыжие коты невероятно тупые"
    assert result.status_code == 403


@responses.activate
def test_with_responses():
    responses.add(
        responses.GET,
        "https://catfact.ninja/fact",
        json={"fact": "Рыжие коты невероятно тупые"},
        status=200
    )

    result = get_fact_of_cat()
    assert result.status_code == 200
    assert result.json()["fact"] == "Рыжие коты невероятно тупые"