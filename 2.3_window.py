from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

def calc(x):
    return math.log(abs(12 * math.sin(x)))


try:

    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, 'input_value').text
    result = calc(int(x))

    browser.find_element(By.ID, 'answer').send_keys(str(result))

    submit = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit.click()


finally:
    time.sleep(10)
    browser.quit()



