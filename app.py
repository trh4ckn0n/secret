import streamlit as st
import requests
from bs4 import BeautifulSoup

# Fonction pour scraper les informations des opérations Anonymous
def get_anonymous_operations():
    # Exemple de scraping sur un site web fictif ou réel (modifier l'URL en fonction de la source)
    url = 'https://example.com/anonymous-operations'  # Remplacer par l'URL réelle

    # Envoi de la requête HTTP et récupération du contenu
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Exemple de récupération de données (adapter en fonction de la structure HTML du site)
    operations = []
    for operation in soup.find_all('div', class_='operation'):  # Adapter selon la structure du site
        title = operation.find('h3').text.strip()
        description = operation.find('p').text.strip()
        operations.append({
            'title': title,
            'description': description
        })
    
    return operations

# Configuration de la page Streamlit
st.set_page_config(page_title="Opérations Anonymous", page_icon="🕵️")

# Affichage du titre
st.title("Opérations Anonymous en cours")
# Injecter du CSS dans la page Streamlit
st.markdown(
    """
    <style>
        body {
            background-color: #111;
            color: #fff;
            font-family: 'Courier New', Courier, monospace;
        }
        .stButton>button {
            background-color: #FF0000;
            color: white;
            border: 2px solid #FF0000;
            border-radius: 10px;
            font-size: 18px;
            padding: 10px 20px;
            box-shadow: 0 0 15px rgba(255, 0, 0, 0.5);
        }
        .stButton>button:hover {
            background-color: #ff6666;
        }
        h1, h3, p {
            font-family: 'Special Elite', cursive;
            text-align: center;
        }
        .operation {
            padding: 20px;
            margin-bottom: 10px;
            background-color: #222;
            border-radius: 8px;
            border: 2px solid #FF0000;
        }
    </style>
    """, unsafe_allow_html=True)
# Affichage dynamique des opérations
operations = get_anonymous_operations()

if operations:
    for op in operations:
        st.subheader(op['title'])
        st.write(op['description'])
        st.markdown('---')  # Séparateur
else:
    st.warning("Aucune opération en cours trouvée.")
