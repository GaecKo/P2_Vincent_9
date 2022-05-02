Bienvenue sur notre site d'analyse de la Ferme des 3 Chênes. 

Comme vous pourrez le voir, celui-ci est loin d'être fini et ne porte pas encore toutes les options nécessaires, mais est déjà sur une bonne lancée. 

COMMENT LANCER LE SITE:
-----------------------

Prérecquis:
1) Soyez connecté à internet (pour que chart.js fonctionne)
2) Ayez le module flask installé sur votre pc, pour cela il suffit de lancer la commande 
	'pip install flask' 
-> Bien évidemment, pour que pip fonctionne python doit être installé. La version de python doit être au minimum python3

Le lancement:
-> Afin de lancer le site, il faut faire attention à ne pas créer de bug dû à VScode par exemple, pour cela suivez bien l'explication ci-dessous

1) Le plus simple pour éviter tout bug est de lancer le programme depuis le terminal.
--> Sur windows, allez dans le dossier où se trouve 'main.py' ...../flaskr/main.py grâce à l'explorateur de fichier
	-> Une fois dedans, lancez le terminal dans ce dossier (cliquez sur l'adresse du fichier en haut de la page et écrivez cmd) https://www.thewindowsclub.com/wp-content/uploads/2009/04/cmd-in-folder.png?ezimgfmt=ng:webp/ngcb188 
	-> Une fois dans le terminal, lancez la commande suivant:
		'python3 main.py'
	
--> Sur Linux/Mac, ouvrez un terminal et rendez-vous dans le dossier où se trouve main.py, pour cela, utilisez la commande cd:
	cd .../.../P2_VINCENT_9/flaskr/ (les ... représentent vos dossiers, l'emplacement du dossier P2 dépend de là où vous l'avez extrait)
	--> Une fois dedans, lancez la commande suivant:
		'python3 main.py' 

-> Copiez l'addresse donnée et entrez la sur un navigateur (firefox de préférence mais chrome fonctionne correctement aussi (normalement))

LE SITE:
--------

Vous êtes automatiquement redirigé vers la page home, où se trouve quelques infos sur la ferme. N'hésitez pas à vous balader et à lire si cela vous chante.

-> Pour accéder aux schémas, cliquez sur "analytics" en haut à droite. Une fois dessus, vous aurez l'occasion de sélectionner les paramètres voulus et ensuite d'afficher le graphe en cliquant sur "Afficher le Graphe". 

Ce qui marche:
- - - - - - - -
- "Graphe à afficher": vêlages. C'est le seul des 3 graphes actuellement fonctionnel. Le choix des dates influencent bien le graphe, cependant la famille pas encore. 

Ce qui ne marche pas:
- - - - - - - - - - -
- Le reste, nous avons malheureusement eu quelques soucis dans la répartitions des taches causant des délais dans le rendu final... L'html fonctionne correctement et le javascript aussi, le css est aussi bon. Il ne reste plus qu'à récupérer certaines informations et les envoyer et le projet sera pratiquement complet.   
- Nous devons encore mettre à jour les paragraphes en dessous de chaques graphes, mais cela n'est pas trop long.

FONCTIONNEMENT GÉNÉRAL:
-----------------------
|
| ~flaskr
-- |
   | ~static
   -- |
      | - style.css (pour le style)
      | - favicon.ico (icone du site)
      | - vache.jpg (image pour la page home)
   |
   | ~templates
   -- |
      | - base.html (squelette du site pour l'héritage)
      | - home.html (page d'acceuil)
      | - analytics (page de choix des options de graphe et les "envoie" à flask)
      | - graph.html (page avec le javascript qui récupère les infos de flask)
   |
   | - database.db (data du site contenant toutes les infos)
   | - schema.sql (schema de la base de donnée)
   | - function.py (fonction de la création des paramètres d'affichage de graphes)
   | - main.py (lanceur du site et récupérateur des infos données par les utilisateurs, les envoies ensuite à function.py qui retourne les données ensuite injectées dans graph.html)
 
      
      
