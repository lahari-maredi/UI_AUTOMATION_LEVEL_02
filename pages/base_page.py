from utils.wait_utils import wait_for_element

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        wait_for_element(self.driver, locator).click()

    def type(self, locator, text):

        element = wait_for_element(self.driver, locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return wait_for_element(self.driver, locator).text