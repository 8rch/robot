from RPA.Browser import Browser


def scrape():
    browser = Browser()
    # Open Wikipedia website
    browser.open("https://www.wikipedia.org/")
    # Search for Albert Einstein
    input_field = browser.element("#searchInput")
    input_field.clear()
    input_field.send_keys("")
    button = browser.button("[type='submit']")
    button.click()
    # Get text inside paragraph tag containing Albert Einstein name
    para = browser.xpath("//p[contains(.,'Albert Einstein')]").first
    return para.text


print(scrape())
