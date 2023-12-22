# Intelligence Artificielle: Othello

## Description

Ce projet est l'aboutissement des TD d'IA et présente le code d'une IA qui permet de jouer contre un joueur au jeu Reversi Othello de taille 10*10.

## Fonctionnalités

- IA vs Random moves
- IA vs Player
- IA vs IA
- Statistiques De IA vs Random moves
- Iterartive deepening

## Installation

Installer termcolor, Pour des raison d'esthtétisme avec la commande: 
    `python3 -m pip install --upgrade termcolor`

## Utilisation

Les différentes parties du projets sont codées dans des fichiers distincts.
Pour choisir ce que l'on veut jouer comme type de partie il suffit d'éxécuter la commande suivante:
    `python3 Select_game.py`
Il sera proposé les différentes options de jeu et même une fonction de statistique pour tester une IA contre Random move.
Attention lorsque l'on joue une partie contre l'IA, il faut absolument jouer un coup proposé dans la liste, sinon le programme plante :(


## Notes

Le fichier Heuristique.py contient plusieurs heuristiques qui sont plus ou moins performantes, celle qui nous a donné les meilleurs résultats est hMobAndCo qui prend en compte la mobilité est l'occupation des coins. On parle ici de résultats > 80% de réussite contre des randoms moves et comme étant l'heuristique gagnant a coup sur contre les autres heuristiques a une profondeur 2. Il est possible de tester les différentes heuristiques. Les heuristiques apparaissant en vert sont les meilleurs, en rouge les moins bonne. Celles en jaune ou en blanc sont un peu bancales et celles en mauve sont vraiment pas bonnes.

