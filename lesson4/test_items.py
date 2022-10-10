from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"


def test_button_find(browser):
    browser.get(link)
    button = browser.find_elements(By.TAG_NAME, "button")
    assert button is not None, 'Not found'
