from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

# Disable Selenium Manager - requires external chromedriver
os.environ["SE_DISABLE_BROWSER_DOWNLOAD"] = "true"

from test_functions import (
    test_load_json_data,
    test_open_application,
    test_login,
    test_get_error_message,
)

# ================= CONFIG =================
URL = "https://www.saucedemo.com"
CHROME_DRIVER_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
CHROME_PORTABLE_PATH = r"C:\ProgramData\chocolatey\lib\chromedriver\tools\chromedriver.exe"

# ================= DRIVER (IDENTIQUE TEST 2) =================
options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)


# ================= LOAD JSON =================
def test_load_json_data():
    data = load_test_data("test_data.json")
    assert data is not None

test_cases = [
    data["invalid_login"],
    data["missing_username"],
    data["missing_password"]
]

# ================= TEST =================
for case in test_cases:
    print("\n" + "=" * 60)
    print("TEST :", case["expected_error"])
    print("=" * 60)

    test_open_application(driver, URL)

    test_login(driver, locators, case["username"], case["password"])

    error_text = test_get_error_message(driver, locators["error_message"])
    print("Message affiché :", error_text)

    if error_text == case["expected_error"]:
        print("✅ TEST OK")
    else:
        print("❌ TEST FAILED")

driver.quit()
