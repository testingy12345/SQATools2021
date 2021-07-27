from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome(executable_path="F:\\ToolsQA Python\\Browser\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.sqatools.in/2020/08/dropdown.html")

"""
select_obj=Select(driver.find_element_by_id("cars"))
sleep(5)
#select_obj.select_by_visible_text("BMW Sport Car")
#sleep(5)
#select_obj.select_by_value("Jaguar Laxury")
#sleep(5)
select_obj.select_by_index(1)
""""""
#sleep(5)
"""
def select_value_from_dropdown(Locator,value):
    select_obj=Select(driver.find_element_by_id(Locator))
    sleep(5)
    select_obj.select_by_visible_text(value)
    sleep(5)
select_value_from_dropdown('cars','Jaguar Laxury')
select_value_from_dropdown('cars','Land Rover')
select_value_from_dropdown('cars','BMW Sport Car')

driver.close()

