# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=36
from sqlalchemy import select
from sqlalchemy.orm import scoped_session

from introduction.model import User


def get_user(db_session: scoped_session, user_id: int) -> User | None:
    statement = select(User).where(User.id == user_id)
    return db_session.scalar(statement)


def add_user(db_session: scoped_session, user: User) -> User:
    with db_session() as session:
        session.add(user)
        session.commit()
        return user.id
