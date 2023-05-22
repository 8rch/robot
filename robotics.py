from RPA.Browser.Selenium import Selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from datetime import datetime

br = Selenium()


class Robot:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print("Hello, my name is " + self.name)

    def say_goodbye(self):
        print("Goodbye, my name is " + self.name)

    def open_webpage(self, webpage):
        br.open_available_browser(webpage)

    def split_date(date_string):
        # Regular expressions pattern to match day, month, and year
        pattern = r"(\d{1,2})\D+(\w+)\D+(\d{4})"

        match = re.search(pattern, date_string)
        if match:
            day = int(match.group(1))
            month = match.group(2)
            year = int(match.group(3))
            return day, month, year
        else:
            print("Invalid date format please correct")
            return None

    def calculate_age(birth_date, death_date):
        birth_day, birth_month, birth_year = split_date(birth_date)
        death_day, death_month, death_year = split_date(death_date)

        if birth_day and birth_month and birth_year and death_day and death_month and death_year:
            age = death_year - birth_year - 1
            if death_month > birth_month or (death_month == birth_month and death_day >= birth_day):
                age += 1
            return age
        else:
            return None

    def start_scrapping(self,):
        path = 'D:\prueba tecnica\dep\chromedriver'

        print("open the browser")

        browser = webdriver.Chrome(executable_path=path)

        print("# load the webpage")
        browser.get('https://www.wikipedia.org')
        sleep(1)
        browser.maximize_window()
        input_search = browser.find_element(By.ID, 'searchInput')
        search_button = browser.find_element(
            By.XPATH, "//i[contains(text(),'Search')]")
