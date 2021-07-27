from selenium import webdriver
from time import sleep
driver =webdriver.Chrome(executable_path="F:\\ToolsQA Python\\Browser\\chromedriver.exe")
driver.get("https://www.google.co.in")
driver.maximize_window()
sleep(5)
driver.find_element_by_name('q').send_keys('Selenium')
sleep(2)
driver.find_element_by_name('btnK').click()
sleep(5)
driver.close()
#driver.find_element_by_name()
