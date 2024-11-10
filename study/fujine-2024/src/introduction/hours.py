from datetime import datetime, time


def is_in_business() -> bool:
    """システム時刻が営業時間中であればTrue、そうでなければFalseを返す

    営業時間とは、土日を除く9〜17時

    ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=24
    """
    now = datetime.now()
    if now.weekday() in (5, 6):
        return False
    if time(9, 0, 0) <= now.time() <= time(17, 0, 0):
        return True
    return False
