
from dummy_ticket_website.base.selenium_code import selenium_driver
from dummy_ticket_website.data.dummy_ticket_page_data import *


class Dummy_Ticket(selenium_driver):
    def __init__(self , driver):
        super().__init__(driver)

    def enter_first_name(self,first_name):
        self.input_text(first_name_field, first_name)

    def enter_last_name(self,last_name):
        self.input_text(last_name_field, last_name)

    def select_dob(self, month, year):
        self.click_element(dob_calender)
        self.select_value_from_dropdown(month_dropdown, month)
        self.select_value_from_dropdown(year_dropdown, year)
        self.click_element(date_link)

    def select_male_gender(self):
        self.click_element(gender_button)

    def select_more_passenger(self, value):
        self.click_element(add_more_passenger_checkbox)
        self.select_value_from_dropdown(add_more_pass_dropdown, value)


    def enter_add_info(self,add_info):
        self.input_text(additional_info,add_info)

    def select_round_trip(self):
        self.click_element(add_round_trip)

    def enter_origin_destination_city(self,origin_city,destination_city):
        self.input_text(add_from_city,origin_city)
        self.input_text(add_to_city,destination_city)

    """
    def select_dep_and_ret_date(self,month1,year1,month2,year2):
        self.click_element(dep_calender)
        self.select_value_from_dropdown(dep_month_calender,month1)
        self.select_value_from_dropdown(dep_year_calender,year1)
        self.click_element(dep_date_link)
        self.click_element(ret_calender)
        self.select_value_from_dropdown(ret_month_calender,month2)
        self.select_value_from_dropdown(ret_year_calender,year2)
        
    """
    def select_dep_date(self,month1,year1):
        self.click_element(dep_calender)
        self.select_value_from_dropdown(dep_month_calender, month1)
        self.select_value_from_dropdown(dep_year_calender, year1)
        self.click_element(dep_date_link)

    def select_ret_date(self,month2,year2):
        self.click_element(ret_calender)
        self.select_value_from_dropdown(ret_month_calender, month2)
        self.select_value_from_dropdown(ret_year_calender, year2)
        self.click_element(ret_date_link)

    def select_delivery_option(self,month3,year3):
        self.click_element(delivery_visa_appointment)
        self.select_value_from_dropdown(del_month_option,month3)
        self.select_value_from_dropdown(dep_year_calender,year3)
        self.click_element(delivery_option)

    def select_both_option(self):
        self.click_element(both_option)

    def enter_billing_detail(self,bill_name):
        self.input_text(billing_name,bill_name)

    def enter_phone_number(self,ph_no):
        self.input_text(billing_phone,ph_no)

    def enter_email_address(self,ema):
        self.input_text(billing_email,ema)

    def enter_street_address(self,st):
        self.input_text(billing_address,st)

    def select_county(self,uk):
        self.click_element(billing_dpdn)
        self.select_value_from_dropdown(billing_contry,uk)

    def enter_apart_name(self,ap):
        self.input_text(apartment,ap)

    def enter_town_city(self,tc):
        self.input_text(billing_city,tc)

    def enter_country(self,ct):
        self.input_text(country_optional,ct)

    def enter_postcode(self,pc):
        self.input_text(postcode,pc)

    def enter_order_notes(self,on):
        self.input_text(additional_info,on)