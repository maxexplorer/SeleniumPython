from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"


try:
    browser = webdriver.Chrome(
        executable_path="/chromedriver/chromedriver.exe")
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure").get_attribute("valuex")
    x = x_element
    y = calc(x)

    input_value = browser.find_element(By.CSS_SELECTOR, "#answer")
    input_value.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option1 = browser.find_element(By.CSS_SELECTOR, "[value=robots]")
    option1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
