import os
from time import sleep
from selenium.webdriver.common.by import By


class AddForm:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, "data.email").clear()
        self.driver.find_element(By.ID, "data.email").send_keys(username)
        sleep(1)

    def enter_password(self, password):
        self.driver.find_element(By.ID, "data.password").clear()
        self.driver.find_element(By.ID, "data.password").send_keys(password)
        sleep(1)

    def click_login_btn(self):
        self.driver.find_element(By.XPATH, "/html/body/div[3]/div/main/div/div[2]/div[2]/div/form/div[2]/div/button").click()
        sleep(1)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_btn()
        sleep(1)

    def verify_login(self):
        text = self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/div/header/div/div/a[2]").text
        assert text == "QuizWhiz AI", f"Expected 'QuizWhiz AI', but got {text}"
        sleep(3)

    def click_user_button(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/aside/nav/ul/li/ul/li[2]").click()
        sleep(1)

    def click_add_user_button(self):
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/main/div/section/header/div[2]/div/a").click()
        sleep(1)

    def upload_image(self):
        upload_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "abc.png"))



        file_input = self.driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(upload_file)
        sleep(10)