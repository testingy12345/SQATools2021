from selenium import webdriver
from selenium.webdriver.chrome.options import Options #To run the browser on headless mode
from automation_framework1.data import session_data as data

class WebdriverFactory:
    def __init__(self,browser,url):
        self.browser=browser
        self.url=url

    def get_driver_instance(self):
        if self.browser.lower() =='chrome':
            #self.driver=webdriver.Chrome()
            chrome_option=Options()
            if data.headless:
                chrome_option.add_argument('--headless')
            self.driver=webdriver.Chrome(executable_path=data.chrome_driver_path ,options=chrome_option)
        elif self.browser.lower() == 'firefox':
            self.driver=webdriver.Firefox()
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        return self.driver