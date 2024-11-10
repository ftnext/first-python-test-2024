import httpx

ENDPOINT = "http://zipcloud.ibsnet.co.jp/api/search"


def get_address(zipcode: str, /) -> str | None:
    """郵便番号から住所情報を検索する"""
    response = httpx.get(ENDPOINT, params={"zipcode": zipcode}, timeout=5)
    response.raise_for_status()
    data = response.json()

    if error_message := data["message"]:
        raise ValueError(error_message)
    if (results := data["results"]) is None:
        return None

    return f"{results[0]['address1']} {results[0]['address2']} {results[0]['address3']}"
