import pytest
from project import compound_interest, conversion, get_date


def test_compound_interest():
    assert compound_interest(1, 2, 3) == 1.06
    assert compound_interest(4.77, 1.87, 8.01) == 5.53


def test_conversion():
    assert conversion() == 0.92


def test_get_date():
    assert get_date(1722024001) == "26-07-2024 22:00:01"
