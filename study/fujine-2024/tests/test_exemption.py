# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=17
import pytest

from introduction.exemption import calculate_exemption_amount


@pytest.mark.parametrize(
    ("income", "expected"),
    [
        # pytest.param(1_625_000, 650_000, id="162.5万円以下") はエスケープされてしまう
        (1_625_000, 550_000),
        (1_625_003, 550_001),
        (1_800_000, 620_000),
        (1_800_001, 1_340_000),
        (3_600_000, 1_880_000),
        (3_600_001, 1_160_000),
        (6_600_000, 1_760_000),
        (6_600_010, 1_760_001),
        (8_500_000, 1_950_000),
        (8_500_001, 1_950_000),
    ],
    ids=[
        "162.5万円以下",
        "162.5万円超かつ180万円以下",
        "162.5万円超かつ180万円以下（上の境界値）",
        "180万円超かつ360万円以下",
        "180万円超かつ360万円以下（上の境界値）",
        "360万円超かつ660万円以下",
        "360万円超かつ660万円以下（上の境界値）",
        "660万円超かつ850万円以下",
        "660万円超かつ850万円以下（上の境界値）",
        "850万円超",
    ],
)
def test_calculate_exemption_amount(income, expected):
    assert calculate_exemption_amount(income) == expected
