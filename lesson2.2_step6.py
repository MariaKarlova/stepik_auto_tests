from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'https://SunInJuly.github.io/execute_script.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    browser.find_element(By.XPATH, '//button').click()

finally:
    time.sleep(5)
    browser.quit()
