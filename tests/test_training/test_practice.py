import pytest


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (pytest.param(1, 2, 6, marks=pytest.mark.xfail)),
        (3, 3, 6),
        (3, 4, 7),
        pytest.param(4, 5, 8, marks=pytest.mark.xfail),
        (2, 2, 4),
    ],
)
def test_assertion(a, b, expected):
    assert a + b == expected


@pytest.fixture(scope="function")
def sample_product():
    return {
        "name": "Ноутбук",
        "price": 1000,
        "discount": 20,
    }


def apply_discount(price: float, discount_percent: float) -> float:
    """Возвращает цену с учётом скидки.

    Примеры:
    - price=100, discount=10 → 90.0
    - price=200, discount=25 → 150.0
    - price=50, discount=100 → 0.0 (бесплатно)
    """
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Скидка должна быть от 0 до 100")
    return price * (100 - discount_percent) / 100


def test_discount_with_fixture(sample_product):
    result = apply_discount(sample_product["price"], sample_product["discount"])
    assert result == 800


@pytest.mark.parametrize(
    "price,discount,expected",
    [(100, 10, 90), (200, 25, 150), (500, 50, 250), (1000, 100, 0)],
)
def test_discount_parametrized(price, discount, expected):
    assert apply_discount(price, discount) == expected


@pytest.mark.parametrize(
    "new_discount, expected",
    [
        (10, 900),
        (20, 800),
        (30, 700),
        (50, 500),
        (100, 0),
    ],
)
def test_discount_fixture_parametrized(sample_product, new_discount, expected):
    assert apply_discount(sample_product["price"], new_discount) == expected
