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
    load_json_data,
    open_application,
    login,
    get_error_message,
)

# ================= CONFIG =================
URL = "https://www.saucedemo.com"
CHROME_DRIVER_PATH = r"C:\chrome-sources\chromedriver-win64"
CHROME_PORTABLE_PATH = r"C:\chrome-sources\chrome-win64"

# ================= DRIVER (IDENTIQUE TEST 2) =================
options = Options()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)


# ================= LOAD JSON =================
data = load_json_data("login_errors_data.json")
locators = data["locators"]

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

    open_application(driver, URL)

    login(driver, locators, case["username"], case["password"])

    error_text = get_error_message(driver, locators["error_message"])
    print("Message affiché :", error_text)

    if error_text == case["expected_error"]:
        print("✅ TEST OK")
    else:
        print("❌ TEST FAILED")

driver.quit()
