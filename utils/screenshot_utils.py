import os
from datetime import datetime

def capture_screenshot(driver, name):

    os.makedirs("reports/screenshots", exist_ok=True)

    filename = f"reports/screenshots/{name}_{datetime.now().strftime('%H%M%S')}.png"

    driver.save_screenshot(filename)

    return filename