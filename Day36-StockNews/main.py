import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla"
NEWS_API_KEY = "f6ce951673694ab1b49ea6aed0b4286e"
ALPHAVANTAGE_API_KEY = "CSOAPG7D9EYMVMR2"
account_sid = 'AC17b46fc48294752b4c85670e1ff96c3e'
auth_token = 'b4786d5adcb29d91b7155ec84871c91b'
messaging_service_sid = 'MGc2193eba4cde0f4f034256962bce3387'

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# ALPHAVANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
# ALPHAVANTAGE_PARAMETERS = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK,
#     "apikey": ALPHAVANTAGE_API_KEY
# }
#
# with requests.get(url=ALPHAVANTAGE_ENDPOINT, params=ALPHAVANTAGE_PARAMETERS) as response:
#     response.raise_for_status()
#     stock_data = response.json()
#
# closing_prices_list = []
# today_date = []
# for (key, value) in stock_data["Time Series (Daily)"].items():
#     closing_prices_list.append(float(value["4. close"]))
#     today_date.append(key)
# today_date = today_date[0]
#
# yesterday_close = closing_prices_list[0]
# day_before_yesterday_close = closing_prices_list[1]
#
# price_difference = yesterday_close - day_before_yesterday_close
# price_difference_perc = price_difference / yesterday_close * 100

today_date = "2024-10-25"
price_difference_perc = -5.61

if price_difference_perc > 5 or price_difference_perc < 5:
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    emoji = ""
    if price_difference_perc > 5:
        emoji = "🔺"
    else:
        emoji = "🔻"
    NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_PARAMETERS = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
        "from": today_date,
        "to": today_date,
        "sortBy": "popularity",
        "language": "en"
    }
    with requests.get(url=NEWS_API_ENDPOINT, params=NEWS_PARAMETERS) as response:
        response.raise_for_status()
        news = response.json()
    news_articles = news["articles"]
    news_articles = news_articles[:3]
    articles = []
    for article in news_articles:
        source = article["source"]["name"]
        title = article["title"]
        body = article["description"]
        temp = f"{source}: {title}.\n\nBrief: {body}"
        articles.append(temp)
    ## STEP 3: Use https://www.twilio.com
    # Send a seperate message with the percentage change and each article's title and description to your phone number.
    client = Client(account_sid, auth_token)
    for article in articles:
        message = client.messages.create(
            messaging_service_sid= messaging_service_sid,
            body=f'{STOCK} {emoji}{abs(price_difference_perc)}%\n\n{article}',
            to='+917798893439'
        )



#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

