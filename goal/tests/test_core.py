from fizzbuzz.core import fizzbuzz


def test_3の倍数のときはFizzを返す():
    assert fizzbuzz(3) == "Fizz"


def test_5の倍数のときはBuzzを返す():
    assert fizzbuzz(5) == "Buzz"


def test_15の倍数のときはFizzBuzzを返す():
    assert fizzbuzz(15) == "FizzBuzz"


def test_3の倍数でも5の倍数でもないときは数字の文字列を返す():
    assert fizzbuzz(1) == "1"
