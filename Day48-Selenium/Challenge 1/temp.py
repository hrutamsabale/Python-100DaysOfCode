from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path="C:\\Users\\hruta\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.python.org/")
events = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li a")
event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li time")

event_dict = {i:{"date":event_dates[i].get_attribute("textContent"), "name":events[i].get_attribute("textContent")} for i in range(len(events))}

print(event_dict)


driver.quit()