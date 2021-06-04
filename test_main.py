"""
IUT-CastleQuest - Labyrinthe fait avec une turtle
Auteur: Hugo CHASSAING
Date: 01/05/2021

Fichier de test des fonctions primaires à chaque push sur GitHub

Entrée: None
Résultat: None
"""

import pytest

from createWorld import calculer_pas
from createWorld import coordonnes

from parseFile import lire_matrice
from parseFile import creer_dictionnaire

from Player import cLibre
from Player import cEnd

if __name__ == "__main__":
    
    MAP = lire_matrice(fichier_plan)
    PAS = calculer_pas(MAP)
    
    coordonnes((1, 22), PAS)
    objDic = creer_dictionnaire(fichier_objets)
    
    cLibre((1, 22))
    cEnd((1, 22))
