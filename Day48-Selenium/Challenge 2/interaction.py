from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(executable_path="C:\\Users\\hruta\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
that_number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')

print(that_number.get_attribute("textContent"))


driver.quit()