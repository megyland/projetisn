# -*-coding:utf-8-*-

from constants import *

def isintable(coord, table) :
    return coord[0] >= 0 and coord[1] >= 0 and coord[0] < len(table[0]) and coord[1] < len(table)

class Enemy :

    def __init__(self, table) :

        self.table = table
        self.unmoving = 0
        self.disturbed = False

        i = 0
        for ligne in table :
            if 's' in ligne :
                self.pos = (ligne.index('s'), i)
                self.prev = self.pos
            i += 1

    def move(self) :
        if self.unmoving :
            self.unmoving -= 1
            self.prev = self.pos
            return self.pos
        else :
            directions = []
            for i in [-1, 0, 1] :
                for j in [-1, 0, 1] :
                    if abs(i) != abs(j) :
                        directions.append( (self.pos[0]+i, self.pos[1]+j) )

            for i in directions :

                if isintable(i, self.table) and self.table[i[1]][i[0]].isspace() and (i != self.prev or self.disturbed) :
                    self.prev = self.pos
                    self.pos = i
                    self.setstatus(self.table[i[1]-1][i[0]])
                    return self.pos
                elif isintable(i, self.table) and self.table[i[1]][i[0]] == 'c' :
                    return False

    def getprev(self) : return self.prev

    def setstatus(self,trap) :
        if trap == ";" : # Erreur de calcul => Immobilise un certain temps (durée moyenne)
            self.unmoving = 2
        elif trap == "!" : # Exp. ratée => Immobilise un certain temps (long)
            self.unmoving = 3
        elif trap == "*" or trap == "4" : # Exp. intéressante => Immobilise un certain temps (court)
            self.unmoving = 1
        elif trap == "?" : # Exp. intéressante => Immobilise un certain temps (court)
            self.unmoving = 1
        elif trap == "." : # 0) Exp. intéressante => Immobilise un certain temps (court)
            self.disturbed = True
