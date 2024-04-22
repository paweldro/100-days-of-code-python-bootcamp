import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

alphavantage_api_key = os.environ.get("alphavantage_api_key")
parameters_alphavantage = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alphavantage_api_key
}

news_api_key = os.environ.get("news_api_key")
parameters_news = {
    "apiKey": news_api_key,
    "q": COMPANY_NAME,
}

account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
to_number = os.environ.get("to_number")

response_alphavantage = requests.get("https://www.alphavantage.co/query", params=parameters_alphavantage)
response_alphavantage.raise_for_status()
data_alphavantage = response_alphavantage.json()

last_refreshed_date = data_alphavantage["Meta Data"]["3. Last Refreshed"]

last_refreshed_date_tab = last_refreshed_date.split("-")
day_before = int(last_refreshed_date_tab[2]) - 1
day_before_last_refreshed_date_tab = last_refreshed_date_tab.copy()
day_before_last_refreshed_date_tab[2] = str(day_before)
day_before_last_refreshed_date = "-".join(day_before_last_refreshed_date_tab)

data_last = data_alphavantage["Time Series (Daily)"][last_refreshed_date]
data_day_before_last = data_alphavantage["Time Series (Daily)"][day_before_last_refreshed_date]

last_close = float(data_last["4. close"])
day_before_last_close = float(data_day_before_last["4. close"])

price_increase = ((last_close - day_before_last_close) / last_close) * 100

if price_increase >= 0:
    price_increase_str = "🔺" + str(round(price_increase, 2)) + "%"
else:
    price_increase *= -1
    price_increase_str = "🔻" + str(round(price_increase, 2)) + "%"

info_to_send = ""

if price_increase >= 5:
    response_news = requests.get("https://newsapi.org/v2/top-headlines", params=parameters_news)

    response_news.raise_for_status()
    data_news = response_news.json()

    articles = data_news["articles"]

    articles_filtered = []
    for article in articles:
        if article["title"] != "[Removed]":
            articles_filtered.append(article)

    client = Client(account_sid, auth_token)

    for article in articles_filtered:
        article_info = (f"\n {STOCK} | {price_increase_str}\n\n{article['author']} | "
                        f"{article['publishedAt'].split('T')[0]}\n\n"
                        f"Headline: {article['title']}\n\n Brief: {article['description']}\n\n")

        message = client.messages \
            .create(
                body=article_info,
                from_='+13342768078',
                to=to_number
            )
