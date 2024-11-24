from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys

service = ChromeService(executable_path="C:\\Users\\hruta\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

# Locating the First Name Input Bar
f_name_bar = driver.find_element(By.NAME, "fName")
f_name_bar.send_keys("Henry")

# Locating the Last Name Input Bar
l_name_bar = driver.find_element(By.NAME, "lName")
l_name_bar.send_keys("Cavill")

# Locating the Email Input Bar
email_bar = driver.find_element(By.NAME, "email")
email_bar.send_keys("notsuperman@warnerbros.dc.com")

# Locating sign-up button
sign_up_button = driver.find_element(By.CSS_SELECTOR, ".form-signin button")
sign_up_button.click()

# driver.quit()