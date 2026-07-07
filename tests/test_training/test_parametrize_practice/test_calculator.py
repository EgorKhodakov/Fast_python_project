import pytest

from tests.test_training.test_parametrize_practice.calculator import Calculator

"""Тест с параметризацией трех аргументов"""


@pytest.mark.parametrize("a,b,expected", [(10, 2, 5), (9, 3, 3), (7, 0, None)])
def test_divide(calk: Calculator, a: float, b: float, expected: float) -> None:
    assert calk.divide(a, b) == expected


"""Тесты с маркировкой smoke"""


@pytest.mark.smoke
def test_add_positive(calk: Calculator) -> None:
    assert calk.add(1, 2) == 3


@pytest.mark.smoke
def test_add_negative(calk: Calculator) -> None:
    assert calk.add(-1, 2) == 1


@pytest.mark.smoke
def test_calk_zero(calk: Calculator) -> None:
    assert calk.add(0, 0) == 0


"""Тесты с маркировкой skip и Xfail"""


@pytest.mark.skip
def test_power_with_float_exponent(calk: Calculator) -> None:
    assert calk.power(4, 0, 5) == 2


@pytest.mark.xfail
def test_divide_by_zero_xfail(calk: Calculator) -> None:
    assert calk.divide(6, 0) is None


"""Тест с маркировкой в параметризации"""


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (pytest.param(2, 6, 12, marks=pytest.mark.smoke)),
        (9, 3, 27),
        pytest.param(7, 0, None, marks=pytest.mark.xfail),
        (2, 7, 14),
    ],
)
def test_multiply_with_markers(calk: Calculator, a, b, expected: float) -> None:
    assert calk.multiply(a, b) == expected
