import pytest
from pages.api_client import ApiClient
from pages.user_cart import UserCart
from data.data_faker import User


@pytest.fixture(scope="class")
def register(request):
    profile = request.param
    response = ApiClient().post("register", profile)
    token = response["token"]
    return profile, token


@pytest.fixture()
def open_text_box_form(create_driver):
    UserCart(create_driver).get_page("https://demoqa.com/text-box")


@pytest.fixture()
def create_user():
    return User()
