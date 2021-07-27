from Data_Driven_Framework_dummy_ticket.base.selenium_code import selenium_driver
from Data_Driven_Framework_dummy_ticket.data.google_search_page_data import *

class GoogleSearch(selenium_driver):
    def __init__(self, driver):
        super().__init__(driver)

    def search_content(self):
        self.input_text(search_field, search_data)
        self.click_element(search_button)