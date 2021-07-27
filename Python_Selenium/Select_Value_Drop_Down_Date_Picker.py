from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

driver =webdriver.Chrome(executable_path="F:\\ToolsQA Python\\Browser\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)


driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

date_of_birth_element_id='dob'
month_drop_down_xpath="//select[@class='ui-datepicker-month']"
year_drop_down_xpath="//select[@class='ui-datepicker-year']"
add_more_passenger_checkbox_id='addmorepax'
add_more_passenger_dropdown_id='addpaxno'
#Select month and year in calendar.
driver.find_element_by_id(date_of_birth_element_id).click()
sleep(5)
select_month=Select(driver.find_element_by_xpath(month_drop_down_xpath))
select_month.select_by_visible_text('Apr')
sleep(5)
select_year=Select(driver.find_element_by_xpath(year_drop_down_xpath))
select_year.select_by_visible_text('1990')
sleep(5)
driver.find_element_by_xpath("//a[text()='28']").click()
sleep(5)
# click on add more passenger checkbox
driver.find_element_by_id(add_more_passenger_checkbox_id).click()
# Select value from checkbox
select_passenger=Select(driver.find_element_by_id(add_more_passenger_dropdown_id))
sleep(2)
select_passenger.select_by_visible_text('add 2 more passengers')
sleep(5)
driver.close()