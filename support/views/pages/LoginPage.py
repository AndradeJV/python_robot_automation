from selenium.webdriver.common.by import By
from support.views.BasePage import BasePage
import conftest


class LoginPage(BasePage):
    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def do_login(self, username, password):
        self.write(self.username_field, username)
        self.write(self.password_field, password)
        self.to_click(self.login_button)
