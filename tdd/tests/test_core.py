from fizzbuzz.core import fizzbuzz


def test_1を渡すと文字列1を返す():
    assert fizzbuzz(1) == "1"


def test_2を渡すと文字列2を返す():
    assert fizzbuzz(2) == "2"


def test_3を渡すと文字列Fizzを返す():
    assert fizzbuzz(3) == "Fizz"


def test_5を渡すと文字列Buzzを返す():
    assert fizzbuzz(5) == "Buzz"


def test_15を渡すと文字列FizzBuzzを返す():
    assert fizzbuzz(15) == "FizzBuzz"
