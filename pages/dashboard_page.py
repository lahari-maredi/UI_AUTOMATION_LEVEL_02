from pages.base_page import BasePage

class DashboardPage(BasePage):

    def is_dashboard_loaded(self):

        return "secure" in self.driver.current_url