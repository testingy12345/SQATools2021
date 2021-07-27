from selenium import webdriver
from time import sleep
driver=webdriver.Chrome(executable_path="F:\\ToolsQA Python\\Browser\\chromedriver.exe")
driver.maximize_window()

#Get the url
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

#Interact with text box

sleep(3)
driver.find_element_by_id("travname").send_keys("Vipin")

driver.find_element_by_id("travname").clear()

#Last name
sleep(3)

driver.find_element_by_id("travlastname").send_keys("Tekade")
driver.find_element_by_id("travlastname").clear()

#Put data to the text area
driver.find_element_by_id("order_comments").send_keys("vhjk")
sleep(3)

# interact with radio button
element=driver.find_element_by_id('sex_1')
print("I radio button is selected :",element.is_selected())
print("I radio button is enabled :",element.is_enabled())
print("I radio button is displayed :",element.is_enabled())
driver.close()

