from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(
        executable_path="/chromedriver/chromedriver.exe")
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    sum_nums = str(int(num1) + int(num2))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum_nums)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
