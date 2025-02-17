# Demande à l'utilisateur de saisir un nombre entier et le stocke dans la variable "nombre1"
nombre1 = input("Veuillez entrer un nombre entier : ")
# Demande à l'utilisateur de saisir un nombre entier et le stocke dans la variable "nombre2"
nombre2 = input("Veuillez entrer un nombre entier : ")

# isnumeric() permet de vérifier si la chaîne de caractères est un nombre
# Si l'une des chaînes n'est pas un nombre entier, on affiche un message d'erreur et on arrête le programme
if not nombre1.isnumeric() or not nombre2.isnumeric():
    print("Erreur: les deux nombres doivent être des nombres entiers")
    raise SystemExit("Fin du programme")

# Convertit les chaînes "nombre1" et "nombre2" en entiers
nombre1 = int(nombre1)
nombre2 = int(nombre2)

# Demande à l'utilisateur de saisir l'opération mathématique qu'il souhaite effectuer
operation = input("Entrez l'opération souhaitée ['+', '-', '*' ou '/'] : ")

# Vérifie si l'opération saisie fait partie des opérations valides ['+', '-', '*', '/']
# Si l'opération n'est pas valide, affiche un message d'erreur et arrête le programme
if operation not in ["+", "-", "*", "/"]:
    print("Erreur : le symbole de l'opération souhaitée doit être '+', '-', '*' ou '/'.")
    raise SystemExit("Fin du programme")

#  Effectue le calcul correspondant, selon l'opération choisie
if operation == "+":
    resultat = nombre1 + nombre2
elif operation == "-":
    resultat = nombre1 - nombre2
elif operation == "*":
    resultat = nombre1 * nombre2
elif operation == "/":
    # Si l'opération est '/', on vérifie que 'nombre2' n'est pas égal à zéro avant de diviser
    if nombre2 == 0:
        # Si 'nombre2' est zéro, on affiche un message d'erreur et arrête le programme
        print("Erreur : la division par zéro n'est pas possible.")
        raise SystemExit("Fin du programme")
    # Effectue la division et arrondit le résultat à 2 décimales en utilisant la fonction round()
    resultat =  round(nombre1 / nombre2, 2)

# Affiche le résultat de l'opération
print(f"Résultat de l'opération {nombre1} {operation} {nombre2} : {resultat}")