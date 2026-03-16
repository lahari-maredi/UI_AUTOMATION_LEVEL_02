import os
import pytest
import allure
from utils.driver_factory import get_driver


@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call":

        driver = item.funcargs.get("driver", None)

        if driver:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = f"screenshots/{item.name}.png"

            driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as f:
                allure.attach(
                    f.read(),
                    name=item.name,
                    attachment_type=allure.attachment_type.PNG
                )