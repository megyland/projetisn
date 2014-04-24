# -*-coding:utf-8-*-

class Enemy:
	# Classe de Schrödinger
	def __init__(self, table, dir1): # Méthode constructeur (s'active à l'initialisation de la classe)
		# table : variable de type tableau contenant le niveau
		# dir1 : direction de départ
		# x : abscisse
		# y : ordonnée
		# d : direction actuelle (haut, gauche, droite)
		# a : accélération
		# v : vitesse actuelle
		self.table = table
                self.x = 0
		for ligne in self.table :
			if "s" in ligne :
				self.y = ligne.index("s")
                        self.x += 1
		
		self.d = dir1
		"""
		self.x=dx
		self.y=dy
		"""
		self.v=0.01
		self.a=0.003
		
	def move(self) : # gestion de l'IA de Schro.
		# établissement des directions en fonction des collisions
		for i in self.table[self.y - 1] : 
			if " " in i and self.table[self.y - 1][self.x] == " " :
				self.d = "up"
			elif self.d == "right" :
                                if len(self.table[self.y]) - self.x > 1 and self.table[self.y][self.x + 1] == " " :
					self.d = "right"
				else :
					self.d = "left"
			elif self.d == "left" :
                                if self.x - 1 >= 0 and  self.table[self.y][self.x - 1] == " " :
					self.d = "left"
				else :
					self.d = "right"
		
		self.v = (1 + self.a ) * self.v # augmentation de la vitesse en fonction de l'accélération (à tester)
		# incrémentation des coordonnées du personnage en fonction de la direction

		if self.d == "up" :
			# fx et fy sont les coordonnées fictives de Schrö., qui permettront la gestion de l'animation
			# la gestion des collisions est faite à partir de x et y
			self.fx = self.x
			self.fy = self.y - self.v
			if self.fy <= self.y - 1 :
				self.y -= 1
		elif self.d == "right" :
			self.fy = self.y
			self.fx = self.x + self.v
			if self.fx >= self.x + 1 :
				self.x += 1
		elif self.d == "left" :
			self.fy = self.y
			self.fx = self.x - self.v
			if self.fx <= self.x - 1 :
				self.x -= 1

                return (self.fx, self.fy)
			
	"""
	def move_old(self) : # gestion de l'IA de Schro.
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
	"""
	
	# Les prochaines méthodes sont les actions des pièges :
			
	def correct_error(time) : # Piège "Erreur de calcul"
		if time != 0 :
			self.tempV = self.v
			self.v = 0
		else :
			self.v = 0.1
	
	
