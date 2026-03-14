import time
from itertools import dropwhile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def summ(x, y):
    return str(x + y)

try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/selects1.html"

    browser.get(link)

    x = browser.find_element(By.ID, 'num1')
    value_str = x.text
    x = int(value_str)

    y = browser.find_element(By.ID, 'num2')
    value_str2 = y.text
    y = int(value_str2)

    res = summ(x, y)
    print(res)

    browser.find_element(By.CLASS_NAME, 'custom-select').click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(res)
    browser.find_element(By.TAG_NAME, 'button').click()


finally:
    time.sleep(10)
    browser.quit()



