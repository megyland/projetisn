Projet ISN : Schrödinger's Cat
==========

![alt text](http://img15.hostingpics.net/pics/166702logom.png "Logo")

Répartition du travail :
------------------------
**Les personnes intéressées par un de ces objectifs doivent se signaler dans le tableau.**  

Objectif | Personne en charge | Etat | Commentaires
:-------:|:------------------:|:----:|:------------:
IA de Schrödinger | Choumat | En développement | 
Apparence du niveau | megyland | En développement |
Ajout de _Erreur de calcul_ | Choumat | En test | Arrêt moyen de Schrödinger, puis redémarrage normal
Ajout de _Expérience intéressante_ | ? | ? | Arrêt court, puis redémarrage normal
Ajout de _Compteur de vitesse_ | ? | ? | Schrö. continue tout droit sur un certain nombre de pas sans être capable de tourner, un autre piège interrompt l'effet ; s'il s'est cogné contre un mur, il s'arrête un temps
Ajout de _Expérience ratée_ | ? | ? | Arrêt long, puis redémarrage normal
Ajout de _Début d'incendie_ | ? | ? | Propagation d'un feu, chaque flamme demande du temps à Schrödinger pour être arrêtée ; si une flamme atteint le chat, il meurt
Placement des objets par Drag&Drop | ? | ? |
Ecran d'accueil | pascalcpp | Fini
... | ? | ? |

Travail de _megyland_ par séance :
---------------------------------

Travail de _Choumat_ par séance :
--------------------------------
* __27/03__ :
 - Création d'une fonction _move()_

* __28/03__ :
 - Création d'une classe _Entity_, pour référencer tous les éléments du jeu, comme Schrödinger, la boîte du chat, les objets posés...
 - Fonction _move()_ intégrée comme méthode à la classe _Entity_

* __29/03__ :
 - Proposition d'un format pour la sauvegarde du niveau avec un fichier prototype _parcours.txt_
 - Fichier _algo.py_ renommé _entity.py_ : il sera réservé à la classe _Entity_ et à ses méthodes
 - Ajout d'un fichier *test_entity.py* pour tester la classe _Entity_ et ses méthodes
 - Documentation sur la bibliothèque _Pygame_, qui va nous servir d'interface graphique  
(tutoriel intéressant : http://fr.openclassrooms.com/informatique/cours/interface-graphique-pygame-pour-python )

* __9/04__ :
 - Fichier _entity.py_ renommé _enemy.py_
 - Ajout de la méthode d'_Enemy_ nommée *correct_error()* : action du piège _Erreur de calcul_

Travail de _pascalcpp_ par séance :
----------------------------------

* __5/04__ :
 - Ajout de l'écran d'accueil (les images pourront êtres modifiées par la suite, je les ai créées à l'arrache pour pouvoir tester)
