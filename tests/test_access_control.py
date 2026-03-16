from pages.login_page import LoginPage
from pages.users_page import UsersPage

URL = "https://the-internet.herokuapp.com/login"


def test_admin_users_access(driver):

    login = LoginPage(driver)

    login.open(URL)

    login.login("tomsmith", "SuperSecretPassword!")

    users = UsersPage(driver)

    users.open_users_page()

    assert users.users_visible()