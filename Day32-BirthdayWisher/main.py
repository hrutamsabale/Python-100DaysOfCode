##################### Extra Hard Starting Project ######################
import pandas
import datetime
import random
import smtplib

my_mail = "gpoppy429@gmail.com"
password = "nytsizxvlqrwnvvd"

# 1. Update the birthdays.csv

birthday_data_df = pandas.read_csv("birthdays.csv")
birthday_data_list = birthday_data_df.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
birthday_person_name = ""
birthday_person_email = ""


def today_a_birthday():
    global birthday_person_name, birthday_person_email
    now = datetime.datetime.now()
    today_month = now.month
    today_day = now.day
    for record in birthday_data_list:
        if record["month"] == today_month and record["day"] == today_day:
            birthday_person_name = record["name"]
            birthday_person_email = record["email"]
            return True
    return False


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
def pick_letter():
    global birthday_person_name
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        letter_content = file.read()
        letter_content = letter_content.replace("[NAME]", birthday_person_name)
        letter_content = letter_content.replace("Angela", "Poppy")
    return letter_content


if today_a_birthday():
    letter_to_send = pick_letter()
    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=birthday_person_email,
            msg=f"Subject:Happy Birthday!\n\n{letter_to_send}"
        )
