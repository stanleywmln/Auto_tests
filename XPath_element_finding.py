import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("hui")

    input2 = browser.find_element(By.CSS_SELECTOR, "form > div:nth-child(2) > input")
    input2.send_keys("stanislavovich")

    input3 = browser.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Nha Trang")

    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Vietnam")

    clicking = browser.find_element(By.XPATH, "//form/div[6]/button[3]")
    clicking.click()

finally:
    time.sleep(20)
    browser.quit()

