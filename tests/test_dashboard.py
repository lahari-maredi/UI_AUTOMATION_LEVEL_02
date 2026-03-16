from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

URL = "https://the-internet.herokuapp.com/login"


def test_dashboard_load(driver):

    login = LoginPage(driver)

    login.open(URL)

    login.login("tomsmith", "SuperSecretPassword!")

    dashboard = DashboardPage(driver)

    assert dashboard.is_dashboard_loaded()