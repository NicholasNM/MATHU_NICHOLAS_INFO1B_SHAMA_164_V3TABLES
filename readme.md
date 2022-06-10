# Module 164 2022.04.13 - Nicholas N. Mathu : 
Ce projet a été effectué afin de fournir un support informatique pour l'entité Shama

Shama est une entité comportant plusieurs entreprises dont Shama Milk, Shama Premier et Shama academy. 
Ce projet a été focalisé sur les entreprises Shama Milk et Shama Premier qui sont des distrubuteurs de lait dans 
les zones rurales.

Ce projet fournit une gestion de personnel avec l'onglet personnes nous donnant la possibilité d'ajouter des employées,
de modifier des données de ces employées ou même de les supprimer au venu de l'éventuel licenciement.

Ce projet permet aussi de modifier des données des entreprises elles-mêmes dont :
- Modification du nom
- Modification du numéro
- Modification de l'email
- modification du personnel faisant partie des entreprises

Cela permet une gestion dynamique des effectifs selon les besoins.

Ce projet permet finalement la gestion des différents magasins dont :
- Modification du nom
- Modification du numéro
- Modification de l'email
- Modification du volume que contient le magasin
- Modification de l'argent que contient le magasin

# Marche à suivre pour faire fonctionner le projet :

# Uwamp:

* Un serveur MySql doit être installé : UwAmp est très utile pour cela (lien: https://www.uwamp.com/en/?page=download)
  * UWAMP : sur le site de "UWAMP", lire "Prerequisites IMPORTANT!!" (vous devez installer une des distributions Visual C++, j'ai choisi la plus récente) 
  * UWAMP : installer la version "EXE" (Choisir : Télécharger Exe/Install) est préférable à la version "PORTABLE"
  * UWAMP : accepter les 2 alertes de sécurité d'accès aux réseaux (apache et MySql)
  * Pour les utilisateur de MAC (donc des hommes serpent) : MAMP ou https://www.codeur.com/tuto/creation-de-site-internet/version-mysql/
  * Contrôler que tout fonctionne bien. Ouvrir "UWAMP". Cliquer sur le bouton "PhpMyAdmin". Utilisateur : root Mot de passe : root

# Python:

* Python doit être installé : De préférence 3.10 (lien: https://www.python.org/downloads/release/python-3100/)
  * ATTENTION : Cocher la case pour que le "PATH" intègre le programme Python
  * Une fois la "case à cocher" du PATH cochée, il faut choisir d'installer
  * Un peu avant la fin du processus d'intallation, cliquer sur "disabled length limit" et cliquer sur "CLOSE"
  * Le test de Python se fait après avec le programme "PyCharm"

# Github:

* Installer "GIT"
  * https://gitforwindows.org/
  * Le test de "GIT" se fait dans le programme "PyCharm"

# PyCharm:

* "PyCharm" (community) doit être intallé. Il s'agit d'un environnement de développement intégré (IDE)
* INFO : Il est préféreble d'utiliser PyCharm Pro qui possède plus d'option et une meilleure affichage
  * Lors de l'installation, il faut cocher toutes les options ASSOCIATIONS, ADD PATH, etc
  * Ouvrir "PyCharm" pour la première fois pour le configurer. Choisir le bouton "New Project"
  * Changer le répertoire pour ce nouveau projet, il faut créer un nouveau répertoire "vide" dans votre ordi en local.
  * Il est important d'avoir sélectionné le répertoire que vous venez de créer car "PyCharm" va automatiquement créer un
    environnement virtuel (venv) dans ce répertoire
  * Menu : File->Settings->Editor->General->Auto Import (rubrique Python) cocher "Show auto-import tooltip"
  * PyCharm vient d'ouvrir une fenêtre avec le contenu du "main.py" pour configurer les actions "UNDO" et "REDO"
  * Sélectionner tout le texte avec "CTRL-A" puis "CTRL-X" (Couper), puis "CTL-Z" (UNDO) et faites un REDO "CTRL-Y" et -
  * -> "PyCharm" va vous demander de choisir l'action du "CTRL-Y" raccourci pour faire un "REDO". -
  * -> (Dans 98% des éditeurs de texte, le "CTRL-Y" représente l'action "REDO"... pas chez JetBrains)

* Aller dans le fichier requirements.txt et lancer les différents paquets qui s'y trouvent
  * Cela va permettre de lire et afficher certaines informations qui sans cela ne seront pas visible
  * cela va aussi permettre au projet de mélanger plusieurs langages de programation dont html et python

# Intégrer base de données (BD):
* Créer une base de données comportant; tables, tabels intermédiaires, identifiants, foreign keys et données
  * (ex: id_personnes, nom_personnes, prenom_personnes)
  
* Prendre le fichier dump de cette base de données et l'ajouter au fichier "database"
* Faire en sorte a ce que cette partie dans le fichier ".env" corresponde au nom de votre fichier :
  * NAME_BD_MYSQL="MATHU_NICHOLAS_INFO1B_SHAMA_164_2022"
  * NAME_FILE_DUMP_SQL_BD="../database/MATHU_NICHOLAS_INFO1B_SHAMA_164_2022.sql"

* Lancer le fichier 1_ImportationDumpSql.py
  * Cela va ajouter votre base de données au projet afin qu'il soit utilisable pour la suite 

* Créer une requête concernant votre base de données
  * placer cette requête dans le fichier 2_test_connection_bd.py
  * lancer le fichier 2_test_connection_bd.py
    * Si le résultat de votre requête est affiché dans la terminale, la base de données a été intégré correctement
    * Si le résultat de votre requête ne s'affiche pas; il y a surement une erreur dans votre requête, corrigez cela!


# Vous pouvez donc maintenant lancer le fichier run_mon_app.py

* Par la suite, si vous souhaitez accéder à votre base de donnée il serai important de connecter votre compte ->
* -> Github 
  * aller sur l'onglet git

