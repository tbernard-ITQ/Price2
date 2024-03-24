import requests
from bs4 import BeautifulSoup

# Remplacez 'URL_DU_SITE_WEB' par l'URL de la page contenant le prix
url = 'https://www.coolblue.be/fr/produit/888735/jura-z10-aluminium-black-ea.html'

# Utilisez Requests pour obtenir le contenu de la page
response = requests.get(url)

# Vérifiez si la requête a réussi
if response.status_code == 200:
    # Utilisez Beautiful Soup pour analyser le contenu HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Remplacez 'SELECTEUR_CSS' par le sélecteur CSS que vous avez trouvé
    # Par exemple, '.price' ou '#product-price'
    selecteur_css = 'sales-price__current'
    
    # Utilisez le sélecteur CSS pour trouver l'élément contenant le prix
    element_prix = soup.select_one(selecteur_css)
    
    # Vérifiez si l'élément a été trouvé
    if element_prix:
        # Affichez le texte de l'élément, qui devrait être le prix
        print("Prix trouvé :", element_prix.text.strip())
    else:
        print("L'élément correspondant au sélecteur CSS n'a pas été trouvé.")
else:
    print("La requête a échoué avec le code d'état :", response.status_code)
