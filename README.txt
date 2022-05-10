Bienvenue sur notre site d'analyse de la Ferme des 3 Chênes.  

COMMENT LANCER LE SITE:
-----------------------

Prérequis:
1) Soyez connecté à Internet (pour que Chart.js fonctionne)
2) Ayez le module flask installé sur votre pc, pour cela il suffit de lancer la commande 
	'pip install flask' 
3) Ayez le module astral installé sur votre pc, pour cela il suffit de lancer la commande 
	'pip install astral' 
-> Bien évidemment, pour que pip fonctionne python doit être installé. La version de python doit être au minimum Python3

Le lancement:
-> Afin de lancer le site, il faut faire attention à ne pas créer de bug dû à VScode par exemple. Pour éviter cela, suivez bien l'explication ci-dessous:

1) Le plus simple pour éviter tout bug est de lancer le programme depuis le terminal.
--> Sur windows, allez dans le dossier où se trouve 'main.py' ...../flaskr/main.py grâce à l'explorateur de fichier
	-> Une fois dedans, lancez le terminal dans ce dossier (cliquez sur l'adresse du fichier en haut de la page et écrivez cmd) https://www.thewindowsclub.com/wp-content/uploads/2009/04/cmd-in-folder.png?ezimgfmt=ng:webp/ngcb188 
	-> Une fois dans le terminal, lancez la commande suivante:
		'python3 main.py'
	
--> Sur Linux/Mac, ouvrez un terminal et rendez-vous dans le dossier où se trouve main.py, pour cela, utilisez la commande cd:
	cd .../.../P2_VINCENT_9/flaskr/ (les ... représentent vos dossiers, l'emplacement du dossier P2 dépend de là où vous l'avez extrait)
	--> Une fois dedans, lancez la commande suivante:
		'python3 main.py' 

-> Copiez l'adresse donnée et entrez-la sur un navigateur (Firefox de préférence mais Chrome fonctionne correctement aussi ainsi que Safari sur MacOS)

LE SITE:
--------

Vous êtes automatiquement redirigé vers la page home, où se trouve quelques infos sur la ferme. N'hésitez pas à vous balader et à lire si cela vous chante.

-> Pour accéder aux schémas, cliquez sur "analytics" en haut à droite. Une fois dessus, vous aurez l'occasion de sélectionner les paramètres voulus et ensuite d'afficher le graphe en cliquant sur "Afficher le Graphe". 

Ce qui marche:
- - - - - - - -
- "Graphe à afficher": vêlages. Le choix des dates influence bien le graphe, ainsi que le choix de la ou les famille(s). 
- "Graphe à afficher": naissances lors des jours de pleine lune. Le choix des dates influence bien le graphe, ainsi que le choix de la ou les famille(s). 
- "Graphe à afficher": races.


- "Graphe à afficher": répartition. Ce graphe affiche la répartition entre les vaches de sexe masculin ou féminin.


Ce qui ne marche pas:
- - - - - - - - - - -


   - - - - - - -



FONCTIONNEMENT GÉNÉRAL:
-----------------------
|
| ~flaskr
-- |
   | ~static
   -- |
      | - style.css (pour le style)
      | - favicon.ico (icône du site)
      | - vache.jpg (image pour la page home)
   |
   | ~templates
   -- |
      | - base.html (squelette du site pour l'héritage)
      | - home.html (page d'accueil)
      | - analytics (page de choix des options de graphe et les "envoie" à flask)
      | - graph.html (page avec le javascript qui récupère les infos de flask)
   |
   | - database.db (data du site contenant toutes les infos)
   | - database-date-format-basic.db
   | - heritage_creation.py (récupération de l'héritage)
   | - schema.sql (schéma de la base des données)
   | - function.py (fonction de la création des paramètres d'affichage de graphes)
   | - main.py (lanceur du site et récupérateur des infos données par les utilisateurs, les envoie ensuite à function.py qui retourne les données ensuite injectées dans graph.html)
 
      
      
