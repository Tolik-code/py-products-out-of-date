import unittest.mock
from unittest.mock import MagicMock

import pytest

from app.main import outdated_products


@pytest.fixture()
def fixture_date_time_now() -> MagicMock:
    with unittest.mock.patch("datetime.date") as mock_function:
        yield mock_function


@pytest.fixture()
def fixture_set_up() -> list:
    return [
        {
            "name": "salmon",
            "expiration_date": 1,
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": 2,
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": 3,
            "price": 160
        }
    ]


@pytest.mark.parametrize(
    "expected,time",
    [
        pytest.param(
            [
                "salmon",
            ], 2, id="return only outdated products names"
        ),
        pytest.param(
            [], 0, id="return empty list if there is no outdated"
        ),
        pytest.param(
            [
                "salmon",
                "chicken",
                "duck"
            ], 4, id="return all names if there is all outdated"
        ),
    ]
)
def test_outdated_products(
    expected: list,
    time: int,
    fixture_date_time_now: MagicMock,
    fixture_set_up: list
) -> None:
    fixture_date_time_now.today.return_value = time
    products = fixture_set_up

    assert outdated_products(products) == expected
