from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, '//button').click()
    browser.switch_to.window(browser.window_handles[1]) #Переход на новую вкладку браузера

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.XPATH, '//button').click()

finally:
    time.sleep(5)
    browser.quit()
