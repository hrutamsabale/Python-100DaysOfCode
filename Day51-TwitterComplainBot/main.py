from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from time import sleep

SUBSCRIBED_DOWN_SPEED = "[YOUR_SUBSCRIBED_DOWN_SPEED]"
SUBSCRIBED_UP_SPEED = "[YOUR_SUBSCRIBED_UP_SPEED]"
EMAIL = "[YOUR_EMAIL]"
USERNAME = "[YOUR_USERNAME]"
PASSWORD = "[YOUR_PASSWORD]"
class InternetSpeedTwitterBot:
    def __init__(self):
        self.upspeed = 0
        self.downspeed = 0
        service = ChromeService(executable_path="C:\\Users\\{user}\\.wdm\\drivers\\chromedriver\\win64\\131.0.6778.85\\chromedriver-win32\\chromedriver.exe")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
        sleep(60)
        download_speed_res = self.driver.find_element(By.XPATH,
                                                 '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        self.downspeed = float(download_speed_res.get_attribute("textContent"))
        upload_speed_res = self.driver.find_element(By.XPATH,
                                               '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        self.upspeed = float(upload_speed_res.get_attribute("textContent"))

    def tweet_at_provider(self, message):
        self.driver.get("https://x.com/?lang=en")
        sleep(10)
        temp = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a')
        href = temp.get_attribute("href")
        self.driver.get(href)
        sleep(10)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email.send_keys(EMAIL)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]').click()
        sleep(10)
        try:
            username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            username.send_keys(USERNAME)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()
            sleep(10)
        except:
            pass
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(PASSWORD)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button').click()
        sleep(10)
        post = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        post.send_keys(message)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button').click()

    def close_browser(self):
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if bot.upspeed < SUBSCRIBED_UP_SPEED or bot.downspeed < SUBSCRIBED_DOWN_SPEED:
    message = (f"Hey service provider, I'm getting {bot.downspeed} down/ {bot.upspeed} up. "
               f"While I've subscribed for {SUBSCRIBED_DOWN_SPEED} down/ {SUBSCRIBED_UP_SPEED} up.")
    bot.tweet_at_provider(message)
bot.close_browser()
