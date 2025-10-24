
import time

from selenium import webdriver

def test_login_with_valid_admin():
    driver = webdriver.Chrome()  # 1. Open the Google Chrome

    driver.maximize_window()

    driver.get("https://ai-quizwhiz.zluck.com/login")
    elem_username_input = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_username_input.clear()
    elem_username_input.send_keys("admin@gmail.com")

    # getting password
    elem_pass_input = driver.find_element("xpath",
                                          "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("123456")

    # click submit button
    elem_btn_login = driver.find_element("xpath",  "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    elem_btn_login.click()

    driver.implicitly_wait(3)

    # click users button / left manu button
    elem_btn_users = driver.find_element("xpath", "/html/body/div[1]/aside/nav/ul/li/ul/li[2]/a")
    elem_btn_users.click()

    driver.implicitly_wait(3)

    elem_btn_new_users = driver.find_element("xpath", "/html/body/div[1]/div[1]/main/div/section/header/div[2]/div")
    assert (elem_btn_new_users.is_displayed() == True)

    # input name
    elem_name = driver.find_element("id","data.name")
    elem_name.send_keys("Md.Zafor")

    # input email
    elem_email = driver.find_element("xpath","/html/body/div[1]/div[1]/main/div/section/div/div/form/div[1]/div/section/div/div/div/div[2]/div/div/div[2]/div/div/input")
    elem_email.send_keys("admin@gmail.com")
    # elem_email_input.clear()

    # input password
    elem_pass = driver.find_element("xpath","/html/body/div[1]/div[1]/main/div/section/div/div/form/div[1]/div/section/div/div/div/div[3]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass.send_keys("123456")

    # input confirm password
    elem_confirm_pass = driver.find_element("xpath","/html/body/div[1]/div[1]/main/div/section/div/div/form/div[1]/div/section/div/div/div/div[4]/div/div/div[2]/div/div[1]/input")
    elem_confirm_pass.send_keys("123456")


    time.sleep(10)
