from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from time import sleep

PHONE_NUMBER = "[YOUR_PHONE_HERE]"
EMAIL = "[YOUR_MAIL_HERE]"
PASSWORD = "[YOUR_PASSWORD_HERE]"
LINK = "[JOB_LINK_HERE]"

service = ChromeService(executable_path="C:\\Users\\{user}\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

to_continue = True

while to_continue:
    try:
        driver.get(LINK)
        sleep(2)
        sign_in_button = driver.find_element(By.CSS_SELECTOR, ".sign-in-modal .sign-in-modal__outlet-btn")
        sign_in_button.click()
        sleep(2)
        email_input = driver.find_element(By.CSS_SELECTOR, ".text-input #base-sign-in-modal_session_key")
        password_input = driver.find_element(By.CSS_SELECTOR, ".text-input #base-sign-in-modal_session_password")
        email_input.send_keys(EMAIL)
        password_input.send_keys(PASSWORD)
        sign_in_button1 = driver.find_element(By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')
        sign_in_button1.click()
        to_continue = False
    except:
        driver.refresh()

sleep(5)
all_job_listings = driver.find_elements(By.CSS_SELECTOR, "#main .plliipbnMJubKrlhVezhSdzOdCrvRaZWcTY .scaffold-layout__list-item")
for job in all_job_listings[5:]:
    job.click()
    sleep(1)
    easy_apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply .jobs-apply-button--top-card .jobs-apply-button")
    easy_apply_button.click()
    sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply .jobs-apply-button").click()
        sleep(2)
    except:
        pass
    bottom_button = driver.find_element(By.CSS_SELECTOR, "footer .display-flex button")
    if bottom_button.get_attribute("textContent").strip() != "Submit application":
        driver.find_element(By.CSS_SELECTOR, '.artdeco-button .artdeco-button__icon use').click()
        sleep(1)
        driver.find_element(By.CSS_SELECTOR, '.artdeco-modal--layer-confirmation .artdeco-modal__actionbar button').click()
        sleep(1)
    else:
        phone_input = driver.find_element(By.CSS_SELECTOR, '.artdeco-text-input--input')
        bottom_button.click()
        sleep(10)
        driver.find_element(By.CSS_SELECTOR, ".artdeco-modal button svg use").click()
        sleep(1)