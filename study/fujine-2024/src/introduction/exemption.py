def calculate_exemption_amount(income: int) -> int:
    """所得額(income)から給与所得控除額を計算する

    ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=16
    """
    if income < 0:
        raise ValueError("Income must be a positive integer.")
    if income <= 1_625_000:
        return 550_000
    if 1_625_000 < income <= 1_800_000:
        return int(income * 0.4) - 100_000
    if 1_800_000 < income <= 3_600_000:
        return int(income * 0.3) + 800_000
    if 3_600_000 < income <= 6_600_000:
        return int(income * 0.2) + 440_000
    if 6_600_000 < income <= 8_500_000:
        return int(income * 0.1) + 1_100_000
    return 1_950_000
