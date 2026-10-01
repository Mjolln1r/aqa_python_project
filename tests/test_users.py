import pytest
from jsonschema import validate
from schemes import user_schema
from pydantic import BaseModel
import allure
from playwright.sync_api import Page
from playwright.sync_api import expect


class UserSchema(BaseModel):
    id: int
    name: str
    email: str


def test_get_user_pydantic(api_client):
    with allure.step("Отправить GET запрос /users/1"):
        response = api_client.get(endpoint="/users/1")
    with allure.step("Проверить успешный статус 200"):
        assert response.status_code == 200, "Not found user"
    with allure.step("Валидировать через пайдентик"):
        UserSchema(**response.json())


def test_get_user_schema(api_client):
    with allure.step("Отправить GET запрос /users/1"):
        response = api_client.get(endpoint="/users/1")
    with allure.step("Проверить успешный статус 200"):
        assert response.status_code == 200, "Not found user"
    with allure.step("Валидировать схему через jsonschema"):
        validate(response.json(), schema=user_schema)


@pytest.mark.parametrize(
    "user_id, field, expected_value",
    [
        (1, "name", "Leanne Graham"),
        (1, "email", "Sincere@april.biz"),
        (2, "name", "Ervin Howell")
    ]
)
def test_get_user_field_value(api_client, user_id, field, expected_value):
    response = api_client.get(endpoint=f"/users/{user_id}")
    assert response.status_code == 200, 'Not 200'
    assert response.json()[field] == expected_value, 'Incorrect field "Name"'


@pytest.mark.parametrize(
    "user_id",
    [
        999,
        99999,
        0
    ]
)
def test_get_user_not_found(api_client, user_id):
    assert api_client.get(endpoint=f"/users/{user_id}").status_code == 404, 'Not 404'


def test_create_user(api_client):
    data = {"name": "Kirill", "job": "AQA"}
    assert api_client.post(endpoint="/posts", data=data).status_code == 201, 'Not Created'


def test_get_all_users(api_client):
    with allure.step("Отправить GET запрос /users"):
        response = api_client.get(endpoint="/users")
    with allure.step("Проверить успешный статус 200"):
        assert response.status_code == 200, 'Not Found'
    with allure.step("Провалидировать список юзеров"):
        users = response.json()
        assert isinstance(users, list)
        assert len(users) > 0, 'Список пользователей пуст'


def test_get_user_id(get_api):
    with allure.step("Отправить GET запрос /users"):
        response = get_api.get_users_id(5)
    with allure.step("Проверить успешный статус 200"):
        assert response.status_code == 200, "Not found user"
    with allure.step("Проверить id юзера"):
        assert response.json()["id"] == 5


def test_create_user_post(post_api):
    with allure.step("Отправить POST запрос создав юзера"):
        response = post_api.create_post(data_post={"name": "Andrey", "job": "MQA"})
    with allure.step("Проверить успешный статус 201, user создался"):
        assert response.status_code == 201
    with allure.step("Проверить name созданного user"):
        assert response.json()["name"] == "Andrey"


def test_ui(page: Page):
    page.goto("https://example.com/")
    expect(page.locator("h1")).to_have_text("Example Domain")
    expect(page.get_by_role("link", name="Learn more")).to_be_visible()

def test_example_page(example_page):
    example_page.open_url()
    expect(example_page.get_title()).to_have_text("Example Domain")
    expect(example_page.get_more_info_link()).to_be_visible()