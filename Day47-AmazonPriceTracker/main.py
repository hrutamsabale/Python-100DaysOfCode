from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

PRESET_PRICE = 45000
SENDER_MAIL = os.environ["SENDER_MAIL"]
PASSWORD = os.environ["PASSWORD"]
RECEIVER_MAIL = os.environ["RECEIVER_MAIL"]
LINK_TO_PRODUCT ="https://www.amazon.in/Sony-CFI-2008A01X-PlayStation%C2%AE5-Console-slim/dp/B0CY5HVDS2/ref=sr_1_4?crid=2AXNQG1Q87IOW&dib=eyJ2IjoiMSJ9.pFhgCqcURNHp7Ghh6tpkbr3wM7lOnFnLWPSDBBE7NSk2C-n6sRFbINxUJ4HBbdyEH88_yVAVNpaF078pJi3r-K_Mh_ExLvWk1c1kfnXYzPeMLOy-GIDsrti-IU5_cD0fBbrYpJXbC_QGO9sWe_yMUZO4aKaqbFqU5IeAsi2GHve4vLfQF6JBX5imN1TlvaSJinu-yqxnS-mGC3BJfkCE7XLAJmrfkhgajo45V5PsSEo.ohW0167iV8BpHXEFMODkCTwJUo9UGRiG-NAySOiG2OA&dib_tag=se&keywords=ps5&qid=1732276172&sprefix=ps%2Caps%2C239&sr=8-4"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

with requests.get(url=LINK_TO_PRODUCT, headers=headers) as response:
    content = response.text

soup = BeautifulSoup(content, "html.parser")

price_whole = soup.find(name="span", class_="a-price-whole")
try:
    price = float(price_whole.getText().split(",")[0]+price_whole.getText().split(",")[1])
except IndexError:
    price = float(price_whole.getText())
product = soup.find(name="span", id="productTitle")
product_title = product.getText().strip()

if price < PRESET_PRICE:
    msg = f"Subject:Price Drop Alert\n\n{product_title} dropped below the set price ({PRESET_PRICE}) to {price} on Amazon.\nLink to buy: {LINK_TO_PRODUCT}".encode("utf-8")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=SENDER_MAIL, password=PASSWORD)
    connection.sendmail(from_addr=SENDER_MAIL, to_addrs=RECEIVER_MAIL, msg=msg)
    connection.close()
