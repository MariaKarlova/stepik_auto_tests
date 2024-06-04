from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #browser.implicitly_wait(12)

    WebDriverWait(browser, 12).until(
         EC.element_to_be_clickable((By.XPATH, "//h5[text()='$100']"))
     )

    #browser.find_element(By.XPATH, "//h5[text()='$100']").click()
    browser.find_element(By.CSS_SELECTOR, '#book').click()

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    browser.execute_script("window. scrollBy(0, 800)")
    browser.find_element(By.CSS_SELECTOR, '#solve').click()

finally:
    time.sleep(10)
    browser.quit()
