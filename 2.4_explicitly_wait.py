import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# ждём пока цена станет 100$
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
)

# нажимаем Book
browser.find_element(By.ID, "book").click()
# решаем задачу
x = browser.find_element(By.ID, "input_value").text
browser.find_element(By.ID, "answer").send_keys(calc(x))

browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)
browser.quit()

