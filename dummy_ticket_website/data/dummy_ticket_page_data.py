# data
user_name = "Vipin"
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
dep_date_link = (dep_date, "link")
# dep_month_calender=("//select[@data-handler='selectMonth']","xpath")
dep_month_calender = ("//select[@class='ui-datepicker-month']", "xpath")
dep_year_calender = ("//select[@data-handler='selectYear']", "xpath")
ret_calender = ("returndate", "id")
ret_date_link = (ret_date, "link")
ret_month_calender = ("//select[@data-handler='selectMonth']", "xpath")
ret_year_calender = ("//select[@data-handler='selectYear']", "xpath")

# Delivery option
delivery_visa_appointment = ('appoinmentdate', 'id')
delivery_option = (visa_appo_date, "link")
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
