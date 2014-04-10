# -*-coding:utf-8-*-
"""
Objectif : tester la classe Entity et ses méthodes
"""

from enemy import *

Schro = Enemy(0,0) # Création de Schrodinger
Schro.move() # Déplacement de Schrodinger

n = 0
while Schro.d == "right":
    # teste le nombre d'itérations pour que Schro. arrive à la fin de la ligne (x=100) et change de direction
    Schro.move()
    print(Schro.x, Schro.y) # affichage pour test
    print(Schro.d, Schro.a, Schro.v) # affichage pour test
    n += 1
print(n) # retourne le nombre d'itérations

