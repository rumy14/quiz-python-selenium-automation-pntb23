from time import sleep

from views.login import LoginPage
from views.users.add_form import AddForm


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
    name = "Mr. Rumy"
    add_form.enter_name_input(name)
    add_form.enter_email_input("rumy103040@gmail.com")
    add_form.enter_password_input("123456")
    add_form.enter_confirm_password_input("123456")


