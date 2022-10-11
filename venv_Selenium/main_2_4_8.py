from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    # говорим Selenium проверять в течение 10 секунд, пока цена не станет $100
    WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
        )

    # Нажатие кнопки
    browser.find_element(By.ID, "book").click()

    # Прокрутка страницы до второй кнопки
    button = browser.find_element(By.ID, "solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Вычисление формулы

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()