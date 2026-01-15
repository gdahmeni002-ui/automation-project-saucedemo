import json
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ================= DATA =================
def load_test_data(filename):
    """Charge les données JSON"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, filename)

    if not os.path.exists(json_path):
        raise FileNotFoundError(f"JSON introuvable : {json_path}")

    with open(json_path, "r", encoding="utf-8") as file:
        return json.load(file)

#  Nouvelle fonction de test pour Pytest
def test_load_json_data():
    """Test simple pour vérifier que le fichier JSON est bien chargé"""
    data = load_test_data("test_data.json")
    assert data is not None
    assert "invalid_login" in data
    assert "missing_username" in data
    assert "missing_password" in data

# ================= NAVIGATION =================
def test_open_application(driver, url):
    driver.get(url)


# ================= LOGIN (COMMUN TEST 1 & 2) =================
def test_login(driver, username, password, locators=None):
    """Login générique. locators optionnel si tu veux garder la structure existante"""
    wait = WebDriverWait(driver, 5)
    if locators:
        wait.until(EC.presence_of_element_located((By.ID, locators["username"]))).clear()
        driver.find_element(By.ID, locators["username"]).send_keys(username)
        driver.find_element(By.ID, locators["password"]).clear()
        driver.find_element(By.ID, locators["password"]).send_keys(password)
        driver.find_element(By.ID, locators["login_button"]).click()
    else:
        # Si locators non fourni, recherche par IDs par défaut
        wait.until(EC.presence_of_element_located((By.ID, "user-name"))).clear()
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()


# ================= ERROR HANDLING (TEST 1) =================
def test_get_error_message(driver, error_css=None):
    """Récupère le texte d'erreur"""
    if not error_css:
        error_css = "h3[data-test='error']"
    return WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, error_css))
    ).text


def close_error_message(driver, close_button_id):
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, close_button_id))
    ).click()


# ================= NEW FUNCTION =================
def test_login_with_case(driver, url, case):
    """
    Fonction générique pour tester un login avec un cas du JSON.
    case = dict avec keys: username, password, expected_error
    """
    test_open_application(driver, url)
    username = case.get("username", "")
    password = case.get("password", "")
    test_login(driver, username, password)
    error_text = test_get_error_message(driver)
    assert error_text == case["expected_error"]
