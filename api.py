from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import openai  # Import OpenAI library

# Set up your OpenAI API key
openai.api_key = ''

# Start a new Chrome session
driver = webdriver.Chrome()

# Open the website where you want to fill in the form
driver.get("https")
time.sleep(5)

# Function to generate dynamic input using ChatGPT API
def generate_input(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Find all form fields on the webpage
form_fields = driver.find_elements(By.XPATH, "//input | //textarea")
print(form_fields)
# Loop through each form field and fill in dynamically generated input
for field in form_fields:
    # Get the label or placeholder of the field for generating prompt
    label = field.get_attribute("placeholder") or field.get_attribute("aria-label") or field.get_attribute("name") or field.get_attribute("label")
    print(label)
    
    # Generate dynamic input using ChatGPT API
    dynamic_input = generate_input(f"Enter {label}: ")
    
    # Fill in the form field with the dynamic input
    field.send_keys(dynamic_input)

# Submit the form
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()

# Add a delay to see the result (you can adjust this delay)
time.sleep(5)

# Close the browser
driver.quit()