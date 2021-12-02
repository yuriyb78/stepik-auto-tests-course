from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #поиск значения Х и вычисление функции
    x_element = browser.find_element_by_css_selector("#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    # заполняем поле ввода, выбор чек бокса и радиоботтон
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    check1 = browser.find_element_by_id("robotCheckbox")
    check1.click()
    radio1 = browser.find_element_by_id("robotsRule")
    radio1.click()
    
   
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
