import math, time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    link = browser.find_element(By.PARTIAL_LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()

    browser.find_element(By.TAG_NAME, "input").send_keys("Stanley")
    browser.find_element(By.NAME, "last_name").send_keys("Lynn")
    browser.find_element(By.CLASS_NAME, "form-control.city").send_keys("NewYork")
    browser.find_element(By.ID, "country").send_keys("theUS")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

