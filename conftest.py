import pytest
from data.data_faker import DataFaker
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--browser_version", action="store", default="")
    parser.addoption("--headless", action="store_true", default=False)
    parser.addoption("--url", action="store", default="")


@pytest.fixture(scope="session")
def get_config(request):
    config = {
        "browser": request.config.getoption("--browser"),
        "verison": request.config.getoption("--browser_version"),
        "headless": request.config.getoption("--headless"),
        "url": request.config.getoption("--url")
    }

    return config


@pytest.fixture(scope="session")
def create_driver(get_config):
    if get_config["browser"] == "chrome":
        chrome_option = ChromeOptions()
        chrome_option.add_argument("window-size=1920,1080")
        chrome_option.headless = get_config["headless"]
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_option)
    elif get_config["browser"] == "firefox":
        geko_options = FirefoxOptions()
        geko_options.add_argument("window-size=1920,1080")
        geko_options.headless = get_config["headless"]
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=geko_options)
    else:
        raise TypeError("Unsupported browser. Set chrome or firefox")
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def create_user():
    return DataFaker().get_first_name(), DataFaker()


@pytest.fixture(scope='session')
def new_fixture():
    pass

