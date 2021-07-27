from selenium import webdriver
from time import sleep

driver =webdriver.Chrome(executable_path="F:\\ToolsQA Python\\Browser\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
sleep(5)
element=driver.find_element_by_id('travname')
sleep(5)

# Through get attribute method we can get any attribute value   of the element
class_name=element.get_attribute('class')
sleep(5)

print(class_name)
sleep(5)

driver.get("https://www.sqatools.in/p/manual-testing.html")
sleep(5)
List_elements=driver.find_elements_by_tag_name('a')

for element in List_elements:
    # Get attribute value using get_attribute method
     print(element.get_attribute('href'))
     sleep(5)
    # Get text of any element using text method
     print(element.text)

driver.close()
