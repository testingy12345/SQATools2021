import pytest
from Data_Driven_Framework_dummy_ticket.modules.google_search_page import GoogleSearch
from Data_Driven_Framework_dummy_ticket.base.selenium_code import selenium_driver
from pytest_html_reporter import attach

@pytest.mark.usefixtures("class_setup")
class TestGoogleSearch:

    def test_search_data_google(self):
        gc = GoogleSearch(self.driver)
        gc.search_content()

    def test_click_on_link(self):
         try:
             dr = selenium_driver(self.driver)
             dr.click_element(("Welcome to Python.org", "link1"))
         except Exception as e:
             attach(data=self.driver.get_screenshot_as_png())
             raise e
