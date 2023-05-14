from datetime import datetime
import pandas
import random
import smtplib


MY_Email = "z0mb1e.zarak1@gmail.com"
password ="ynlmtgglgrxrjafe"

today = (datetime.now().month, datetime.now().day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        contents = letter.read()
        contents = contents.replace("[NAME]",birthdays_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_Email,password)
        connection.sendmail(
            from_addr=MY_Email,
            to_addrs=birthdays_person["email"],
            msg=f"Happy Birthday\n\n{contents}")






