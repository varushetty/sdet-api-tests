import pytest
from utils import api_client


@pytest.fixture
def all_posts():
    return api_client.get_posts()