#import BY as BY
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

driver =webdriver.Chrome(executable_path="F:\\ToolsQA Python\\Browser\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

college_url = 'https://www.collegedekho.com/engineering/colleges-in-india/'
driver.get(college_url)

"""get_element_list=driver.find_element_by_xpath("//a[@title]")
with open('college_list.txt','a') as file:
    for element in get_element_list:
        college_name=element.get_attribute('title')
        file.write(f"{college_name}\n")
        print(college_name)
        """
"""college_list_element=driver.find_element_by_xpath("//div[@class='row collegeBlock']//div[@class='title']/a")
college_link=[]
for element in college_list_element:
    try:
        link=element.get_attribute('href')
        college_link.append(link)
    except:
        pass
for link in college_link:
    driver.get(link)
"""
element_xpath="//div[@class='row collegeBlock']//div[@class='title']/a"
wait=WebDriverWait(driver, 20)
element_list=wait.until(ec.visibility_of_element_located((By.XPATH,element_xpath)))
for element in element_list:
    print(element.get_Attribute('title'))
    print(element.get_Attribute('href'))
driver.close()
