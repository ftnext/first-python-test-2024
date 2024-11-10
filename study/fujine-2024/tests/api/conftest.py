# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=30
import re

import httpx
import pytest

from .mockresponse import MockResponse


@pytest.fixture
def mock_response(monkeypatch):
    def mock_get(*args, **kwargs) -> MockResponse:
        zipcode = kwargs["params"]["zipcode"]

        if zipcode == "0000000":
            empty_response = MockResponse()
            return empty_response
        elif re.match("^[0-9]{7}$", zipcode):
            return MockResponse(
                results=[
                    {"address1": "都道府県", "address2": "市区町村", "address3": "番地"}
                ]
            )
        else:
            return MockResponse(message="郵便番号の桁数や値が不正です。")

    monkeypatch.setattr(httpx, "get", mock_get)
