import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})

@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(
        executable_path="C:/Users/Макс/PycharmProjects/SeleniumPython/chromedriver/chromedriver.exe",
        options=options
    )
    yield browser
    print("\nquit browser..")
    browser.quit()
