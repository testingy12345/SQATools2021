from selenium import webdriver
from time import sleep
import pytest
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

@pytest.fixture(scope='module')
def setup():
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield
    driver.close()

@pytest.mark.smoke
@pytest.mark.sanity
def  test_Launch_Url_and_Verify(setup):
      driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
      element=driver.find_element_by_xpath("//h2[@class='fg-text-dark ffb-h2-1']/p[2]")
      expected_title="Dummy ticket booking"
      heading=element.text
      assert expected_title == heading

@pytest.mark.sanity
def test_passenger_details(setup):
     driver.find_element_by_id('travname').send_keys("Vipin")
     driver.find_element_by_id('travlastname').send_keys("Tekade")

     sleep(5)


@pytest.mark.smoke
def test_additional_notes(setup):
    driver.find_element_by_id('order_comments').send_keys("Travel Journey")
    sleep(5)

@pytest.mark.sanity
def date_of_birth(setup):
    driver.find_element_by_id('dob').click()
    sleep(5)
    #select_date=Select(driver.find_element_by_class_name('ui-state-default'))
    #select_date.
    select_month=Select(driver.find_element_by_class_name('ui-datepicker-month'))
    select_month.select_by_visible_text('Apr')
    sleep(5)
    select_year=Select(driver.find_element_by_class_name('ui-datepicker-year'))
    select_year.select_by_visible_text('1990')
    sleep(5)
    driver.find_element_by_xpath("//a[text()='28']").click()
    sleep(5)


@pytest.mark.smoke
def gender_identification(setup):
    Gender=driver.find_element_by_id('sex_1')
    Gender.click()
    print('male')
    sleep(5)

@pytest.mark.sanity
def add_more_passenger(setup):
    amp=driver.find_element_by_id('addmorepax')
    amp.click()
    select_nop=Select(driver.find_element_by_xpath('//*[@id="addpaxno_field"]/span[1]/span[1]/span'))
    select_nop.select_by_visible_text('add 2 more passengers')

@pytest.mark.smoke
def travel_detail(setup):
    roundTrip=driver.find_element_by_id('traveltype_2')
    roundTrip.click()
    fromCity=driver.find_element_by_id('fromcity')
    fromCity.send_keys('Nagpur')
    toCity=driver.find_element_by_id('tocity')
    toCity.send_keys('London')

@pytest.mark.sanity
def departure_date(setup):
    driver.find_element_by_id('departon').click()
    dep_month=Select(driver.find_element_by_class_name('ui-datepicker-month'))
    dep_month.select_by_visible_text('May')
    sleep(5)
    dep_year=Select(driver.find_element_by_class_name('ui-datepicker-year'))
    dep_year.select_by_visible_text('2021')
    sleep(5)
    driver.find_element_by_xpath("//a[text()='3']").click()
    sleep(5)

@pytest.mark.smoke
def return_date(setup):
    driver.find_element_by_id('ui-datepicker ui-widget ui-widget-content ui-helper-clearfix ui-corner-all notranslate').click()
    ret_month=Select(driver.find_element_by_class_name('ui-datepicker-month'))
    ret_month.select_by_visible_text('May')
    sleep(5)
    ret_year=Select(driver.find_element_by_class_name('ui-datepicker-year'))
    ret_year.select_by_visible_text('2021')
    sleep(5)
    driver.find_element_by_xpath("//a[text()='31']")
    sleep(5)

@pytest.mark.sanity
def delivery_option(setup):
    driver.find_element_by_id('appoinmentdate').click()
    delivery_month=Select(driver.find_element_by_class_name('ui-datepicker-month'))
    delivery_month.select_by_visible_text('May')
    sleep(5)
    drivery_year=Select(driver.find_element_by_class_name('ui-datepicker-year'))
    drivery_year.select_by_visible_text('2021')
    driver.find_element_by_xpath("//a[text()='25']").click()

@pytest.mark.smoke
def dummy_ticket(setup):
    email=driver.find_element_by_id('deliverymethod_1')
    email.click()
    sleep(5)
    print('Email button got clicked ',email)
    whats_app=driver.find_element_by_id('deliverymethod_2')
    whats_app.click()
    sleep(5)
    print('Whats app option got clicked',whats_app)
    both=driver.find_element_by_id('deliverymethod_3')
    both.click()
    sleep(5)
    print('Both the option got clicked',both)

@pytest.mark.sanity
def billing_detail(setup):
    driver.find_element_by_id('billname').send_keys('Vipin')
    driver.find_element_by_id('billing_phone').send_keys('8208627925')
    driver.find_element_by_id('billing_email').send_keys('a@gmail.com')
    country_details=Select(driver.find_element_by_id('select2-billing_country-container'))
    country_details.select_by_visible_text('United Kingdom (UK)')
    sleep(5)

@pytest.mark.smoke
def street_address(setup):
    driver.find_element_by_id('billing_address_1').send_keys('Roopena Agahara')
    driver.find_element_by_id('billing_address_2').send_keys('Benguluru')
    driver.find_element_by_id('billing_city').send_keys('London')
    driver.find_element_by_id('billing_state').send_keys('UK')
    driver.find_element_by_id('billing_postcode').send_keys('560068')

@pytest.mark.sanity
def additional_info(setup):
    driver.find_element_by_id('order_comments').send_keys('Done')
    sleep(5)
