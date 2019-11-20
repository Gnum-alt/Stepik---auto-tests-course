from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    x_element = browser.find_element_by_css_selector(".form-group #input_value")
    x = x_element.text
    y = calc(x) 
    
    input = browser.find_element_by_css_selector(".form-group .form-control")
    input.send_keys(y)

    option1 = browser.find_element_by_css_selector('[for="robotCheckbox"]')
    option1.click()

    option2 = browser.find_element_by_css_selector('[for="robotsRule"]')
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()