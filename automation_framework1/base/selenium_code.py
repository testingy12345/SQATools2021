from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class selenium_driver:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver, 10)

    def get_locator_type(self ,locator):
        if locator.lower() =="xpath":
            return By.XPATH

        elif locator.lower() =="id":
            return By.ID

        elif locator.lower() == "css":
            return By.CSS_SELECTOR

        elif locator.lower() == "link":
            return By.LINK_TEXT

        elif locator.lower() =="partial link":
            return By.PARTIAL_LINK_TEXT

        elif locator.lower() =="name":
            return By.NAME


    def click_element(self , element):
        web_element= element[0]
        element_type=self.get_locator_type(element[1])
        elem=self.wait.until(ec.element_to_be_clickable((element_type ,web_element)))
        elem.click()

    def input_text(self,element ,value):
        web_element=element[0]
        element_type=self.get_locator_type(element[1])
        elem=self.wait.until(ec.visibility_of_element_located((element_type,web_element)))
        elem.send_keys(value)



            #To debug the code use
            #import pnb;pnb.set_trace()
            #for dubugging see the video after 1:13 min
