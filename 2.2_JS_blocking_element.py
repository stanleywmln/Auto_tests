import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calcu(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/execute_script.html")

    x = browser.find_element(By.ID, "input_value").text
    answer = calcu(x)

    input_field = browser.find_element(By.ID, "answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", input_field)
    input_field.send_keys(answer)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    button = browser.find_element(By.CLASS_NAME, "btn-primary")
    button.click()

finally:
    time.sleep(10)
    browser.quit()