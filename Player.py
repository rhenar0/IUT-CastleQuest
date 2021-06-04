"""
IUT-CastleQuest - Labyrinthe fait avec une turtle
Auteur: Hugo CHASSAING
Date: 01/05/2021

Définition du joueur et de ses fonctions.

Entrée: Fonctions et variables
Résultat: Mouvement du joueur
"""

from CONFIGS import *
from turtle import *
from parseFile import creer_dictionnaire
from createWorld import tracer_case
from createWorld import MAP
from createWorld import PAS
from createWorld import Case


def cLibre(emp):
    """
    Permet de savoir si une case est vide ou pas
    Entrée:
        emp: Tuple | Nombre de celulles
    Exemple: cLibre((1, 22))
    Return: Boolean
    """

    enumCase = MAP[emp[0]][emp[1]]

    if enumCase == Case.EMPTY.value:
        return True

    if enumCase == Case.VICTORY.value:
        END()
        return True

    if enumCase == Case.DOOR.value:

        if poser_question(emp):
            return True
        return False

    elif enumCase == Case.OBJECT.value:
        ramasser_objet(emp)
        return True

    else:
        return False


def cEnd(emp):
    """
    Permet de savoir si la case actuelle est empe de la victoire
    Entrée:
        emp: Tuple | Coordonnées de la case
    Exemple: cEnd((1, 22))
    Return: Boolean
    """

    if MAP[emp[0]][emp[1]] == Case.VICTORY.value:
        return True
    return False


def ramasser_objet(emp):
    """
    Permet de ramasser un objet, de l'afficher et de le faire apparaître à l'écran
    emp: Tuple | Coordonnéees de la case
    Example: ramasser_objet((1, 22))
    """

    global INVSTATUS

    inventaire.up()
    inventaire.goto(posInv[0], posInv[1] - 15 * INVSTATUS)
    inventaire.down()
    inventaire.write("N°" + str(INVSTATUS + 1) + ": " + objDic[emp], font=("Verdana", 10, "normal"))

    annonce.clear()
    annonce.write("Vous venez de trouver: " + objDic[emp], font=("Verdana", 12, "bold"))

    INVSTATUS += 1

    tracer_case(emp, COULEUR_CASES, PAS)
    MAP[emp[0]][emp[1]] = 0


def poser_question(case):
    """
    Permet de poser une question au joueur
    Entrée:
        case: Tuple | Coordonnées de la case
    Exemple: poser_question((1, 22))
    Return: Boolean
    """

    annonce.clear()
    annonce.write("Cette porte est fermée.", font=("Verdana", 12, "bold"))

    reponse = textinput("Porte", questDic[case][0])
    listen()

    if reponse == questDic[case][1]:
        tracer_case(case, COULEUR_CASES, PAS)
        MAP[case[0]][case[1]] = 0

        annonce.clear()
        annonce.write("Ouverture de la porte !", font=("Verdana", 12, "bold"))

        return True
    annonce.clear()
    annonce.write("Et non...", font=("Verdana", 12, "bold"))

    return False


def END():
    """
    Annonce la réussite
    Exemple: END()
    """
    
    annonce.clear()
    annonce.write("Félicitation, vous êtes venus à bout de ce quiz !", font=("Verdana", 12, "bold"))


questDic = creer_dictionnaire(fichier_questions)

INVSTATUS = 0

annonce = Turtle()
annonce.ht()
annonce.up()
annonce.goto(POINT_AFFICHAGE_ANNONCES[0], POINT_AFFICHAGE_ANNONCES[1])
annonce.down()

inventaire = Turtle()
inventaire.ht()
inventaire.up()
inventaire.goto(POINT_AFFICHAGE_INVENTAIRE[0], POINT_AFFICHAGE_INVENTAIRE[1])
inventaire.down()
inventaire.write("Inventaire", font=("Verdana", 10, "bold"))

posInv = (POINT_AFFICHAGE_INVENTAIRE[0], POINT_AFFICHAGE_INVENTAIRE[1] - 15)
objDic = creer_dictionnaire(fichier_objets)
