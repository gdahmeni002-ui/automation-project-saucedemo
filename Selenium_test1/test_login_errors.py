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
from test_functions import load_test_data
data = load_test_data("test_data.json")

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
def test_invalid_login():
    case = data["invalid_login"]

    test_open_application(driver, URL)
    test_login(driver, locators, case["username"], case["password"])

    error_text = test_get_error_message(driver, locators["error_message"])
    assert error_text == case["expected_error"]
driver.quit()
def test_missing_username():
    driver = create_driver()
    case = data["missing_username"]

    test_open_application(driver, URL)
    test_login(driver, case.get("username", ""), case["password"])
    error_text = test_get_error_message(driver)
    assert error_text == case["expected_error"]

    driver.quit()


def test_missing_password():
    driver = create_driver()
    case = data["missing_password"]

    test_open_application(driver, URL)
    test_login(driver, case["username"], case.get("password", ""))
    error_text = test_get_error_message(driver)
    assert error_text == case["expected_error"]

    driver.quit()
