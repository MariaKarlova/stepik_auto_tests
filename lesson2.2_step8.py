from selenium import webdriver
from selenium.webdriver.common.by import By
import os # импортируем модуль
import time

link = 'https://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, '//input[@placeholder="Enter first name"]').send_keys("Testoviy")
    browser.find_element(By.XPATH, '//input[@placeholder="Enter last name"]').send_keys("Test")
    browser.find_element(By.XPATH, '//input[@placeholder="Enter email"]').send_keys("test@gogl.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__)) # получаем путь к директории текущего исполняемого скрипта
    file_name = "test.txt" # имя файла, который будем загружать на сайт
    file_path = os.path.join(current_dir, file_name) # получаем путь к file_example.txt
    element = browser.find_element(By.ID, 'file')
    element.send_keys(file_path) # отправляем файл

    browser.find_element(By.XPATH, '//button').click()

finally:
    time.sleep(5)
    browser.quit()
