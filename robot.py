from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


path = 'D:\prueba tecnica\dep\chromedriver'

print("open the browser")

browser = webdriver.Chrome(executable_path=path)

print("# load the webpage")
browser.get('https://www.amazon.ca')
browser.maximize_window()
input_search = browser.find_element(By.ID, 'twotabsearchtextbox')
search_button = browser.find_element(By.XPATH, "(//input[@type='submit'])[1]")
print("#####input search")
input_search.send_keys("Smartphones under 10000")
sleep(1)
search_button.click()

products = []
for i in range(4):
    print('Scraping page', i+1)
    product = browser.find_elements(By.XPATH,
                                    "//span[@class='a-size-medium a-color-base a-text-normal']")
    for p in product:
        products.append(p.text)
    next_button = browser.find_element(By.XPATH, "//a[text()='Next']")
    next_button.click()
    sleep(2)

print(len(products), "#########product Length###########")

print(products[:5], "############Products###########")


browser.quit()
