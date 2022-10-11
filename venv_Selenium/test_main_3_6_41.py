import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

class Test1():
    mess = ""
    pages_list = (["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1"])

    @pytest.mark.parametrize('page', pages_list)
    def test_01(self, browser, page):
        link = f"{page}/"
        browser.get(link)

        browser.implicitly_wait(10)

        input1 = browser.find_element(By.CSS_SELECTOR, ".textarea")
        input1.send_keys(str(math.log(int(time.time()))))

        # Выжидаем 10 сек что бы кнопка точно стала активной, Отправляем заполненную форму
        wait = WebDriverWait(browser, 10)
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
        button.click()

        # находим элемент, содержащий текст
        message = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.smart-hints"))).text

        if message != 'Correct!':
            mess += message
            print(mess)

        assert page == False


if __name__ == "__main__":
    pytest.main()