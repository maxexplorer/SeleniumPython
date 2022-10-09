from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:

    browser = webdriver.Chrome(
        executable_path="/chromedriver/chromedriver.exe"
    )

    browser.maximize_window()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    element = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    value = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(value)

    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()


except Exception as ex:
    print(ex)

finally:
    time.sleep(30)
    browser.quit()
