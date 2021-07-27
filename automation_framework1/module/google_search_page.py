from automation_framework1.base.selenium_code import selenium_driver
from  automation_framework1.data.google_search_page_data import*


class GoogleSearch(selenium_driver):
    def __init__(self,driver):
        super().__init__(driver)

    def search_content(self):
        self.input_text(search_field,search_data)
        self.click_element(search_button)


    """def click_test_on_link(self):
        try:
        
            dr=selenium_driver(self.driver)
            dr.click_element(("Welcome to Python.org","link1"))
        except Exception as e:
            attach(data=self.driver.get_screenshot_as_png())
            raise e
    """