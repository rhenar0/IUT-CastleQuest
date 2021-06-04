"""
IUT-CastleQuest - Labyrinthe fait avec une turtle
Auteur: Hugo CHASSAING
Date: 01/05/2021

Définition de la map du labyrinthe

Entrée: Fonctions et variables
Résultat: Création de la map du labyrinthe
"""

from CONFIGS import *
from parseFile import *
from turtle import *
from enum import Enum


def calculer_pas(matrice):
    """
    Calcule le pas (taille) des cases
    Entrée:
        matrice: Tuple | Table de la map
    Example: calculer_pas(matrice)
    Return: Float
    """

    y = len(matrice)
    x = len(matrice[0])

    maxX = abs(ZONE_PLAN_MINI[0]) + abs(ZONE_PLAN_MAXI[0])
    maxY = abs(ZONE_PLAN_MINI[1]) + abs(ZONE_PLAN_MAXI[1])

    return min(maxX / x, maxY / y)


def coordonnes(case, pas):
    """
    Calcule les coordonnées en pixel de la case souhaité
    Entrées:
        case: Tuple | Coordonnées de la case
        pas: Float | Le pas d'une case
    Exemple: coordonnes((4,22), pas)
    Return: Tuple
    """

    pxCoord = [ZONE_PLAN_MINI[0] + case[1] * pas, ZONE_PLAN_MAXI[1] - pas - case[0] * pas]

    return tuple(pxCoord)


def tracer_carre(dimension):
    """
    Permet de tracer une case d'une certaine dimension
    Entrée:
        dimension: Float | Dimension de la case
    Exemple: tracer_carre(15)
    """

    caseTurtle.begin_fill()

    for _ in range(4):
        caseTurtle.forward(dimension)
        caseTurtle.left(90)

    caseTurtle.end_fill()


def tracer_case(case, couleur, pas):
    """
    Préparation de la turtle au dessin de la map
    Entrées:
        case: Tuple | Coordonnées de la case
        couleur: String | Couleur de remplissage de la case
        pas: Float | Dimension de la case
    Exemple: tracer_case((1,22), "red", pas)
    """

    coord = coordonnes(case, pas)

    caseTurtle.color("white", couleur)

    caseTurtle.up()
    caseTurtle.goto(coord[0], coord[1])
    caseTurtle.down()

    tracer_carre(pas)


def afficher_plan(matrice):
    """
    Affiche la map
    Entrée:
        matrice: Tuple | Table de la map
    Example: afficher_plan([[1,0,1,1],[0,0,1,0]])
    """

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            tracer_case((i, j), COULEURS[matrice[i][j]], calculer_pas(matrice))

    update()


class Case(Enum):  # Merci Jimmy
    """
    Enumeration de la case
    Exemple: Case.DOOR.value
    """
    EMPTY = 0
    WALL = 1
    VICTORY = 2
    DOOR = 3
    OBJECT = 4


tracer(0, 0)

MAP = lire_matrice(fichier_plan)
PAS = calculer_pas(MAP)

caseTurtle = Turtle()
caseTurtle.ht()
caseTurtle.speed(10)

afficher_plan(MAP)
