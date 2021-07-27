import os
from datetime import datetime

import pytest
from Data_Driven_Framework_dummy_ticket.base.webdriver_factory import WebdriverFactory
from Data_Driven_Framework_dummy_ticket.data import session_data as data
from pytest_html_reporter import attach

'''@pytest.fixture(scope="session")
def setup():
    web = WebdriverFactory(data.browser, data.url)
    driver = web.get_driver_instance()
    return driver
'''


@pytest.fixture(scope="class")
def Class_setup(request):
    web = WebdriverFactory(data.browser, data.url)
    global driver
    driver = web.get_driver_instance()
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def dummy_setup(request):
    web = WebdriverFactory(data.browser, data.dummy_url)
    global driver
    driver = web.get_driver_instance()
    request.cls.driver = driver
    yield driver
    driver.quit()

def pytest_configure(config):
    '''Create a log  file if log_file is not mentioned in *.ini file'''
    if not config.option.log_file:
        timestamp=datetime.strftime(datetime.now(),'%Y-%m-%d_%H-%M-%S')
        #config.option.log_file='debug_'+ timestamp +'.log'
        config.option.log_file =os.path.join(data.log_path,'debug_' + timestamp + '.log')
