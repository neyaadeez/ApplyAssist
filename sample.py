from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://github.com/neyaadeez")
script = "alert('Alert via selenium')"
driver.execute_async_script(script) 