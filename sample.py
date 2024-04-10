from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Replace these with your GitHub credentials
email = "your_email@example.com"
password = "your_password"

# Start a new Chrome session
driver = webdriver.Chrome()

# Open GitHub login page
driver.get("")
time.sleep(10)
# Find the email field and enter email
email_field = driver.find_element(By.ID, "input-4")
email_field.send_keys(email)

# Find the password field and enter password
password_field = driver.find_element(By.ID, "input-5")
password_field.send_keys(password)

# Submit the form
password_field.send_keys(Keys.ENTER)

# Add a delay to ensure page fully loads (you might need to adjust this delay)
time.sleep(5)

# You are now logged in. You can add further actions here, like navigating to a specific page or performing certain tasks.

# Close the browser
driver.quit()