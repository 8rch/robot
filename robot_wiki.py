from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import date, datetime
import datetime
import re


def introduce_yourself():
    robot_name = "Quandrinaut"
    introduction = f"Hey there! I'm {robot_name}, your Robotic Researcher.\n I'm here to assist you with any questions or information you need.\n Feel free to ask me anything!"

    print(introduction)


print("_______________________________________________________________________________________________________________________________________________________________________________\n")

introduce_yourself()

print("_______________________________________________________________________________________________________________________________________________________________________________\n")

### LIST OF SCIENTISTS###
SCIENTISTS = ["Albert Einstein", "Isaac Newton", "Charles Darwin",
              "Marie Curie"]

### START THE PROCESS ###
print("_______________________________________________________________________________________________________________________________________________________________________________\n")

print("####################  Loading variables #################### ")

path = 'D:\prueba tecnica\dep\chromedriver'

print("open the browser")

browser = webdriver.Chrome(executable_path=path)
sleep(1)

print("_______________________________________________________________________________________________________________________________________________________________________________\n")

print("#################### load the webpage #################### ")

browser.get('https://www.wikipedia.org')
browser.maximize_window()
sleep(2)
input_search = browser.find_element(By.ID, 'searchInput')
search_button = browser.find_element(
    By.XPATH, "//i[contains(text(),'Search')]")


class Person:
    def __init__(self, name, age, born, dead):
        self.name = name
        self.age = age
        self.born = born
        self.dead = dead


class Dates:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


def split_date(date_string):
    pattern = r"(\d{1,2})\s+([a-zA-Z]+)\s+(\d{4})"

    match = re.search(pattern, date_string)
    if match:
        return match.group(1), match.group(2), match.group(3)
    else:
        print("Invalid date format")
        return None


def month_to_number(month_name):
    try:
        month_number = datetime.datetime.strptime(month_name, "%B").month
        return month_number
    except ValueError:
        print("Invalid month name")
        return None


def convert_month_to_number(date_tuple):
    day, month, year = date_tuple
    try:
        month_number = month_to_number(month)
        if month_number:
            return day, month_number, year
        else:
            raise ValueError("Invalid month name")
    except (ValueError, TypeError):
        print("Invalid date format")
        return None


def calculate_age(birth_date, death_date):
    birth_day, birth_month, birth_year = map(int, birth_date)
    death_day, death_month, death_year = map(int, death_date)

    age = death_year - birth_year - 1
    if death_month > birth_month or (death_month == birth_month and death_day >= birth_day):
        age += 1
    return age


def process_date(date_tuple):
    # Convert the tuple to a string
    date_string = str(date_tuple)
    # Remove parentheses and single quotes
    cleaned_date = date_string.replace(
        "(", "").replace(")", "").replace("'", "")
    # Split the cleaned date into separate values
    values = cleaned_date.split(", ")
    # Concatenate the values into a single string
    concatenated_date = " ".join(values)
    return concatenated_date


def center_log(log_message, total_width=80):
    log_length = len(log_message)
    if log_length >= total_width:
        return log_message
    padding = (total_width - log_length) // 2
    centered_log = " " * padding + log_message + " " * padding
    return centered_log


print("_______________________________________________________________________________________________________________________________________________________________________________\n")
print("_______________________________________________________________________________________________________________________________________________________________________________\n")

print("################################################# STARTTING THE PROCESS #################################################")

for i in range(len(SCIENTISTS)):
    input_search.send_keys(SCIENTISTS[i])
    sleep(1)
    search_button.click()

    age = []
    p = []

    for j in range(1):
        print('#################### Scraping page', j+1,
              "Information of", SCIENTISTS[i], "#################### ")

        born = browser.find_elements(By.XPATH,
                                     "(//tbody/tr[3]/td[1])[1]")
        for m in born:
            born = m.text
            born = split_date(born)

        birth_date = born
        birth_date = convert_month_to_number(birth_date)

        died = browser.find_elements(By.XPATH,
                                     "(//tbody/tr[4]/td[1])[1]")
        # info = browser.find_elements(
        #     By.XPATH, "//body/div[2]/div[1]/div[3]/main[1]/div[3]/div[3]/div[1]/p[1]")

        for s in died:
            died = s.text
            died = split_date(died)

        death_date = died
        death_date = convert_month_to_number(death_date)

        age = calculate_age(birth_date, death_date)

        data_born = process_date(born)
        data_died = process_date(died)

        print(SCIENTISTS[i], " was born on", data_born,
              " and passed away on ", data_died, ". He lived for ", age, "years.")

        text = []

        para_elements = browser.find_elements(
            By.XPATH, f"//p[contains(., '{SCIENTISTS[i]}')][1]")
        for para in para_elements:
            text.append(para.text)
        print("\n", text, "\n \n")
    browser.get('https://www.wikipedia.org')
    browser.maximize_window()
    input_search = browser.find_element(By.ID, 'searchInput')
    search_button = browser.find_element(
        By.XPATH, "//i[contains(text(),'Search')]")


browser.quit()
