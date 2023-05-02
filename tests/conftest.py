import pytest
from pages.api_client import ApiClient
from pages.user_cart import UserCart
from pages.user_cart import MainForm
from data.data_faker import UserEx

from data.data_faker import DataFaker


# ___API FIXTURE__

@pytest.fixture
def schema():
    return {"name": "string",
            "job": "string",
            "id": "string",
            "createdAt": "string"}


@pytest.fixture()
def create_user():
    return UserEx()


@pytest.fixture(scope="class")
def register(request):
    profile = request.param
    response = ApiClient().post("register", profile)
    token = response["token"]
    return profile, token


@pytest.fixture
def login(request):
    request.cls.login = "ajkajk"
    request.cls.password = "qwerty"


@pytest.fixture
def printer(request):
    print(request.node)
    print(dir(request.node))
    a = getattr(request.node, 'rep_call', None)
    print(request.node.rep_call.failed)


# __UI_FIXTURE__

@pytest.fixture
def open_text_box_form(create_driver):
    UserCart(create_driver).get_page("https://demoqa.com/text-box")

@pytest.fixture
def open_main_form(create_driver):
    create_driver.get("https://demoqa.com/automation-practice-form")


# __UTILS FIXTURE__
@pytest.fixture(scope="function")
def create_file(tmpdir):
    fn = tmpdir.mkdir("for")
    path = str(f'{fn}/for_testing.png')
    with open(path, 'w') as file:
        file.write("asdasd")
    yield path
    del path
