import smtplib
import datetime as dt
import random

my_email = "your@mail.com"
password = "yourpassword"

send_day = 0
week_day = dt.datetime.now().weekday()

if week_day == send_day:
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    quote_to_send = random.choice(quotes)
    subject = "Monday Motivation"
    with smtplib.SMTP("your-mail-smtp") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="addressee@mail.com",
                            msg=f"Subject:{subject}\n\n{quote_to_send}")
