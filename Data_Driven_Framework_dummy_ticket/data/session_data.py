import os
from datetime import datetime

browser = 'chrome'
url = "https://www.google.co.in"
#yatra_url = "https://www.yatra.com/"
chrome_driver_path = "F:\\ToolsQAPython\\Browser\\chromedriver.exe"
dummy_url="https://www.dummyticket.com/dummy-ticket-for-visa-application/"


cure_dir = os.getcwd()

log_path  = os.path.join(cure_dir, 'logs')
excel_path=os.path.join(cure_dir,'data','excel_file')
log_file=datetime.now().strftime("%d_%m_%y_%H_%M_%S")
log_file_path=os.path.join(log_path,f"{log_file}.log")
headless= True
test_data_excel_file='dummy_ticket.xlsx'
test_data_excel_file_path=os.path.join(excel_path,test_data_excel_file)


