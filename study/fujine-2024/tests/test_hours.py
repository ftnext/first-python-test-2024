# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=25
import pytest
from freezegun import freeze_time

from introduction.hours import is_in_business


class TestIsInBusiness:
    @pytest.mark.parametrize(
        "now",
        ["2024-09-27 09:00:00", "2024-09-27 17:00:00"],
        ids=["金曜日9時", "金曜日17時"],
    )
    def test_平日の9時から17時は営業時間(self, now):
        with freeze_time(now):
            assert is_in_business()

    @pytest.mark.parametrize(
        "now",
        ["2024-09-27 08:59:59", "2024-09-27 17:00:01"],
        ids=["金曜日9時前", "金曜日17時過ぎ"],
    )
    def test_平日の9時より前_17時より後は営業時間ではない(self, now):
        with freeze_time(now):
            assert not is_in_business()

    @pytest.mark.parametrize(
        "now",
        ["2024-09-28 12:00:00", "2024-09-29 12:00:00"],
        ids=["土曜日", "日曜日"],
    )
    def test_土日は営業時間ではない(self, now):
        with freeze_time(now):
            assert not is_in_business()
