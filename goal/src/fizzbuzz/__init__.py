import argparse

from fizzbuzz.core import fizzbuzz


def print_fizzbuzz(upper_limit: int) -> None:
    for number in range(1, upper_limit + 1):
        print(fizzbuzz(number))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--number", "-n", type=int, default=30)
    args = parser.parse_args()

    print_fizzbuzz(args.number)
