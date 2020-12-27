Nicolas Rodrigues Dimitri Didier
--------------------------------------
Tout d'abord notre joueur utilise l'algorithme Negalphabeta en profondeur 3 pour parcourir l'abre des jeux.

L'heuristique que nous utilisons est la différence entre le nombre de jetons noirs et de jetons blancs
ainse que le nombre de liberté autour de nos jetons.

Pour cela nous avons d'abord fait la fonction "capture_diff()" qui permet de calculer la différence de jetons
selon notre couleur. Cette fonction est donc utiliser par notre Negalphabeta appelé "negalpha_best_result()"
qui va donc chercher les meilleurs coup selon notre heuristique et renvoyer donc une liste de coups avec
la meilleur heuristique. Ensuite la fonction "get_liberty()" va prendre la liste des meilleur coup en 
paramètre et ne renvoyer que la liste des coups qui permettent d'obtenir le plus de liberté et pour finir
la fonction "getPlayerMove()" va choisir un des coup de la liste renvoyer.
