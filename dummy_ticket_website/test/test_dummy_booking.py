import pytest
from dummy_ticket_website.modules.dummy_ticket_search_page import Dummy_Ticket
from  dummy_ticket_website.data.dummy_ticket_page_data import *
from time import sleep



@pytest.mark.usefixtures("dummy_setup")
class Test_Dummy_Booking:

    #@pytest.mark.country
    def test_ptovide_passenger_entry(self):
        global dm
        dm= Dummy_Ticket(self.driver)
        dm.enter_first_name(user_name)
        dm.enter_last_name(last_name)

    #@pytest.mark.dob
    def test_select_dob(self):
        #dm.select_dob(date_of_birth)
        dm.select_dob(dob_month, dob_year)
        #dm.select_male_gender()
        sleep(5)

    def test_select_gender(self):
        dm.select_male_gender()
        sleep(5)

    def test_select_more_passenger(self):
        dm.select_more_passenger(extra_passenger)
        sleep(5)

    def test_select_add_info(self):
        dm.enter_add_info(add_info)
        sleep(5)

    def test_round_trip(self):
        dm.select_round_trip()
        sleep(5)

    def test_origin_and_destination_city(self):
        dm.enter_origin_destination_city(origin_city,destination_city)
        sleep(5)

    def test_select_dep(self):
        #dm.click_element()
        dm.select_dep_date(dep_month,dep_year)
        sleep(5)

    def test_select_ret(self):
        dm.select_ret_date(ret_month,ret_year)
        sleep(5)


    def test_delivery_option(self):
        dm.select_delivery_option(visa_appo_month,visa_appo_year)
        sleep(5)

    def test_both_option(self):
        dm.select_both_option()

    def test_bill_name(self):
        dm.enter_billing_detail(billing_name1)

    def test_phone_no(self):
        dm.enter_phone_number(phone)

    def test_email_address(self):
        dm.enter_email_address(email_address)

    def test_street_address(self):
        dm.enter_street_address(street_address)

    #@pytest.mark.country
    def test_select_country(self):
        dm.select_county(country)

    def test_apartment_name(self):
        dm.enter_apart_name(apartment1)

    def test_town_city(self):
        dm.enter_town_city(town_city)

    def test_country(self):
        dm.enter_country(country1)

    def test_post_code(self):
        dm.enter_postcode(postcode1)

    def test_order_notes(self):
        dm.enter_order_notes(order_notes)
