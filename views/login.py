from time import sleep
from selenium.webdriver.common.by import By


class LoginPage:
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