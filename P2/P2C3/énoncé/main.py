# Définition de la fonction salaire_mensuel()
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

# Définition de la fonction salaire_hebdomadaire()
def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

# Définition de la fonction salaire_horaire()
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

# Demander à l'utilisateur de saisir son salaire annuel et le nombre d'heures travaillées
salaire_annuel = float(input("Veuillez entrer votre salaire annuel : "))
heures_travaillees = float(input("Veuillez entrer votre nombre d'heures travaillées par semaine : " ))

# calculer le salaire horaire 
mensuel = salaire_mensuel(salaire_annuel)
hebdomadaire =  salaire_hebdomadaire(mensuel)
horraire = hebdomadaire / heures_travaillees

# Afficher le salire horraire
print("Votre salaire horaire est de : ", horraire, "euros") 