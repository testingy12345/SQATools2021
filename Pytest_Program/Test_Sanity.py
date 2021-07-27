from time import sleep
from .Data_File import *
from  Web_Locator import *
from  selenium import webdriver

def test_book_ticket(setup):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get(url)
    setup.find_element_by_id(user_name_field_id).send_keys(username)
    setup.find_element_by_id(surname_field_id).send_keys(surname)

def test_select_date_of_birth(setup):
    setup.find_element_by_id(calender_id).click()
    setup.find_element_by_link_text(birth_date)

def test_select_gender(setup):
    setup.find_element_by_id(male_gneder_id).click()

def test_select_more_passenge_checkbox(setup):
    setup.find_element_by_id(add_more_passenger_id)
    sleep(5)
    setup.close()