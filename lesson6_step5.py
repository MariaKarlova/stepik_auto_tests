from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(
        By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e) * 10000))
    )
    link.click()

    browser.find_element(By.NAME, "first_name").send_keys("Test")
    browser.find_element(By.NAME, "last_name").send_keys("Testoviy")
    browser.find_element(By.NAME, "firstname").send_keys("Russia")
    browser.find_element(By.ID, "country").send_keys("Gorod")
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    time.sleep(10)
    browser.quit()

# browser.find_element(By.XPATH, '//input[@id="country"]')
# browser.find_element('[id="country"]')
# browser.find_element('#country')
# browser.find_element(By.ID, 'country')
