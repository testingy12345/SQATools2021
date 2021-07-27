import pytest
from dummy_ticket_website.base.webdriver_factory import WebdriverFactory
from dummy_ticket_website.data import session_data as data
from pytest_html_reporter import attach


@pytest.fixture(scope="session")
def setup():
    web=WebdriverFactory(data.browser,data.url)
    driver=web.get_driver_instance()
    return driver

@pytest.fixture(scope="class")
def class_setup(request):
    web=WebdriverFactory(data.browser,data.url)
    global driver
    driver=web.get_driver_instance()
    request.cls.driver=driver
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def dummy_setup(request):
    web=WebdriverFactory(data.browser,data.dummy_url)
    global driver
    driver=web.get_driver_instance()
    request.cls.driver=driver
    yield driver
    driver.quit()


