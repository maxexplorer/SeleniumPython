import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(
        executable_path="/chromedriver/chromedriver.exe"
    )
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('pytest', ["https://stepik.org/lesson/236895/step/1",
                                    "https://stepik.org/lesson/236896/step/1",
                                    "https://stepik.org/lesson/236897/step/1",
                                    "https://stepik.org/lesson/236898/step/1",
                                    "https://stepik.org/lesson/236899/step/1",
                                    "https://stepik.org/lesson/236903/step/1",
                                    "https://stepik.org/lesson/236904/step/1",
                                    "https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, pytest):
    link = pytest
    browser.get(link)
    browser.implicitly_wait(15)
    input_text_area = browser.find_element(By.TAG_NAME, "textarea")
    answer = math.log(int(time.time()))
    input_text_area.send_keys(answer)
    button = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button.click()

    feedback_text = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint")

    assert "Correct!" in feedback_text.text



if __name__ == '__main__':
    pytest.main()