# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

# enter keyword to search
keyword = "geeksforgeeks"

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

login_form = driver.find_element(By.XPATH, "//form[1]")
login_form.send_keys("hello world")
login_form.click()

# print complete element
print(login_form)
