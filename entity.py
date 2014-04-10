# -*-coding:utf-8-*-

class Entity:
	# Classe des entités (Schro., le chat, les pièges...)
	def __init__(self, type, dx, dy): # Méthode constructeur (s'active à l'initialisation de la classe)
		self.x=dx
		self.y=dy
		if type == "ennemy":
			self.d="right"
			self.v=0.1
			self.a=0.003
	def move(self) : # gestion de l'IA de Schro.
		# x : abscisse
		# y : ordonnée
		# d : direction actuelle (haut, gauche, droite)
		# a : accélération
		# v : vitesse actuelle
		self.v = (1 + self.a ) * self.v

		if self.d == "left" :
			tx = self.x - self.v
			if tx <= 0 : # changement de direction lorsque Schro. arrive en bout de ligne (par la gauche)
				self.x = 0
				self.d = "up"
			else :
				self.x = tx
		elif self.d == "right" :
			tx = self.x + self.v
			if tx >= 100 : # changement de direction lorsque Schro. arrive en bout de ligne (par la droite)
				self.x = 100
				self.d = "up"
			else :
				self.x = tx
		elif self.d == "up" :
			ty = self.y + self.v
		else :
			print("error")


