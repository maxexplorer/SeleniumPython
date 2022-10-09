from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome(
        executable_path="/chromedriver/chromedriver.exe"
    )
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button.btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    value = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(value)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


except Exception as ex:
    print(ex)

finally:
    time.sleep(30)
    browser.quit()