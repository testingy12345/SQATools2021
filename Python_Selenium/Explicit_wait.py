from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep
driver=webdriver.Chrome(executable_path="F:\\ToolsQA Python\\Browser\\chromedriver.exe")
driver.maximize_window()

#Explicit wait
wait=WebDriverWait(driver,10)
#Fluent Wait

#wait2=WebDriverWait.
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# Apply Explicit wait on specific element
first_name=wait.until(ec.visibility_of_element_located((By.NAME,'travname')))
first_name.send_keys('Vipin')
#last_name=wait
print("Execution Successful")
sleep(20)
driver.close()
