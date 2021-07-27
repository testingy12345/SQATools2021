from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from time import sleep

driver=webdriver.Chrome(executable_path="F:\\ToolsQA Python\\Browser\\chromedriver.exe")
driver.maximize_window()

#Fluent wait
wait=WebDriverWait(driver,5 , poll_frequency=1)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

# Apply fluent wait on lastname field
last_name=wait.until(ec.visibility_of_element_located((By.NAME,'travlastname')))
last_name.send_keys("Tekade")
sleep(10)
print("Execution completed")
driver.close()