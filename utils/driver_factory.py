from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import GRID_URL, HEADLESS


def get_driver():

    chrome_options = Options()

    if HEADLESS:
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=chrome_options
    )

    return driver