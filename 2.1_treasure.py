from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.CSS_SELECTOR, "img[valuex]")
    x = treasure.get_attribute("valuex")   # <-- исправлено
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")  # <-- исправлено
    submit.click()

finally:
    time.sleep(10)
    browser.quit()