import pytest
from pages.login_page import LoginPage

URL = "https://the-internet.herokuapp.com/login"


def test_valid_admin_login(driver):

    login = LoginPage(driver)

    login.open(URL)

    login.login("tomsmith", "SuperSecretPassword!")

    assert "secure" in driver.current_url


@pytest.mark.parametrize("user,password",[

("wrong","SuperSecretPassword!"),
("tomsmith","wrong"),
("","")

])

def test_invalid_login(driver,user,password):

    login = LoginPage(driver)

    login.open(URL)

    login.login(user,password)

    assert "login" in driver.current_url