import smtplib
import datetime as dt
import random

my_email = "z0mb1e.zarak1@gmail.com"
password = "ynlmtgglgrxrjafe"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
     connection.starttls()   #transport layer security,secure connection
     connection.login(user=my_email,password=password)
     connection.sendmail(
         from_addr=my_email,to_addrs="sumanbhandari854@yahoo.com",
         msg=f"Subject:Hello\n\n{quote}"
     )
















# import smtplib
#
#
# my_email = "z0mb1e.zarak1@gmail.com"
# password = "ynlmtgglgrxrjafe"
#
# # connection = smtplib.SMTP("smtp.gmail.com")
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()   #transport layer security,secure connection
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,to_addrs="sumanbhandari854@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
# # # connection.close()
#
#
# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# print(now)
#
# dob = dt.datetime(year=1999, month=5,day=2)
# print(dob)