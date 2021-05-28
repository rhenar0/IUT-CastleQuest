"""
IUT-CastleQuest - Labyrinthe fait avec une turtle
Auteur: Hugo CHASSAING
Date: 01/05/2021

Mise en marche du jeu

Entrée: Import des fichiers
Résultat: Mise en fonction du jeu
"""

import pytest
from createWorld import *
from playerMovement import deplacer_bas
from playerMovement import deplacer_droite
from playerMovement import deplacer_haut
from playerMovement import deplacer_gauche

if __name__ == "__main__":
    listen()

    # Exécution de la fonction si un évenement se produit (appuyer sur les touches directionnels)
    onkeypress(deplacer_gauche, "Left") 
    onkeypress(deplacer_droite, "Right")
    onkeypress(deplacer_haut, "Up")
    onkeypress(deplacer_bas, "Down")

    mainloop()
