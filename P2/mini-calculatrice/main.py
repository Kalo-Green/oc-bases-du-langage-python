# Fonction qui affiche un message de bienvenue
def print_welcome_message():
    print("Bienvenue sur la mini-calculatrice !")

# Fonction qui demande à l'utilisateur d'entrer deux nombres et les retourne sous forme de float
def input_two_number():
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    return num1, num2

# Fonction qui affiche un menu et récupère le choix de l'utilisateur
def print_menu_and_get_choice():
    print("=== MENU ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    # Demande le choix de l'utilisateur
    user_choice = input("Entrez votre choix (1-4) : ")

    # Vérifie que l'utilisateur entre un choix valide (1 à 4)
    while user_choice not in ["1", "2", "3", "4"]:
        user_choice = input("Choix invalide. Entrez votre choix (1-4) : ")

    return user_choice

# Fonction qui effectue une addition entre deux nombres
def sum(a, b):
    return a + b

# Fonction qui effectue une soustraction entre deux nombres
def substraction(a, b):
    return a - b

# Fonction qui effectue une multiplication entre deux nombres
def multiplication(a, b):
    return a * b

# Fonction qui effectue une division entre deux nombres avec une vérification pour éviter la division par zéro
def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Erreur : division par zéro")

# Fonction principale qui exécute le calcul en fonction du choix de l'utilisateur
def run_calculation(user_choice):
    num1, num2 = input_two_number()  # Récupère les deux nombres saisis par l'utilisateur

    # Utilisation de 'match-case' pour exécuter l'opération choisie
    match user_choice:
        case '1':
            result = sum(num1, num2)
        case '2':
            result = substraction(num1, num2)
        case '3':
            result = multiplication(num1, num2)
        case '4':
            result = division(num1, num2)
        case _:
            print("Choix invalide.")

    return result  # Retourne le résultat du calcul

# Point d'entrée du script : exécute les fonctions dans le bon ordre
if __name__ == '__main__':
    print_welcome_message()  # Affiche le message de bienvenue
    user_choice = print_menu_and_get_choice()  # Récupère le choix de l'utilisateur
    result = run_calculation(user_choice)  # Exécute l'opération choisie

    # Affiche le résultat du calcul si celui-ci est valide (évite d'afficher None en cas de division par zéro)
    if result is not None:
        print("Résultat :", result)
