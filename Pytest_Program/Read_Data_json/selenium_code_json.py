from selenium import webdriver
from Read_Jason_File import get_json_data
from time import sleep

test_data=get_json_data()
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(test_data['url'])
driver.find_element_by_id('travname')
driver.find_element_by_id('travlastname')
sleep(5)