from selenium.webdriver.common.by import By

class LoginLocators:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR = (By.ID, "flash")

class AlertLocators:

    ALERT_BUTTON = (By.XPATH, "//button[text()='Click for JS Alert']")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Click for JS Confirm']")
    PROMPT_BUTTON = (By.XPATH, "//button[text()='Click for JS Prompt']")
    RESULT = (By.ID, "result")

class FrameLocators:

    IFRAME = (By.ID, "mce_0_ifr")

class WindowLocators:

    NEW_TAB = (By.LINK_TEXT, "Click Here")