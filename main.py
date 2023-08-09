##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
my_email="piyush92111mishra@gmail.com"
password="keybdmdzevpqeljl"
connection=smtplib.SMTP("smtp.gmail.com", 587)
connection.starttls()

# 1. Update the birthdays.csv
main_dict={}
with open("letter_templates/birthdays.csv") as birthday_data:
    birthday_data_dataframe=pandas.read_csv(birthday_data)

    #print(birthday_data_dataframe["day"])
    birthday_data_dict=birthday_data_dataframe.to_dict(orient="records")
    #print(birthday_data_dict)
    for i in birthday_data_dict:
        main_dict[i["name"]]={"email":i["email"], "month":i["month"], "day":i["day"]}
    #print(main_dict)


# 2. Check if today matches a birthday in the birthdays.csv
datetime=dt.datetime
now=datetime.now()
month=now.month
day=now.day
print(month)
print(day)
for i in main_dict:
    if main_dict[i]["month"]==month and main_dict[i]["day"]==day:
        x = random.randint(1, 3)
        with open(f"letter_templates/letter_{x}.txt") as letter:
            old_word = "[NAME]"
            new_word = f"{i}"

            # Read the file and replace the word
            content = letter.read()
            modified_content = content.replace(old_word, new_word)

            # Write the modified content back to the file
            with open(f"letter_templates/letter_{x}.txt", 'w') as letter:
                letter.write(modified_content)
        with open(f"letter_templates/letter_{x}.txt") as letter:
            read_letter=letter.read()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=main_dict[i]["email"], msg=read_letter)
        connection.close()


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
