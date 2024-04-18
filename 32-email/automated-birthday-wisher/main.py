import smtplib
import datetime as dt
import random
import pandas

my_email = "your@mail.com"
password = "yourpassword"

day = dt.datetime.now().day
month = dt.datetime.now().month
today = (day, month)

birthdays_data_frame = pandas.read_csv("birthdays.csv")

birthdays_dict = {index: data_row for (index, data_row) in birthdays_data_frame.iterrows()}

for x in birthdays_dict:
    birth_date = (birthdays_dict[x]["day"], birthdays_dict[x]["month"])
    if birth_date == today:
        number = random.randint(1, 3)
        with open(f"./letter_templates/letter_{number}.txt", "r") as file_let:
            all_lines = file_let.readlines()
            all_lines[0] = all_lines[0].replace("[NAME]", birthdays_dict[x]["name"])

        subject = "Birthday!"
        to_send = ''.join(all_lines)
        with smtplib.SMTP("your-mail-smtp.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthdays_dict[x]["email"],
                                msg=f"Subject:{subject}\n\n{to_send}")
