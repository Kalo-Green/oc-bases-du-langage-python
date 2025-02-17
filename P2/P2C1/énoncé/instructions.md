# Instructions  

1. Demandez à l'utilisateur de fournir **deux nombres** avec la fonction `input`.  
   * Stockez ces valeurs dans `nombre1` et `nombre2`.  

2. `nombre1` et `nombre2` sont des **chaînes de caractères** (`str`).  
   * Utilisez la fonction `isnumeric` pour vérifier que ce sont des nombres.  

3. Si ce **n'est pas le cas**, quittez le programme en générant une exception avec :  
   * `raise SystemExit("Fin du programme")`  

4. **Sinon**, convertissez les deux nombres en **nombres entiers** avec la fonction `int`.  

5. Créez une variable `operation` et utilisez `input` pour obtenir l'opération souhaitée par l'utilisateur.  

6. Vérifiez que l'opération est **valide** (`+`, `-`, `*`, `/`).  
   * **Si ce n'est pas le cas**, quittez le programme.  

7. Effectuez le **calcul** en fonction de la valeur de `operation` en utilisant `if - elif - else`, puis stockez le résultat dans la variable `resultat`.  

8. **Gestion des erreurs** :  
   * Si l'opération est une division (`/`) et que `nombre2` est **0**, quittez le programme.  
   * Utilisez la fonction `round` pour arrondir le résultat de la division et le rendre plus lisible.  

9. **Affichez** `resultat` sous la forme :  
   * `"Résultat: valeur du résultat"`  
