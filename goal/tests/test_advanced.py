import random
from unittest.mock import patch

import pytest

from fizzbuzz import print_fizzbuzz
from fizzbuzz.core import fizzbuzz
from fizzbuzz.lottery import draw_lottery


@pytest.mark.parametrize("number", [3, 6])
def test_3の倍数のときはFizzを返す(number):
    assert fizzbuzz(number) == "Fizz"


def test_15までのfizzbuzz(capsys):
    print_fizzbuzz(15)

    expected = """\
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
"""
    assert capsys.readouterr().out == expected


class Test_モックの例:
    def test_6の目が出たら超吉と返す(self, monkeypatch):
        randint_call_count = 0

        def randint_mock(a, b):
            assert (a, b) == (1, 6)
            nonlocal randint_call_count
            randint_call_count += 1
            return 6

        monkeypatch.setattr(random, "randint", randint_mock)

        assert draw_lottery() == "超吉"
        assert randint_call_count == 1

    @patch("random.randint", return_value=5)
    def test_6以外の目が出たら凶と返す(self, mock_randint):
        assert draw_lottery() == "凶"
        mock_randint.assert_called_once_with(1, 6)
