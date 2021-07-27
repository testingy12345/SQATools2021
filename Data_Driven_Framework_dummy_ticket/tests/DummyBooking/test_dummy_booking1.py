import logging

import pytest
from Data_Driven_Framework_dummy_ticket.modules.dummy_ticket_search_page1 import Dummy_Ticket
from  Data_Driven_Framework_dummy_ticket.data.dummy_ticket_page_data1 import *
from time import sleep

from dummy_ticket_website.data.dummy_ticket_page_data import *

log=logging.getLogger(__name__)

@pytest.mark.usefixtures("dummy_setup")
class Test_Dummy_Booking:

    #@pytest.mark.country
    def test_provide_passenger_entry(self):
        global dm
        log.info('Test Dummy Ticket booking execution has started')
        dm= Dummy_Ticket(self.driver)
        log.info('Enter the first name of passenger')
        dm.enter_first_name(user_name)
        log.info('Enter the last name of passenger')
        dm.enter_last_name(last_name)

    #@pytest.mark.dob
    def test_select_dob(self):
        #dm.select_dob(date_of_birth)
        log.info('Enter the date of birth')
        dm.select_dob(dob_month, dob_year)
        #dm.select_male_gender()
        sleep(5)

    def test_select_gender(self):
        log.info('Enter the gender ')
        dm.select_male_gender()
        sleep(5)

    def test_select_more_passenger(self):
        log.info('Enter the extra passenger')
        dm.select_more_passenger(extra_passenger)
        sleep(5)

    def test_select_add_info(self):
        log.info('Enter add info')
        dm.enter_add_info(add_info)
        sleep(5)

    def test_round_trip(self):
        log.info('Enter round trip')
        dm.select_round_trip()
        sleep(5)

    def test_origin_and_destination_city(self):
        log.info('Enter origin and destination city')
        dm.enter_origin_destination_city(origin_city,destination_city)
        sleep(5)

    def test_select_dep(self):
        #dm.click_element()
        log.info('Enter departure month and year')
        dm.select_dep_date(dep_month,dep_year)
        sleep(5)

    def test_select_ret(self):
        log.info('Enter return month and year')
        dm.select_ret_date(ret_month,ret_year)
        sleep(5)


    def test_delivery_option(self):
        log.info('Enter Visa appointment month and year')
        dm.select_delivery_option(visa_appo_month,visa_appo_year)
        sleep(5)

    def test_both_option(self):
        log.info('Select both option')
        dm.select_both_option()

    def test_bill_name(self):
        log.info('Enter billing name')
        dm.enter_billing_detail(billing_name1)

    def test_phone_no(self):
        log.info('Enter Phone Number')
        dm.enter_phone_number(phone)

    def test_email_address(self):
        log.info('Enter email address')
        dm.enter_email_address(email_address)

    def test_street_address(self):
        log.info('Enter Street Address')
        dm.enter_street_address(street_address)

    #@pytest.mark.country
    def test_select_country(self):
        log.info('Select the country')
        dm.select_county(country)

    def test_apartment_name(self):
        log.info('Enter Appartment name')
        dm.enter_apart_name(apartment1)

    def test_town_city(self):
        log.info('Enter Town city')
        dm.enter_town_city(town_city)

    def test_country(self):
        log.info('Enter Country')
        dm.enter_country(country1)

    def test_post_code(self):
        log.info('Enter post code')
        dm.enter_postcode(postcode1)

    def test_order_notes(self):
        log.info('Enter order notes')
        dm.enter_order_notes(order_notes)
        log.info('Test dummy ticket excution has finished ')

