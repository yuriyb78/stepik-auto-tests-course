from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #ищем числа для сложения
    x_element = browser.find_element_by_css_selector("#num1")
    x = int(x_element.text)
    y_element = browser.find_element_by_css_selector("#num2")
    y = int(y_element.text)
    z=str(x+y)
    

    #выбираем из ниспадающего списка ответ
    select=Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(z)
        
   
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
