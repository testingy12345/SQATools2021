from Data_Driven_Framework_dummy_ticket.base.selenium_code import selenium_driver
from Data_Driven_Framework_dummy_ticket.data import *

class Dynamic(selenium_driver):
    def __init__(self ,driver):
        super().__init__(driver)
        #//td[text()='6001']//parent::tr//input

    '''def select_dynamic_checkbox(self, dynamic_xpath):
        dynamic_xpath=f"//td[text()='college_id']//parent::tr//input"
        self.click_element((dynamic_xpath,"xpath"))
    '''

    def select_dynamic_checkbox(self, institude_id):
        dynamic_xpath = f"//td[text()={institude_id}]//parent::tr//input"
        self.click_element((dynamic_xpath, "xpath"))