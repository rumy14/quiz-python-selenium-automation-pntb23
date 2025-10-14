
import time

from selenium import webdriver

def test_login_with_valid_admin():
    driver = webdriver.Chrome()  # 1. Open the Google Chrome

    driver.get("https://ai-quizwhiz.zluck.com/login")
    elem_username_input = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/div/div/input")
    elem_username_input.clear()
    elem_username_input.send_keys("sadmin@gmail.com")

    # getting password
    elem_pass_input = driver.find_element("xpath",
                                          "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div[2]/div/div[1]/input")
    elem_pass_input.clear()
    elem_pass_input.send_keys("123456")

    # click submit button
    elem_btn_login = driver.find_element("xpath",
                                         "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button")
    elem_btn_login.click()

    driver.implicitly_wait(3)

    # click users button / left manu button
    elem_btn_users = driver.find_element("xpath", "/html/body/div[1]/aside/nav/ul/li/ul/li[2]/a")
    elem_btn_users.click()

    driver.implicitly_wait(3)

    elem_btn_new_users = driver.find_element("xpath", "/html/body/div[1]/div[1]/main/div/section/header/div[2]/div")
    assert (elem_btn_new_users.is_displayed() == True)

    # Error message verify
    text_error_message_for_wrong_email = driver.find_element("xpath","/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div[2]/p"
                                                             ).text

    # Assert the expected error message
    assert text_error_message_for_wrong_email == "These credentials do not match our records.", f"Expected 'These credentials do not match our records.', but got {text_error_message_for_wrong_email}"
    time.sleep(3)
    driver.quit()


    time.sleep(10)
