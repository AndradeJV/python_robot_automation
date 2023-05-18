from selenium import webdriver
import pytest

driver: webdriver.Remote


@pytest.fixture
def setup_teardown():
    # setup

    global driver
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')

    # run test
    yield

    # teardown
    driver.quit()
