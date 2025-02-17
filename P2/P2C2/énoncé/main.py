# Demande à l'utilisateur de saisir une liste de nombres séparés par des virgules
nombres = input("Veuillez saisir une liste de nombres, séparés par des virgules : ")

# Convertit la chaîne de caractères en liste de chaînes de caractères
liste = nombres.split(",")

# Affiche la liste des nombres
print("Liste des nombres : ", liste)

# Convertit chaque élément de la liste (chaîne de caractères) en entier
liste_entiers = []
for nombre in liste:
    nombre_entiers = int(nombre)
    liste_entiers.append(nombre_entiers)

# Affiche la liste des nombres entiers
print("Liste des nombres entiers : ", liste_entiers)

# Calcule la somme des nombres
somme = 0
for nombre in liste_entiers:
    somme += nombre

# Affiche la somme des nombres
print("Somme des nombres : ", somme)

# Calcule la moyenne des nombres
moyenne = somme / len(liste_entiers)

# Affiche la moyenne des nombres
print("Moyenne des nombres : ", moyenne)

nombre_au_dessus_de_la_moyenne = 0

# Compte le nombre de nombres supérieurs à la moyenne
for nombre in liste_entiers:
    if nombre > moyenne:
        nombre_au_dessus_de_la_moyenne += 1

# Affiche le nombre de nombres supérieurs à la moyenne
print("Nombre de nombres supérieurs à la moyenne : ", nombre_au_dessus_de_la_moyenne)