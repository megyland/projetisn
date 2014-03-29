# -*-coding:utf-8-*-

class Entity:
	# Classe des entités (Schro., le chat, les pièges...)
	def __init__(self, type, dx, dy): # Méthode constructeur (s'active à l'initialisation de la classe)
		self.x=dx
		self.y=dy
		if type == "ennemy":
			self.d="right"
			self.v=0.06
			self.a=0.005
	def move(self) : # gestion de l'IA de Schro.
		# x : abscisse
		# y : ordonnée
		# d : direction actuelle (haut, gauche, droite)
		# a : accélération (défaut=0.3)
		# v : vitesse actuelle
		fv = (1 + self.a) * self.v
		fx = self.x
		fy = self.y

		if self.d == "left" :
			fx = self.x - fv
			if fx < 0 : # changement de direction lorsque Schro. arrive en bout de ligne (par la gauche)
				fx = 0
				fd = "up"
			else :
				self.x = fx
		elif self.d == "right" :
			fx = self.x + fv
			if fx > 100 : # changement de direction lorsque Schro. arrive en bout de ligne (par la droite)
				fx = 100
				fd = "up"
			else :
				self.x = fx
		elif self.d == "up" :
			fy = self.y + fv
		else :
			print("error")
		print(self.x)
		print(self.y)

"""Schro = Entity("ennemy",0,0) # Création de Schrodinger
Schro.move() # Déplacement de Schrodinger (utiliser boucle avec délai) """

