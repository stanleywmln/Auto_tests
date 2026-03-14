import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from registration import button

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    firstname = browser.find_element(By.CSS_SELECTOR, 'input[name="firstname"]')
    firstname.send_keys("Stanley")

    lastname = browser.find_element(By.CSS_SELECTOR, 'input[name="lastname"]')
    lastname.send_keys("Lynn")

    email = browser.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    email.send_keys("damnboy.gmail.com")

    dirPath = os.path.abspath(os.path.dirname(__file__))
    filePath = os.path.join(dirPath, 'ddl_ignore.txt')

    element = browser.find_element(By.ID, 'file')
    element.send_keys(filePath)

    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()




finally:
    time.sleep(10)
    browser.quit()