# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=31
import pytest

from introduction.api import get_address


class TestGetAddress:
    @pytest.mark.parametrize(
        ("zipcode", "expected"),
        [
            ("0000000", None),
            ("1111111", "都道府県 市区町村 番地"),
        ],
        ids=["テスト用郵便番号ではNoneを返す", "テスト用郵便番号以外では住所を返す"],
    )
    def test_住所が取得できる(self, mock_response, zipcode, expected):
        assert get_address(zipcode) == expected

    @pytest.mark.parametrize(
        "zipcode",
        ["1", "12345678", "dummy"],
        ids=["桁数が少ない", "桁数が多い", "数字以外"],
    )
    def test_郵便番号が不正な場合_ValueErrorが送出される(self, mock_response, zipcode):
        with pytest.raises(ValueError) as ex:
            get_address(zipcode)
        assert str(ex.value) == "郵便番号の桁数や値が不正です。"
