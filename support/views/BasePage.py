import conftest


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def find_el(self, locator):
        return self.driver.find_element(*locator)

    def find_els(self, locator):
        return self.driver.find_element(*locator)

    def write(self, locator, text):
        self.find_el(locator).send_keys(text)

    def to_click(self, locator):
        self.find_el(locator).click()