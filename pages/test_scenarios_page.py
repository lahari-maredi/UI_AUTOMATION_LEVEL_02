from pages.base_page import BasePage
from config.locators import AlertLocators

class ScenariosPage(BasePage):

    def handle_alert(self):

        self.click(AlertLocators.ALERT_BUTTON)

        alert = self.driver.switch_to.alert
        alert.accept()

    def handle_confirm(self):

        self.click(AlertLocators.CONFIRM_BUTTON)

        alert = self.driver.switch_to.alert
        alert.dismiss()

    def handle_prompt(self):

        self.click(AlertLocators.PROMPT_BUTTON)

        alert = self.driver.switch_to.alert
        alert.send_keys("Hello")

        alert.accept()