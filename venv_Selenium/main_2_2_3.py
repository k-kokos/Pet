from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1_element = browser.find_element(By.CSS_SELECTOR, '#num1')
    x1 = x1_element.text

    x2_element = browser.find_element(By.CSS_SELECTOR, '#num2')
    x2 = x2_element.text

    sum = int(x1) + int(x2)
    sum = str(sum)

    select = Select(browser.find_element(By.TAG_NAME, "select")) # Выбор из выпадающего окна
    select.select_by_value(str(sum)) # Выбор определенного параметра из выпадающего окна


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
