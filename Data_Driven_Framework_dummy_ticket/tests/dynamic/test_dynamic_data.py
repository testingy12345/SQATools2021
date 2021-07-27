import pytest

from Data_Driven_Framework_dummy_ticket.data.dynamic_data import *
from Data_Driven_Framework_dummy_ticket.modules.dynamic.dynamic import Dynamic
from Data_Driven_Framework_dummy_ticket.base.selenium_code import selenium_driver
from pytest_html_reporter import  attach
from time import sleep
import logging

from Data_Driven_Framework_dummy_ticket.modules.dynamic.dynamic import Dynamic

log= logging.getLogger(__name__)

@pytest.mark.usefixtures("Class_setup")
class TestDynamic:

    def test_select_dynamic(self):
        self.driver.get(college_list_url)
        global obj
        obj=Dynamic(self.driver)
        obj.select_dynamic_checkbox('6001')
        sleep(10)

    def test_select_multiple_checkbox(self):
        for id in college_id_list:
            obj = Dynamic(self.driver)
            obj.select_dynamic_checkbox(id)
            sleep(10)

    def test_select_multiple_checkbox_from_excel(self):
        sheet_name='dynamic'
        excel_obj=Excel_Reader(test_data_excel_file_path)
        for i in range(1,9):
            #obj = Dynamic(self.Driver)
            id=excel_obj.read_excel_data(i,1 ,sheetname=sheet_name)
            log.info(f"institude id from excel {id} ")
            obj.select_dynamic_checkbox(id)
            sleep(5)