import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    step3 = browser.find_element(By.ID, "answer")
    step3.send_keys(y)

    step4 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    step4.click()

    step5 = browser.find_element(By.CSS_SELECTOR, "label[for='robotsRule']")
    step5.click()

    submitting = browser.find_element(By.CSS_SELECTOR, "form > button")
    submitting.click()

finally:
    time.sleep(10)
    browser.quit()


