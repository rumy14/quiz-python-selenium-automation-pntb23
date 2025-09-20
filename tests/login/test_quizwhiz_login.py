from time import sleep

from views.login import LoginPage


URL = "https://ai-quizwhiz.zluck.com/login"


def test_login(driver):
    # Initialize Page Objects
    login_page = LoginPage(driver)

    # Open Webpage
    driver.get(URL)

    # Login
    username = "admin@gmail.com"
    password = "123456"
    login_page.login(username, password)
    sleep(5)

    login_page.verify_login()  # Verify Login Page
