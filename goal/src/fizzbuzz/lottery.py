import random


def draw_lottery() -> str:
    number = random.randint(1, 6)
    if number == 6:
        return "超吉"
    else:
        return "凶"
