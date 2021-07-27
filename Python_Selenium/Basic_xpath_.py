from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver.maximize_window()
xpath1="//input[@name='travlastname']"
xpath2="//input[@id='travlastname']"
xpath3="//*[@id='travlastname']"
xpath4="//p//*[@id='travlastname']"
xpath5="//p//input[@id='travlastname']"
xpath6="//p[@id='travlastname_field']//input"
xpath7="//*[@id='travlastname_field']//input"
xpath8="//div[@id='customer_details']//input[@id='travlastname']"
xpath9="//div[@class='wcopc']//input[@id='travlastname']"

#Css Selector
CSS1="input[id='travlastname']"
CSS2="input[name='travlastname']"
CSS3="P[id='travlastname_field']>input"
CSS4="div[class='col-1']>div>p[id='travlastname_field']>input"