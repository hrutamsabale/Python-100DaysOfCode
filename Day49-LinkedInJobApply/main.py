from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from time import sleep

LOGIN_MAIL = "YOUR_MAIL_HERE"
LOGIN_PASSWORD = "PASSWORD"

service = ChromeService(executable_path="C:\\Users\\hruta\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4081835849&f_AL=true&f_WT=2&geoId=102713980&keywords=video%20editor&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")
sleep(2)

try:
    sign_in_button = driver.find_element(By.CSS_SELECTOR, ".sign-in-modal .sign-in-modal__outlet-btn")
    sign_in_button.click()
    sleep(2)
    email_input = driver.find_element(By.CSS_SELECTOR, ".text-input #base-sign-in-modal_session_key")
    password_input = driver.find_element(By.CSS_SELECTOR, ".text-input #base-sign-in-modal_session_password")
    email_input.send_keys(LOGIN_MAIL)
    password_input.send_keys(LOGIN_PASSWORD)
    sign_in_button1 = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
    sign_in_button1.click()
except:
    sign_in_button = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/form/p/button')
    sleep(2)
    email_input = driver.find_element(By.CSS_SELECTOR, ".text-input #session_key")
    password_input = driver.find_element(By.CSS_SELECTOR, ".text-input #session_password")
    email_input.send_keys(LOGIN_MAIL)
    password_input.send_keys(LOGIN_PASSWORD)
    sign_in_button1 = driver.find_element(By.XPATH, '//*[@id="main-content"]/div[1]/div[2]/form/div[2]/button')
    sign_in_button1.click()

# driver.quit()