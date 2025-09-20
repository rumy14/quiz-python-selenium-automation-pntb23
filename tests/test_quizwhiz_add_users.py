import os

from views.login import LoginPage
from views.add_form import AddForm


URL = "https://ai-quizwhiz.zluck.com/login"


def test_show_add_form(driver):
    # Initialize Page Objects
    login_page = LoginPage(driver)
    add_form = AddForm(driver)

    # Open Webpage
    driver.get(URL)

    # Login
    username = "admin@gmail.com"
    password = "123456"
    login_page.login(username, password)

    add_form.click_user_button()
    add_form.click_add_user_button()
    add_form.upload_image()


