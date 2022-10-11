from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    x = int(x)
    y = calc(x)


    # Ввод значения y  в поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Прокрутка страницы до кнопки button
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Установка галки
    chois1 = browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]')
    chois1.click()

    #Установка радиобаттон
    chois2 = browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]')
    chois2.click()

    # Отправляем заполненную форму

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
