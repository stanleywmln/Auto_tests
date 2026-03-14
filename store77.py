# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# link = "https://store77.net/apple_iphone_15_2/"
#
# browser = webdriver.Chrome()
# browser.set_window_size(1440, 900)  # desktop версия для hover
# browser.get(link)
#
# wait = WebDriverWait(browser, 10)
# actions = ActionChains(browser)
#
# try:
#     # Шаг 1 — КЛИК
#     step1 = wait.until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "button.toggle_menu.viz_menu_big"))
#     )
#     step1.click()
#
#     # Шаг 2 — НАВЕДЕНИЕ
#     step2 = wait.until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR, "div.middle_menu > div > ul > li:nth-child(1) > div > a"))
#     )
#     actions.move_to_element(step2).perform()
#
#     # Шаг 3 — НАВЕДЕНИЕ
#     step3 = wait.until(
#         EC.visibility_of_element_located((By.CSS_SELECTOR,
#                                           "div.middle_menu > div > ul > li:nth-child(1) > ul > li:nth-child(2) > div.bli_pos_second > a"))
#     )
#     actions.move_to_element(step3).perform()
#
#     step4 = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'full_menu_block')]//a[contains(text(),'Mac')]"))
#     )
#     step4.click()
#
# finally:
#     time.sleep(10)
#     browser.quit()


people = [{"name": "stan", "age": 34}, {"name": "goddamn", "age": 34}]

for i in people:
    if i["name"].startswith("s"):
        print(i)