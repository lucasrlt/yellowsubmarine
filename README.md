# Projet AMFR5 - Evolve
ROLLET Lucas, PETITJEAN Damien, GILBERT Jordan

## Présentation
Ce projet réalisé dans le cadre de l'UE de L3 LIFProjet a pour but de faire fonctionner un algorithme
génétique (évolutif) dans des environnements physiques 2D.
****
On retrouvera deux environnements physiques distincts: 

  * Une simulation de sous-marins évoluant dans une caverne. Le sous-marin a un comportement prédéfini.
    Dès que le sonar détecte un obstacle au-dessus de lui, il descend, et vice-versa.
    Les paramètres modifiés par l'algorithme sont:
      - Rayon du sonar
      - Taille du sous-marin
      - Forces sur X et sur Y

****
   * Une simulation de voitures évoluant sur un terrain escarpé.
     Les paramètres modifiés par l'algorithme sont:
       - Largeur et hauteur de la voiture
       - Taille des roues (gauche et droite)
       - Position des roues (gauche et droite)
       - Vitesse de la voiture

## Dépendances
Les dépendances suivantes sont nécessaires pour lancer le programme:
- Python3
- pygame
- pymunk
- numpy

Pour installer les dépendances (hors Python), lancez avec Pip: 
`pip3 install pygame pymunk numpy`

## Exécution du programme
Le point de départ du programme est le fichier main.py. Il se lance avec la commande `python3 main.py`.

Différents arguments de ligne de commande sont disponible pour lancer les différents modes:
- `--submarines` pour lancer le programme avec les sous-marins
- `--cars` pour lancer le programme avec les voitures
- `--console` pour lancer l'entraînement en console (disponible uniquement pour les sous-marins)
- `--trained` pour afficher le résultat d'une session d'entraînement exécutée au préalable. (combinable avec --submarines ou --cars)

## Organisation du code
L'intégralité du code source se trouve dans le dossier src/.

Dans le dossier src/cars se trouve le code générant le terrain pour l'entraînement des voitures

Dans le dossier src/submarines se trouve le code générant le terrain pour l'entraînement des sous-marins.

Dans le dossier src/genetic se trouve le code de l'algorithme génétique (généralisable et utilisable pour différents problèmes en faisant varier les paramètres du constructeur). Dans ce dossier se trouve aussi l'ancienne version de l'algorithme génétique (old.py) montrant tous les essais réalisés avant d'atteindre un résultat abouti.