from pages.base_page import BasePage
from config.locators import LoginLocators

class LoginPage(BasePage):

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):

        self.type(LoginLocators.USERNAME, username)
        self.type(LoginLocators.PASSWORD, password)

        self.click(LoginLocators.LOGIN_BUTTON)