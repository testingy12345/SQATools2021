import os
from Data_Driven_Framework_dummy_ticket.data.session_data import excel_path
from Data_Driven_Framework_dummy_ticket.utilities.ExcelReader import Excel_Reader
sheet_name = 'dummy_ticket'

dummy_ticket_excel_path=os.path.join(excel_path,'dummy_ticket.xlsx')
excel_obj=Excel_Reader(dummy_ticket_excel_path)


# data
user_name = excel_obj.read_excel_data(1, 2, sheetname=sheet_name)
last_name = excel_obj.read_excel_data(2, 2, sheetname=sheet_name)
date_of_birth = excel_obj.read_excel_data(3, 2, sheetname=sheet_name)
dob_month = excel_obj.read_excel_data(4, 2, sheetname=sheet_name)
dob_year = excel_obj.read_excel_data(5, 2, sheetname=sheet_name)
extra_passenger = excel_obj.read_excel_data(6, 2, sheetname=sheet_name)
add_info=excel_obj.read_excel_data(7,2,sheetname=sheet_name)
origin_city=excel_obj.read_excel_data(8,2 ,sheetname=sheet_name)
destination_city=excel_obj.read_excel_data(9,2 ,sheetname=sheet_name)
dep_date=excel_obj.read_excel_data(10,2 ,sheetname=sheet_name)
dep_month=excel_obj.read_excel_data(11,2 ,sheetname=sheet_name)
dep_year=excel_obj.read_excel_data(12,2 ,sheetname=sheet_name)
ret_date=excel_obj.read_excel_data(13,2 ,sheetname=sheet_name)
ret_month=excel_obj.read_excel_data(14,2,sheetname=sheet_name)
ret_year=excel_obj.read_excel_data(15,2,sheetname=sheet_name)
visa_appo_date=excel_obj.read_excel_data(16,2,sheetname=sheet_name)
visa_appo_month=excel_obj.read_excel_data(17,2,sheetname=sheet_name)
visa_appo_year=excel_obj.read_excel_data(18,2,sheetname=sheet_name)
billing_name1=excel_obj.read_excel_data(19,2 ,sheetname=sheet_name)
phone=excel_obj.read_excel_data(20,2,sheetname=sheet_name)
email_address=excel_obj.read_excel_data(21,2,sheetname=sheet_name)
street_address=excel_obj.read_excel_data(22,2,sheetname=sheet_name)
country=excel_obj.read_excel_data(23,2,sheetname=sheet_name)
apartment1=excel_obj.read_excel_data(24,2,sheetname=sheet_name)
town_city=excel_obj.read_excel_data(25,2,sheetname=sheet_name)
country1=excel_obj.read_excel_data(26,2,sheetname=sheet_name)
postcode1=excel_obj.read_excel_data(27,2,sheetname=sheet_name)
order_notes=excel_obj.read_excel_data(28,2,sheetname=sheet_name)


'''user_name = "Vipin"
last_name = "Tekade"
date_of_birth = "28"
dob_month = 'Apr'
dob_year = '1990'
add_info = 'Loves to travel'
extra_passenger = 'add 2 more passengers (200%)'
origin_city = 'Nagpur'
destination_city = 'London'
country = 'United Kingdom (UK)'
apartment = 'Milton Kenyes'
dep_date = "1"
dep_month = 'Jun'
dep_year = '2021'
ret_date = "30"
ret_month = 'Jun'
ret_year = '2021'
visa_appo_date = '28'
visa_appo_month = 'May'
visa_appo_year = '2021'
billing_name1 = 'Vipin'
phone = '9677607354'
email_address = 'vtekade4@gmail.com'
street_address = 'Unit 4, 222 Kingsland Rd , London, Greater London, E2 8AX'
country = 'United Kingdom (UK)'
apartment1 = "Birmingham Palace"
town_city = 'London'
country1 = 'UK'
postcode1 = 'BBND 1ZZ'
order_notes = "Thank you"
'''
# Locator
first_name_field = ("travname", "id")
last_name_field = ("travlastname", "id")
dob_calender = ("dob", "id")
month_dropdown = ("//select[@class='ui-datepicker-month']", "xpath")
year_dropdown = ("//select[@data-handler='selectYear']", "xpath")
date_link = (date_of_birth, "link")
gender_button = ("sex_1", "id")
additional_info = ("order_comments", "id")

add_more_passenger_checkbox = ('addmorepax', 'id')
add_more_pass_dropdown = ('addpaxno', 'id')
add_round_trip = ('traveltype_2', 'id')
add_from_city = ('fromcity', 'id')
add_to_city = ('tocity', 'id')
dep_calender = ('departon', 'id')
#dep_date_link = (dep_date, "link")
# dep_month_calender=("//select[@data-handler='selectMonth']","xpath")
dep_month_calender = ("//select[@class='ui-datepicker-month']", "xpath")
dep_year_calender = ("//select[@data-handler='selectYear']", "xpath")
ret_calender = ("returndate", "id")
#ret_date_link = (ret_date, "link")
ret_month_calender = ("//select[@data-handler='selectMonth']", "xpath")
ret_year_calender = ("//select[@data-handler='selectYear']", "xpath")

# Delivery option
delivery_visa_appointment = ('appoinmentdate', 'id')
#delivery_option = (visa_appo_date, "link")
del_month_option = ("//select[@data-handler='selectMonth']", "xpath")
del_year_option = ("//select[@data-handler='selectYear']", "xpath")

# Receive Dummy_Ticket
both_option = ('deliverymethod_3', 'id')
# Billing name
billing_name = ('billname', 'id')
billing_phone = ('billing_phone', 'id')
billing_email = ('billing_email', 'id')
billing_address = ('billing_address_1', 'id')
billing_dpdn=("//p[@id='billing_country_field']","xpath")
billing_contry = ("//span[@id='select2-billing_country-container']", "xpath")
apartment = ('billing_address_2', 'id')
billing_city = ('billing_city', 'id')
country_optional = ('billing_state', 'id')
postcode = ('billing_postcode', 'id')
additional_info = ('order_comments', 'id')

