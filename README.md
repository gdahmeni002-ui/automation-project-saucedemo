# automation-project-saucedemo
Projet d'automatisation de tests pour Saucedemo.com
🧪 Selenium Test – Gestion des erreurs de connexion (SauceDemo)
📌 Objectif

Automatiser la validation des scénarios de connexion échouée sur le site
👉 https://www.saucedemo.com

en utilisant Selenium WebDriver + Pytest, avec des données de test externalisées en JSON.

Ce test correspond à un seul Test Xray (Selenium Test 1) lié à une Story Jira.

🧩 Périmètre fonctionnel couvert

Le test valide les cas suivants :

Connexion avec identifiants invalides

Connexion sans nom d’utilisateur

Connexion sans mot de passe

Vérification du message d’erreur affiché

Validation de la cohérence des données JSON

🗂️ Structure du projet
Selenium_test1/
│
├─ test_login_errors.py      # Script de test Pytest/Selenium
├─ test_functions.py         # Fonctions utilitaires Selenium
├─ login_errors_data.json    # Données de test + locators
│
test-reports/
└─ results.xml               # Rapport JUnit (optionnel – CI/Xray)

🧪 Description des fichiers
🔹 test_login_errors.py

Script principal de tests Selenium.

Technologies

Python

Selenium WebDriver (Chrome)

Pytest

Configuration

Mode headless

Mode incognito

Un navigateur par test (isolation des scénarios)

Tests implémentés
Test Pytest	Scénario
test_invalid_login	Login avec identifiants invalides
test_missing_username	Login sans username
test_missing_password	Login sans password
test_load_json_data	Validation du chargement JSON
🔹 login_errors_data.json

Fichier contenant les données de test ET les locators UI.

Sections :

locators : identifiants des éléments HTML

Cas de test :

invalid_login

missing_username

missing_password

👉 Avantages :

Pas de données codées en dur

Ajout de nouveaux cas sans modifier le code Python

Compatible Data-Driven Testing

🔹 test_functions.py

Bibliothèque de fonctions Selenium réutilisables.

Fonctions principales :

load_test_data(filename)
→ Charge et valide l’existence du fichier JSON

open_application(driver, url)
→ Ouvre l’application Saucedemo

login(driver, username, password)
→ Effectue une tentative de connexion

get_error_message(driver)
→ Récupère le message d’erreur affiché

login_with_case(driver, url, case)
→ Fonction générique qui :

ouvre l’application

exécute le login

vérifie le message d’erreur attendu

👉 Cette approche rend le test :

lisible

maintenable

réutilisable

⚙️ Prérequis techniques

Python 3.10+

Google Chrome

ChromeDriver

Dépendances Python
pytest
selenium


Installation :

pip install -r requirements.txt

▶️ Exécution des tests

Depuis la racine du projet :

pytest Selenium_test1 -v

📄 Génération d’un rapport (pour Jira / Xray)

Pour générer un rapport JUnit XML compatible Xray :

pytest Selenium_test1 -v --junitxml=test-reports/results.xml


Fichier généré :

test-reports/results.xml

🔗 Intégration Jira / Xray (manuel + automatique)
Organisation recommandée
Story
 └── Test (Xray) – Selenium Test 1
      └── Test Execution

Étapes Xray

Créer un Test (type Xray Test)

Ajouter les Test Steps :

Invalid login

Missing username

Missing password

Créer un Test Execution

Importer results.xml

Les statuts Pass / Fail sont mis à jour automatiquement

✅ Bonnes pratiques appliquées

Séparation :

Tests

Fonctions

Données

Tests indépendants

Données centralisées

Assertions explicites

Compatible CI/CD et Xray

🚀 Évolutions possibles

Paramétrisation Pytest (@pytest.mark.parametrize)

Utilisation des locators depuis le JSON

Ajout d’un hook setup/teardown

Intégration Xray via API

Rapport HTML

👤 Auteur

Automatisation Selenium – Gestion des erreurs de connexion
Projet prêt pour Git + Jira + Xray

👉 Prochaine étape possible

Si tu veux, je peux :

traduire ce README en format Jira Test Steps

te dire exactement quoi mettre dans chaque champ Xray

aligner noms des tests Pytest ↔ Tests Jira

préparer le mapping Xray auto (import XML)
