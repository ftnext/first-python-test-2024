# ref: https://speakerdeck.com/mhrtech/pyconjp2024-pytest?slide=21
import pytest

from introduction.env import get_api_url


@pytest.fixture
def mock_env_api_url(monkeypatch):
    monkeypatch.setenv("API_URL", "http://localhost:8080")


def test_get_api_url(mock_env_api_url):
    assert get_api_url() == "http://localhost:8080"
