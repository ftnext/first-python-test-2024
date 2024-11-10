# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=29
"""http://zipcloud.ibsnet.co.jp/doc/api をコードで表す"""

from dataclasses import dataclass
from typing import TypedDict


class Result(TypedDict):
    address1: str
    address2: str
    address3: str
    # kana1: str
    # kana2: str
    # kana3: str
    # prefcode: str
    # zipcode: str


class ResponseJson(TypedDict):
    message: str | None
    results: list[Result] | None


@dataclass
class MockResponse:
    message: str | None = None
    results: list[Result] | None = None

    def raise_for_status(self) -> None:
        return None

    def json(self) -> ResponseJson:
        return {"message": self.message, "results": self.results}
