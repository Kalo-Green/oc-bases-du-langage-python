# Importation du module CSV pour manipuler les fichiers CSV
import csv  

def extract(filename="input.csv"):
    """
    Extrait les données du fichier CSV et les retourne sous forme de liste de dictionnaires.
    
    :param filename: Nom du fichier CSV à lire (par défaut "input.csv").
    :return: Liste de dictionnaires représentant les données du fichier CSV.
    """
    data = []
    # Ouverture du fichier en mode lecture
    with open(filename, "r") as file:  
        # Lecture du fichier sous forme de dictionnaires
        csv_reader = csv.DictReader(file)  
        # Parcours de chaque ligne du fichier
        for line in csv_reader:  
            # Ajout de la ligne (dictionnaire) à la liste
            data.append(line) 
    # Retourne la liste contenant toutes les données extraites  
    return data  

def transform(data_to_transform):
    """
    Transforme les données en calculant les salaires.

    :param data_to_transform: Liste de dictionnaires contenant les employés et leurs heures travaillées.
    :return: Liste de dictionnaires avec le nom et le salaire calculé.
    """
    data_to_load = []
    # Parcours de chaque employé
    for data in data_to_transform:  
        # Création d'un dictionnaire pour stocker les nouvelles données
        transformed_data = {} 
        # Conservation du nom de l'employé
        transformed_data["nom"] = data["nom"]  
        # Calcul du salaire (15€ de l'heure)
        transformed_data["salaire"] = int(data["heures_travaillees"]) * 15 
        # Ajout des nouvelles données transformées à la liste 
        data_to_load.append(transformed_data)  
    # Retourne la liste contenant les employés avec leurs salaires
    return data_to_load  

def load(data_to_load, filename="output.csv"):
    """
    Charge les données transformées dans un fichier CSV.

    :param data_to_load: Liste de dictionnaires contenant les employés et leurs salaires.
    :param filename: Nom du fichier CSV où enregistrer les données (par défaut "output.csv").
    """
    # Ouverture du fichier en mode écriture
    with open(filename, mode="w") as file: 
        # Définition des noms de colonnes 
        fieldnames = ["nom", "salaire"]  
        # Création de l'écrivain CSV
        writer = csv.DictWriter(file, fieldnames=fieldnames)  
        # Écriture de l'en-tête du fichier CSV
        writer.writeheader() 
        # Parcours des données transformées
        for data in data_to_load:  
            # Écriture de chaque ligne dans le fichier CSV
            writer.writerow(data) 

def main():
    """
    Fonction principale qui exécute les étapes ETL :
    1. Extraction des données depuis le fichier "input.csv".
    2. Transformation des données (calcul des salaires).
    3. Chargement des données dans le fichier "output.csv".
    """
    # Extraction des données
    data_to_transform = extract("input.csv")
    # Transformation des données  
    data_to_load = transform(data_to_transform)
    # Chargement des nouvelles données  
    load(data_to_load, "output.csv")  
    # Affichage du message de succès
    print("Le fichier salaires.csv a été généré avec succès !")

# Vérifie si le script est exécuté directement et non importé comme module
if __name__ == "__main__":
    # Exécution du programme principal
    main()