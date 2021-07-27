from selenium import webdriver
from time import sleep
import sys
#browser= 'edge'
print(sys.argv)
browser=sys.argv[1]
driver= None
if browser == 'chrome':
    #driver = webdriver.Chrome(executable_path="F:\\ToolsQA Python\\Browser\\chromedriver.exe")

    driver = webdriver.Chrome()

elif browser == 'firefox':
    driver = webdriver.Firefox()
elif browser == 'edge':
    driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://www.google.co.in')
driver.find_element_by_name('q').send_keys("Python")
sleep(20)
driver.find_element_by_name('btnK').click()
sleep(10)
driver.close()