from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="F:\\ToolsQA Python\\Browser\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
sleep(5)
driver.refresh()
# Click on dummy ticket for visa application
Dummy =driver.find_element_by_id("product_549")
Dummy.click()
print("Clicked on dummy ticket for visa application",Dummy)
sleep(5)
# Dummy return ticket
Dummy1 =driver.find_element_by_id("product_550")
Dummy1.click()
print("Clicked on Dummy return ticket",Dummy1)
# Dummy hotel booking
Dummy2=driver.find_element_by_id("product_551")
Dummy2.click()
print("Dummy hotel booking",Dummy2)
sleep(5)
#Dummy ticket and hotel
Dummy3=driver.find_element_by_id("product_3186")
Dummy3.click()
print("Dummy ticket & hotel booking",Dummy3)
sleep(5)
#Past dated ticket
Dummy4=driver.find_element_by_id("product_7441")
Dummy4.click()
print("Dummy Past dated ticket",Dummy4)
sleep(5)
#Male
Gender=driver.find_element_by_id("sex_1")
Gender.click()
print("Male Gender")
sleep(5)
#Female
Gender1=driver.find_element_by_id("sex_2")
Gender1.click()
print("Female Gender")
sleep(5)
#One way
Ow=driver.find_element_by_id("traveltype_1")
Ow.click()
print("One Way")
sleep(5)
#Round Trip
Rt=driver.find_element_by_id("traveltype_2")
Rt.click()
print("Round Trip")
sleep(5)
#Email
Email=driver.find_element_by_id("deliverymethod_1")
Email.click()
print("Email")
sleep(5)
#What's app
Wapp=driver.find_element_by_id("deliverymethod_2")
Wapp.click()
print("What's app")
sleep(5)
#Both
Both=driver.find_element_by_id("deliverymethod_3")
Both.click()
print("Both")
sleep(5)

driver.close()
