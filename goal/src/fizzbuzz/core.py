def fizzbuzz(number: int) -> str:
    match number % 3, number % 5:
        case 0, 0:
            return "FizzBuzz"
        case 0, _:
            return "Fizz"
        case _, 0:
            return "Buzz"
        case _, _:
            return str(number)
