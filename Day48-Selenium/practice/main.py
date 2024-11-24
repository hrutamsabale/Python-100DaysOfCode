from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from time import sleep
from selenium.webdriver.common.keys import Keys


service = ChromeService(executable_path="C:\\Users\\hruta\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.amazon.in/?ie=UTF8&ext_vrnc=hi&tag=googhydrabk-21&ascsubtag=_k_Cj0KCQjw8IaGBhCHARIsAGIRRYp7eEX-Mgw7E5bYleY38gix-UaKniIOvX36GafMzsLSNKYLS9Nz9YkaAt3FEALw_wcB_k_&ext_vrnc=hi&gclid=Cj0KCQjw8IaGBhCHARIsAGIRRYp7eEX-Mgw7E5bYleY38gix-UaKniIOvX36GafMzsLSNKYLS9Nz9YkaAt3FEALw_wcB")
search_bar = driver.find_element(By.ID, 'twotabsearchtextbox')
sleep(2)
search_bar.send_keys("Iphone 16")
sleep(2)
search_bar.send_keys(Keys.ENTER)

# driver.quit()


# -----------------------------------------------GETTING STARTED--------------------------------------------------------

# driver.get("https://www.amazon.in/Apple-iPhone-16-128-GB/dp/B0DGHZWBYB/?_encoding=UTF8&pd_rd_w=8fQj4&content-id=amzn1.sym.509965a2-791b-4055-b876-943397d37ed3%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=509965a2-791b-4055-b876-943397d37ed3&pf_rd_r=3AR817JXJVYRTDX7VPJJ&pd_rd_wg=mLmUe&pd_rd_r=59507f68-c54d-4468-9c77-309a17a1fea2&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.get_attribute("textContent"))
# print(price.text)

# driver.get("https://www.amazon.in/Apple-iPhone-16-128-GB/dp/B0DGHZWBYB/?_encoding=UTF8&pd_rd_w=8fQj4&content-id=amzn1.sym.509965a2-791b-4055-b876-943397d37ed3%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=509965a2-791b-4055-b876-943397d37ed3&pf_rd_r=3AR817JXJVYRTDX7VPJJ&pd_rd_wg=mLmUe&pd_rd_r=59507f68-c54d-4468-9c77-309a17a1fea2&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1")
# search_box = driver.find_element(By.ID, "twotabsearchtextbox")
# print(search_box.get_attribute("aria-label"))

# driver.get("https://www.amazon.in/Apple-iPhone-16-128-GB/dp/B0DGHZWBYB/?_encoding=UTF8&pd_rd_w=8fQj4&content-id=amzn1.sym.509965a2-791b-4055-b876-943397d37ed3%3Aamzn1.symc.fc11ad14-99c1-406b-aa77-051d0ba1aade&pf_rd_p=509965a2-791b-4055-b876-943397d37ed3&pf_rd_r=3AR817JXJVYRTDX7VPJJ&pd_rd_wg=mLmUe&pd_rd_r=59507f68-c54d-4468-9c77-309a17a1fea2&ref_=pd_hp_d_atf_ci_mcx_mr_ca_hp_atf_d&th=1")
# title = driver.find_element(By.CSS_SELECTOR, "#title #productTitle")
# print(title.get_attribute("textContent"))
# print(title.text)

#---------------------------------------CLICKING A LINK-------------------------------------------------------------

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# sleep(2)
# article_count.click()
# sleep(2)

