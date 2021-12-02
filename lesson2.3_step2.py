from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #нажатие на кнопку на первой странице
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

    #нажате на ОК в аллерте
    alert = browser.switch_to.alert
    alert.accept()

    #поиск значения Х и вычисление функции
    x_element = browser.find_element_by_css_selector("#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    # заполняем поле ввода, выбор чек бокса и радиоботтон
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)  
   
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
