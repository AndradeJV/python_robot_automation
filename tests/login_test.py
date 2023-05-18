from selenium.webdriver.common.by import By
import conftest
import pytest

from support.views.pages.LoginPage import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestLoginTest:
    def test_valid_login(self):
        driver = conftest.driver
        login_page = LoginPage()

        login_page.do_login("standard_user", "secret_sauce")

        assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed()

    def test_invalid_login(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secdret_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert not driver.find_elements(By.XPATH, "//span[@class='title']")[0].is_displayed()
