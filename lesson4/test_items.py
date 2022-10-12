from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_button_find(browser):
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    assert button.is_enabled, 'Not found'
