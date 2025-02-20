# Importation de la classe BeautifulSoup pour analyser le contenu HTML
from bs4 import BeautifulSoup

# Utilisation de BeautifulSoup4 pour extraire des informations du fichier "index.html"
# Le fichier est ouvert en mode lecture avec l'encodage UTF-8
with open("index.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")  # Création d'un objet BeautifulSoup pour analyser le HTML

# Extraction du titre de la page à partir de la balise <title>
title = soup.title.string
print("Titre de la page:", title)

# Extraction du texte de la balise <h1>
h1_text = soup.find("h1").string
print("Texte de la balise h1:", h1_text)

# Dictionnaire pour stocker les produits et leurs informations
all_products = {}

# Extraction des produits à partir des éléments <li>
products = soup.find_all("li")  # .find_all récupère tous les éléments <li> (chaque produit)

# Parcours de chaque produit dans la liste
for product in products:
    # Extraction du nom du produit à partir de la balise <h2>
    name = product.find("h2").string

    # Extraction du prix du produit à partir de la balise <p> avec la classe "price"
    price_str = product.find("p", class_="price").string
    # Séparation de la chaîne de texte du prix avec " " (espace) pour extraire le montant
    price_list = price_str.split(" ")
    # On récupère le prix (= deuxième mot) après l'espace
    all_products[name] = {"prix": price_list[1]}  # Stockage du prix dans un dictionnaire avec le nom du produit

    # La description est le dernier élément de la liste des paragraphes
    description = product.find_all("p")[-1].string  # .find_all récupère toutes les balises <p>, et on prend le dernier
    all_products[name]["description"] = description  # Ajout de la description au dictionnaire du produit

# Affichage des informations extraites pour vérifier que tout est bien récupéré
print("Produits:", all_products)

# Conversion des prix en euros vers les dollars (avec un taux de conversion fictif de 1.2)
for name in all_products.keys():
    # Récupération du prix du produit
    price_str = all_products[name]["prix"]
    # Suppression du symbole "€" du prix
    price = price_str.strip("€")  # .strip() enlève les symboles ou espaces indésirables
    # Conversion en float pour pouvoir effectuer les calculs
    price = float(price)
    # Calcul du prix en dollars avec un taux de conversion de 1.2
    dollar_price = price * 1.2
    # Enregistrement du prix en dollars dans le dictionnaire sous la clé "prix_dollar"
    all_products[name]["prix_dollar"] = f"{dollar_price}$"

# Affichage des produits avec leur prix en dollars
for name in all_products.keys():
    # Pour chaque produit, on affiche son nom et son prix en dollars
    print(f"Nom: {name}, Prix en dollars: {all_products[name]['prix_dollar']}")
