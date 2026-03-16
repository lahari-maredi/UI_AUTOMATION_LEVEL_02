from pages.test_scenarios_page import ScenariosPage

def test_alerts(driver):

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    page = ScenariosPage(driver)

    page.handle_alert()
    page.handle_confirm()
    page.handle_prompt()