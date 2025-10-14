
import time

from selenium import webdriver

def test_login_with_valid_admin():
    driver = webdriver.Chrome()  # 1. Open the Google Chrome

    driver.get("https://ai-quizwhiz.zluck.com/login")
    elem_username_input = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_username_input.clear()
    elem_username_input.send_keys("")

    # getting password
    elem_pass_input = driver.find_element("xpath", "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("")

    # click submit button
    elem_btn_login = driver.find_element("xpath", "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    elem_btn_login.click()

    time.sleep(10)
