# -*-coding:utf-8-*-

def move() : # gestion de l'IA de Schro.
	# x : abscisse
	# y : ordonnée
	# d : direction actuelle (haut, gauche, droite)
	# a : accélération (défaut=0.3)
	# v : vitesse actuelle
	global x, y, d, a, v # recherche des variables globales, déclarées en dehors de la fonction
	fv = (1 + a) * v
	fx = x
	fy = y

	if d == "left" :
		fx = x - fv
		if fx < 0 : # changement de direction lorsque Schro. arrive en bout de ligne (par la gauche)
			fx = 0
			fd = "up"
		else :
			x = fx
	elif d == "right" :
		fx = x + fv
		if fx > 100 : # changement de direction lorsque Schro. arrive en bout de ligne (par la droite)
			fx = 100
			fd = "up"
		else :
			x = fx
	elif d == "up" :
		fy = y + fv
	else :
		print("error")
	print(x)
	print(y)
