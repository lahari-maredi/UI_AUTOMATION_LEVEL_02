from pages.base_page import BasePage

class UsersPage(BasePage):

    def open_users_page(self):

        self.driver.get("https://the-internet.herokuapp.com/secure")

    def users_visible(self):

        return "Secure Area" in self.driver.page_source