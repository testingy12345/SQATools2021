college_id=6010
college_list_url="https://www.sqatools.in/2021/05/pune-college-list.html"
college_id_list=['6001','6002','6003','6004','6005','6006','6007','6008','6009','6010']

from Data_Driven_Framework_dummy_ticket.data.session_data import test_data_excel_file_path
from  Data_Driven_Framework_dummy_ticket.utilities.ExcelReader import Excel_Reader
sheet_name='dummy_ticket'
excel_obj=Excel_Reader(test_data_excel_file_path)