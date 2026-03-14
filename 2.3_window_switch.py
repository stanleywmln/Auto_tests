from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

def calc(x):
    return math.log(abs(12 * math.sin(x)))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    old_tab = browser.window_handles[0]

    troll_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    troll_btn.click()

    new_tab = browser.window_handles[1]

    browser.switch_to.window(new_tab)

    x = browser.find_element(By.ID, 'input_value').text
    result = calc(int(x))

    answer_field = browser.find_element(By.CSS_SELECTOR, 'input[class="form-control"]')
    answer_field.send_keys(str(result))


    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_btn.click()

finally:

    time.sleep(10)
    browser.quit()
