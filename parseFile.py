"""
IUT-CastleQuest - Labyrinthe fait avec une turtle
Auteur: Hugo CHASSAING
Date: 01/05/2021

Mise en marche du jeu

Entrée: Fichier texte
Résultat: Table
"""


def lire_matrice(fichier):
    """
    Permet d'interpréter un fichier et de le mettre dans une table
    Entrée:
        fichier: String | Nom du fichier à interpréter
    Exemple: lire_matrice("plan_chateau.txt")
    Return: Table à 2 dimensions
    """

    map = []

    with open(fichier) as file:
        dataFile = file.readlines()

    for v in dataFile:
        dataInt = []
        for k in v.split():
            dataInt.append(int(k))

        map.append(dataInt)

    return map


def creer_dictionnaire(fichier_des_objets):
    """
    Permet d'interpréter un fichier et de le mettre dans une table
    Entrée:
        fichier: String | Nom du fichier à interpréter
    Exemple: creer_dictionnaire("dico_portes.txt")
    Return: Dictionnaire d'objets
    """

    dicObj = {}

    with open(fichier_des_objets, mode="r", encoding="utf-8") as file:
        dataFile = file.readlines()

        for k in dataFile:
            emp, obj = eval(k)
            dicObj[emp] = obj

    return dicObj
