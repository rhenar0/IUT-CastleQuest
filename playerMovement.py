"""
IUT-CastleQuest - Labyrinthe fait avec une turtle
Auteur: Hugo CHASSAING
Date: 01/05/2021

Définition des déplacements du joueur sur le labyrinthe.

Entrée: Fonctions et variables
Résultat: Mouvement du joueur
"""

from turtle import *
from CONFIGS import *
from Player import cEnd
from Player import cLibre
from createWorld import coordonnes
from createWorld import PAS


def deplacer(position, mouvement):
    """
    Permet de déplacer le dot en fonction du mouvement donner
    Entrée:
        position: Tuple | Coordonnées du joueur
        mouvement: Tuple | Prochaine coordonnées du joueur
    Example: deplacer((1,5), (1,6))
    Returns: Tuple
    """

    if cEnd(position):
        onkeypress(None, "Left")
        onkeypress(None, "Right")
        onkeypress(None, "Up")
        onkeypress(None, "Down")

        quit()  # Fin de partie
        return None
    
    elif (cLibre(mouvement)) is True:
        charPlayer.clear()

        coordPos = coordonnes(mouvement, PAS)

        charPlayer.up()
        charPlayer.goto(coordPos[0] + PAS / 2, coordPos[1] + PAS / 2)
        charPlayer.down()
        charPlayer.dot(PAS * RATIO_PERSONNAGE, COULEUR_PERSONNAGE)

        update()

        return mouvement
    
    else:
        return position


def deplacer_droite():
    """
    Fonction de préparation de déplacement vers la droite
    Exemple: deplacer_droite()
    """

    global PLAYERPOS

    onkeypress(None, "Right")

    newPos = (PLAYERPOS[0], PLAYERPOS[1] + 1)
    PLAYERPOS = deplacer(PLAYERPOS, newPos)

    if PLAYERPOS is not None:
        onkeypress(deplacer_droite, "Right")


def deplacer_haut():
    """
    Fonction de préparation de déplacement vers le haut
    Exemple: deplacer_haut()
    """

    global PLAYERPOS

    onkeypress(None, "Up")

    newPos = (PLAYERPOS[0] - 1, PLAYERPOS[1])
    PLAYERPOS = deplacer(PLAYERPOS, newPos)

    if PLAYERPOS is not None:
        onkeypress(deplacer_haut, "Up")


def deplacer_bas():
    """
    Fonction de préparation de déplacement vers le bas
    Exemple: deplacer_bas()
    """

    global PLAYERPOS

    onkeypress(None, "Down")

    newPos = (PLAYERPOS[0] + 1, PLAYERPOS[1])
    PLAYERPOS = deplacer(PLAYERPOS, newPos)

    if PLAYERPOS is not None:
        onkeypress(deplacer_bas, "Down")


def deplacer_gauche():
    """
    Fonction de préparation de déplacement vers la gauche
    Exemple: deplacer_gauche()
    """

    global PLAYERPOS

    onkeypress(None, "Left")

    newPos = (PLAYERPOS[0], PLAYERPOS[1] - 1)
    PLAYERPOS = deplacer(PLAYERPOS, newPos)

    if PLAYERPOS is not None:
        onkeypress(deplacer_gauche, "Left")


PLAYERPOS = POSITION_DEPART

charPlayer = Turtle()
charPlayer.ht()

deplacer(POSITION_DEPART, POSITION_DEPART)
