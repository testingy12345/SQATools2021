from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="F:\\ToolsQA Python\\Browser\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

element=driver.find_element_by_id("addmorepax")

if element.is_enabled():
    element.click()
    sleep(2)
    driver.find_element_by_id('select2-addpaxno-container').click()
    sleep(2)
    driver.find_element_by_xpath("//li[contains(text(),'add 3 more passengers')]").click()
    sleep(2)

sleep(5)

driver.find_element_by_id('dob4').click()
sleep(2)
driver.find_element_by_xpath("//a[text()='28']").click()
sleep(2)
driver.close()