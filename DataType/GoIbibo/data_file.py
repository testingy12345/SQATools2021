browser='chrome'
url='https://www.goibibo.com'

#Input Data
source_location_search='Nagpur'
select_source='Nagpur (NAG)'
destination_location_search='Chennai'
select_destination='Chennai (MAA)'
depart_date= '23'
return_date= '31'

adult = 2
child = 2
infant = 2
flight_type = 'First class'

#locators
soure_field_id='gosuggest_inputSrc'
source_drop_down_value="//ul[contains(@id,'react-autosuggest')]//div"
destination_field_id='gosuggest_inputDest'
date_xpath="//div[text()='date']"
return_calender_path="//input[@id='returnCalendar']"
passenger_section_id='pax_link_common'
add_adults_id='adultPaxPlus'
add_child_id='childPaxPlus'
add_infant_id='infantPaxPlus'
flight_type_dropdown='gi_class'
search_button_id='gi_search_btn'

