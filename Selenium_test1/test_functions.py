import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ================= DATA =================
def load_json_data(json_filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, json_filename)

    if not os.path.exists(json_path):
        raise FileNotFoundError(f"JSON introuvable : {json_path}")

    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)


# ================= NAVIGATION =================
def open_application(driver, url):
    driver.get(url)


# ================= LOGIN (COMMUN TEST 1 & 2) =================
def login(driver, locators, username, password):
    wait = WebDriverWait(driver, 5)

    wait.until(EC.presence_of_element_located((By.ID, locators["username"]))).clear()
    driver.find_element(By.ID, locators["username"]).send_keys(username)

    driver.find_element(By.ID, locators["password"]).clear()
    driver.find_element(By.ID, locators["password"]).send_keys(password)

    driver.find_element(By.ID, locators["login_button"]).click()


# ================= ERROR HANDLING (TEST 1) =================
def get_error_message(driver, error_css):
    return WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, error_css))
    ).text


def close_error_message(driver, close_button_id):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, close_button_id))
    ).click()
