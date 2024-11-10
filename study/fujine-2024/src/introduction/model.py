# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=34
from __future__ import annotations

from datetime import date

from sqlalchemy import String
from sqlalchemy.orm import Mapped, declarative_base, mapped_column

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(12), nullable=False)
    birthday: Mapped[date] = mapped_column(nullable=False)

    def __eq__(self, other: User) -> bool:
        return (
            (self.id == other.id)
            and (self.name == other.name)
            and (self.birthday == other.birthday)
        )
