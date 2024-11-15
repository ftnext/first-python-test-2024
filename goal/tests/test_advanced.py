import pytest

from fizzbuzz.core import fizzbuzz


@pytest.mark.parametrize("number", [3, 6])
def test_3の倍数のときはFizzを返す(number):
    assert fizzbuzz(number) == "Fizz"
