import os

from openpyxl.reader.excel import ExcelReader

from Data_Driven_Framework_dummy_ticket.data.session_data import excel_path
from Data_Driven_Framework_dummy_ticket.utilities.ExcelReader import Excel_Reader

sheet_name = 'Google'
dummy_ticket_excel_file = os.path.join(excel_path, 'dummy_ticket.xlsx')
excel_obj = ExcelReader(dummy_ticket_excel_file)
#search_data = "Python"

search_data = excel_obj.read_excel_data(1, 1, sheetname=sheet_name)





#locators
search_field = ("q", "name")
search_button = ("btnK", "name")
