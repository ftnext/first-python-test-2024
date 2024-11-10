# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=20
import os

# os.environ["API_URL"] = "https://production.example.com"


def get_api_url() -> str | None:
    """環境変数API_URLの設定値を返す（未設定ならNoneを返す）"""
    return os.getenv("API_URL")
