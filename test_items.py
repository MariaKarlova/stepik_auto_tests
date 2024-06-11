from selenium.webdriver.common.by import By
import time
link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_goods_has_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(5)
    button1 = browser.find_element(By.CSS_SELECTOR, '.btn-add-to-basket')
    assert button1, 'Нет кнопки добавления товара'