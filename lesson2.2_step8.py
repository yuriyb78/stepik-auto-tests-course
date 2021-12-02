from selenium import webdriver
import time
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем полz ввода
    input1 = browser.find_element_by_css_selector(".form-group [name=firstname]")
    input1.send_keys("Test")
    input2 = browser.find_element_by_css_selector(".form-group [name=lastname]")
    input2.send_keys("Test")
    input3 = browser.find_element_by_css_selector(".form-group [name=email]")
    input3.send_keys("Test@test.test")
   
    #добавляем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла
    print (file_path)
    element = browser.find_element_by_id("file")
    #element.click()
    element.send_keys(file_path)
    
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
