from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ввод значения имя в поле
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys('Konstantin')

    # Ввод значения фамилия в поле
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input1.send_keys('Lee')

    # Ввод значения почта в поле
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input1.send_keys('Lee@ww.com')

    # Загрузка файла 12.txt
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '12.txt')
    # print(current_dir)
    # print(file_path)
    element = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
    element.send_keys(file_path)
    #
    #
    #
    # Нажатие кнопки button
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
