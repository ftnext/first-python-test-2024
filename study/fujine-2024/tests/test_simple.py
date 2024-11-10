# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=14
import pytest

from introduction.simple import calculate_bmi


class TestCalculateBMI:
    def test_身長と体重からBMI値を計算できる(self):
        assert calculate_bmi(height_m=2, weight_kg=80) == 20.0

    def test_身長が0以下の場合_ValueErrorが送出される(self):
        with pytest.raises(ValueError) as ex:
            calculate_bmi(height_m=0, weight_kg=80)
        assert str(ex.value) == "Height and weight must be greater than 0."

    def test_体重が0以下の場合_ValueErrorが送出される(self):
        with pytest.raises(ValueError):
            calculate_bmi(height_m=2, weight_kg=0)
