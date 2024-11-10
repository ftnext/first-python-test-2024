# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=39
from datetime import date

import pytest
import sqlalchemy
from sqlalchemy import select

from introduction.crud import add_user
from introduction.model import User


class TestAddUser:
    def test_新規Userレコードが挿入される(self, test_session):
        user = User(name="tanaka", birthday=date(1999, 12, 31))
        user_id = add_user(test_session, user)

        assert user == test_session.scalar(select(User).where(User.id == user_id))

    def test_PKが同じUserレコードを複数挿入すると_IntegrityErrorが送出される(
        self, test_session
    ):
        with pytest.raises(sqlalchemy.exc.IntegrityError) as ex:
            for _ in range(2):
                add_user(
                    test_session, User(id=1, name="tanaka", birthday=date(1999, 12, 31))
                )

        error_message = str(ex.value)
        # テスト用の依存にPyMySQLを追加しているが、そこまでしなくてもいいのではないかと思った
        assert "pymysql.err.IntegrityError" in error_message
        assert "1062" in error_message  # 主キー重複のエラーコード
