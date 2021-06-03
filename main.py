"""
IUT-CastleQuest - Labyrinthe fait avec une turtle
Auteur: Hugo CHASSAING
Date: 01/05/2021

Mise en marche du jeu

Entrée: Import des fichiers
Résultat: Mise en fonction du jeu
"""

from createWorld import *
from playerMovement import movement

if __name__ == "__main__":
    listen()

    # Exécution de la fonction si un évenement se produit (appuyer sur les touches directionnels)
    onkeypress(movement("Left"), "Left")
    onkeypress(movement("Right"), "Right")
    onkeypress(movement("Up"), "Up")
    onkeypress(movement("Down"), "Down")

    mainloop()
