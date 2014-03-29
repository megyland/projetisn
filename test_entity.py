# -*-coding:utf-8-*-
"""
Objectif : tester la classe Entity et ses méthodes
"""

from entity import *

Schro = Entity("ennemy",0,0) # Création de Schrodinger
Schro.move() # Déplacement de Schrodinger

n = 0
while Schro.d == "right":
    # teste le nombre d'itérations pour que Schro. arrive à la fin de la ligne (x=100) et change de direction
    Schro.move()
    n += 1
print(n) # retourne le nombre d'itérations

