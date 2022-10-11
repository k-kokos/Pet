from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажатие кнопки button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Переключение на модальное окно Confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # Находим значение X
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    # Вычисляем значение по формуле
    y = calc(x)

    # Ввод найденного по формуле значения в поле
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    # Нажатие кнопки button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()