# -*-coding:utf-8-*-

from constants import *

def isintable(coord, table) :
    return coord[0] >= 0 and coord[1] >= 0 and coord[0] < len(table[0]) and coord[1] < len(table)

class Enemy :

    def __init__(self, table) :

        self.table = table

        i = 0
        for ligne in table :
            if 's' in ligne :
                self.pos = (ligne.index('s'), i)
                self.prev = self.pos
            i += 1

    def move(self) :
        directions = []
        for i in [-1, 0, 1] :
            for j in [-1, 0, 1] :
                if abs(i) != abs(j) :
                    directions.append( (self.pos[0]+i, self.pos[1]+j) )

        for i in directions :

            if isintable(i, self.table) and self.table[i[1]][i[0]].isspace() and i != self.prev :
                self.prev = self.pos
                self.pos = i
                return self.pos
            elif isintable(i, self.table) and self.table[i[1]][i[0]] == 'c' :
                return False

    def getprev(self) : return self.prev
