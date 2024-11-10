# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=38
from datetime import date

from introduction.crud import get_user
from introduction.model import User


class TestGetUser:
    def test_idに一致するUserが取得できる(self, test_session):
        user = User(name="sato", birthday=date(1999, 12, 31))
        with test_session() as session:
            session.add(user)
            session.commit()
            user_id = user.id

        user_ = get_user(test_session, user_id)
        assert user_ == user

    def test_idに一致するUserが存在しない場合_Noneが返る(self, test_session):
        assert get_user(test_session, 1) is None
