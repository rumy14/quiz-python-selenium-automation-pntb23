import time

from selenium import webdriver

def test_login_with_valid_admin():
    driver = webdriver.Chrome()  # 1. Open the Google Chrome

    # Maximize the browser window
    driver.maximize_window()

    driver.get("https://ai-quizwhiz.zluck.com/login")

    # getting username
    elem_username_input = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_username_input.clear()
    elem_username_input.send_keys("admin@gmail.com")

    # getting password
    elem_pass_input = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("123456")

    # click submit button
    elem_btn_login = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    elem_btn_login.click()

    # click users button / left manu button
    elem_btn_users = driver.find_element("xpath", "/html/body/div[1]/aside/nav/ul/li/ul/li[2]/a")
    elem_btn_users.click()

    driver.implicitly_wait(3)

    # user checkbox
    checkbox1 = driver.find_element("xpath", "/html/body/div[1]/div[1]/main/div/section/div/div/div/div/div/div[3]/table/tbody/tr[2]/td[1]/div/label/input")
    checkbox1.click()
    time.sleep(10)