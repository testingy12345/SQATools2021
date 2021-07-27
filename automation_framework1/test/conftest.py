import pytest
from automation_framework1.base.webdriver_factory import WebdriverFactory
from automation_framework1.data import session_data as data

@pytest.fixture(scope="session")
def setup():
    web=WebdriverFactory(data.browser,data.url)
    driver=web.get_driver_instance()
    return driver