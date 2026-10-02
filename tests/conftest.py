from playwright.async_api import Page

from client.api_client import APIClient
from client.api_client import GetApi
from client.api_client import PostApi
import pytest

from pages.example_page import ExamplePage

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture
def api_client():
    return APIClient(base_url=BASE_URL)


@pytest.fixture
def get_api():
    return GetApi(base_url=BASE_URL)


@pytest.fixture
def post_api():
    return PostApi(base_url=BASE_URL)


@pytest.fixture
def example_page(page: Page):
    return ExamplePage(page)