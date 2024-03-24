from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Remplacez 'CHEMIN_DU_PILOTE' par le chemin de votre pilote Chrome
service = Service(executable_path='/usr/local/bin/chromedriver')

# Initialisez le navigateur avec l'instance de service
navigateur = webdriver.Chrome(service=service)

try:
    # Votre code pour ouvrir l'URL et extraire les données
    navigateur.get('https://www.coolblue.be/fr/produit/888735/jura-z10-aluminium-black-ea.html')
    element_prix = WebDriverWait(navigateur, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".sales-price__current"))
    )
    print("Prix trouvé :", element_prix.text)
finally:
    navigateur.quit()
