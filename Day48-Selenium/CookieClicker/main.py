from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time

service = ChromeService(executable_path="C:\\Users\\hruta\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

TIMEOUT_SECS = 5
FINISHED_MINS = 5
all_ids = [item.get_attribute("id") for item in driver.find_elements(By.CSS_SELECTOR, "#store div")]

cookie = driver.find_element(By.ID, "cookie")

# ------------------------------------FUNCTIOMS-----------------------------------#
def remove_comma(number):
    temp = ""
    for char in number:
        if char != ",":
            temp += char
    return temp

def get_store():
    all_prices = [int(remove_comma(item.get_attribute("textContent").split()[-1])) for item in driver.find_elements(By.CSS_SELECTOR, "#store b")]
    item_dictionary = {}
    for i in range(len(all_ids)):
        item_dictionary[all_prices[i]] = all_ids[i]
    return item_dictionary


def get_money():
    money_bar = driver.find_element(By.ID, "money")
    money = remove_comma(money_bar.get_attribute("textContent"))
    return int(money)

def buy_something(current_money, current_store):
    id_to_buy = ""
    for price in current_store:
        if current_money >= price:
            id_to_buy = current_store[price]
    try:
        item_to_buy = driver.find_element(By.ID, id_to_buy)
        item_to_buy.click()
    except:
        return


# ---------------------------------------MAIN LOOP----------------------------------#
finished = time.time() + 60*FINISHED_MINS

while time.time() < finished:
    # reset timeout
    timeout = time.time() + TIMEOUT_SECS
    while time.time() < timeout:
        cookie.click()
    curr_store = get_store()
    curr_money = get_money()
    buy_something(curr_money, curr_store)

cookies_ps = driver.find_element(By.ID, "cps").get_attribute("textContent")

driver.quit()

print(cookies_ps)
