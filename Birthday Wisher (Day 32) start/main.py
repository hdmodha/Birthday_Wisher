import datetime as dt
import smtplib
import random

now = dt.datetime.now()
weekday = now.weekday()
with open("quotes.txt", "r") as file:
    list_quotes = file.readlines()
if weekday == 0:
    one_quote = random.choice(list_quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="<your-email>", password="<your-password>")
        connection.sendmail(
            from_addr="<your-email>",
            to_addrs="<receiver-email>",
            msg=f"Subject:Motivational Quote\n\n {one_quote}",
        )
