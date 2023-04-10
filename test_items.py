from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button(browser: WebDriver):
    browser.get(link)
    assert browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket"), "button not found"