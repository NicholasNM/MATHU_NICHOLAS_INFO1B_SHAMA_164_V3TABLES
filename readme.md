# Module 164 2022.04.13


Le "début de la fin"

---
#### Avant de commencer cette version presque finale.
##### Cette démo. CRUD (Create Read Update Delete) presque complète sur les 3 tables de la base film : Soit "t_film"; "t_genre" et la table intermédiaire "t_genre_film"
* Un serveur MySql doit être installé
  * UWAMP : sur le site de "UWAMP", lire "Prerequisites IMPORTANT!!" (vous devez installer une des distributions Visual C++, j'ai choisi la plus récente) 
  * UWAMP : installer la version "EXE" (Choisir : Télécharger Exe/Install) est préférable à la version "PORTABLE"
  * UWAMP : accepter les 2 alertes de sécurité d'accès aux réseaux (apache et MySql)
  * MAC : MAMP ou https://www.codeur.com/tuto/creation-de-site-internet/version-mysql/
  * Contrôler que tout fonctionne bien. Ouvrir "UWAMP". Cliquer sur le bouton "PhpMyAdmin". Utilisateur : root Mot de passe : root
* Python doit être installé.
  * ATTENTION : Cocher la case pour que le "PATH" intègre le programme Python
  * Une fois la "case à cocher" du PATH cochée, il faut choisir d'installer
  * Un peu avant la fin du processus d'intallation, cliquer sur "disabled length limit" et cliquer sur "CLOSE"
  * Le test de Python se fait après avec le programme "PyCharm"
* Installer "GIT"
  * https://gitforwindows.org/
  * Le test de "GIT" se fait dans le programme "PyCharm"
* "PyCharm" (community) doit être intallé, car toutes mes démonstrations sont faites avec cette version de l'IDE. INFO : Vous pouvez télécharger tous les produits de JetBrains car vous êtes étudiant.
  * Lors de l'installation, il faut cocher toutes les options ASSOCIATIONS, ADD PATH, etc
  * Ouvrir "PyCharm" pour la première fois pour le configurer. Choisir le bouton "New Project"
  * Changer le répertoire pour ce nouveau projet, il faut créer un nouveau répertoire "vide" dans votre ordi en local.
  * Il est important d'avoir sélectionné le répertoire que vous venez de créer car "PyCharm" va automatiquement créer un
    environnement virtuel (venv) dans ce répertoire
  * Menu : File->Settings->Editor->General->Auto Import (rubrique Python) cocher "Show auto-import tooltip"
  * PyCharm vient d'ouvrir une fenêtre avec le contenu du "main.py" pour configurer les actions "UNDO" et "REDO"
  * Sélectionner tout le texte avec "CTRL-A" puis "CTRL-X" (Couper), puis "CTL-Z" (UNDO) et faites un REDO "CTRL-Y" et "PyCharm" va vous demander de choisir l'action du "CTRL-Y" raccourci pour faire un "REDO". (Dans 98% des éditeurs de texte, le "CTRL-Y" représente l'action "REDO"... pas chez JetBrains)



## Situation 1 : Vous n'avez encore rien modifié depuis le 14.04 2022
  * Cloner ma dernière version (lien ci-dessous)
  * Ouvrir "PyCharm". Cliquer sur le bouton à droite "GET FROM VCS"
      * Une fenêtre s'ouvre, copier le lien suivant dans le champ url : https://github.com/info164/164_OM_PYTHON_MYSQL_FLASK_EX_2_V1.git
      * Il est indispensable de créer un répertoire vide pour accueillir MON projet de référence. Cliquer sur l'icône répertoire
      * Cliquer sur le bouton "CLONE"
      * Une fenêtre de sécurité "Trust and open project"... cliquer sur "Trust"
      * Laisser "PyCharm" créer un environnment virtuel, cliquer sur "Ok"
      * Lire et réaliser les étapes du mode d'emploi de la démonstration
	
### Faire une copie du répertoire afin de pouvoir travailler sur une copie et non sur l'original.
  * Fermer "PyCharm"
  * Faire une copie du répertoire où vous venez d'importer "MA" démonstration
  * Renommer cette copie de répertoire : "VOTRENOM_VOTREPRENOM_VOTRECLASSE_VOTRESUJET_164_V3TABLES"
  * Ouvrir ce répertoire. Effacer les 3 sous-répertoires suivants (".git" répertoire caché, ".idea" et "venv")
  * Ouvrir "PyCharm", puis "File"-->"Open..." un projet et choisir le répertoire racine "VOTRENOM_VOTREPRENOM_VOTRECLASSE_VOTRESUJET_164_V3TABLES"
  * Lire et réaliser les étapes du mode d'emploi de la démonstration
  * Quand "MA" démonstration fonctionne, alors il faut passer à "Vos devoirs"


## Situation 2 : Vous avez déjà commencé à remplacer mes requêtes par les vôtres depuis le 14.04 2022
  * Cloner (comme en situation 1) ma dernière version : https://github.com/info164/164_OM_PYTHON_MYSQL_FLASK_EX_2_V1.git
  * En faire une copie (voir plus haut)
  * Ouvrir votre projet que vous avez déjà commencé à modifier
  * Dans "PyCharm", cliquer avec le bouton droit de la souris sur le nom de la racine de votre projet et choisir "Compare With..." (CTRL-D", vous devez importer tout ce qui a changé dans la nouvelle version que je vous propose, mais ne pas écraser ce que vous avez déjà fait.

## Mode d'emploi de cette démonstration
* Démarrer le serveur MySql (uwamp ou xamp ou mamp, etc)
* Dans "PyCharm", importer la BD à partir du fichier DUMP
    * Ouvrir le fichier "database/1_ImportationDumpSql.py"
    * Cliquer avec le bouton droit sur l'onglet de ce fichier et choisir "run" (CTRL-MAJ-F10)
    * En cas d'erreurs : ouvrir le fichier ".env" à la racine du projet, contrôler les indications de connexion pour la
      bd.
* Test simple de la connexion à la BD
    * Ouvrir le fichier "database/2_test_connection_bd.py"
    * Cliquer avec le bouton droit sur l'onglet de ce fichier et choisir "run" (CTRL-MAJ-F10)
* Démarrer le microframework FLASK
    * Dans le répertoire racine du projet, ouvrir le fichier "run_mon_app.py"
    * Cliquer avec le bouton droit sur l'onglet de ce fichier et choisir "run" (CTRL-MAJ-F10)

## Mode d'emploi de votre github
* Créer un compte github
* Cliquer sur le menu déroulant de votre compte github (à droite en haut), choisir "your repositories"
  * Faire un "NEW" repostiories avec le bouton "NEW"
  * Le nom doit être "VOTRENOM_VOTREPRENOM_VOTRECLASSE_VOTRESUJET_164_V3TABLES"
  * Petite description dans le champ juste au-dessous
  * Définissez votre projet en "private"
  * Cliquer sur "Create repository"
  * Copier l'adresse de votre repository https://?????????/!!!!!????/VOTRENOM_VOTREPRENOM_VOTRECLASSE_VOTRESUJET_164_V3TABLES.git
* Dans le menu au-dessus choisir "Settings"
  * Menu à gauche choisir "Collaborators"
  * Dans la nouvelle page cliuer sur le bouton "Add people"
  * Écrire dans le champ mon adresse mail officielle (déjà donnée lors des cours)

## Github et PyCharm (si c'est la première fois que vous définissez un repository distant"
* Dans "PyCharm" ouvrir votre projet
* Dans le menu "VCS", cliquer "Enable Version Control Integration", après cette action le nom "VCS" est remplacé par "Git"
  * Une fenêtre s'ouvre, choisir le system "git"
* Cliquer sur le menu "Git", choisir "Commit..."
* Définir un message de Commit (Obligatoire)
* Cliquer sur le menu "Git", choisir "Push..."
* Vous devez définir la première fois le nom de votre repository distant coller votre adresse copiée avant : https://?????????/!!!!!
  ????/VOTRENOM_VOTREPRENOM_VOTRECLASSE_VOTRESUJET_164_V3TABLES.git
* Il vous sera demandé de vous connecter au travers de "JetBrains, PyCharm", acceptez et remplir avec votre mot de passe de votre github
* Vous pouvez cliquer sur le bouton "Push"
* Faites de nombreux "Commit"/"Push", c'est la garantie de ne rien perdre et que j'analyse votre avance sur votre projet
# Vos devoirs :
* Placer votre "DUMP" à la place de celui de ma "BD" films. Votre "DUMP" doit se nommer "VOTRENOM_VOTREPRENOM_VOTRECLASSE_VOTRESUJET_164.SQL"
  * Dans le répertoire "database" vous devez placer vos fichiers (PDF: Cahier des charges, MCD, MLD, dictionnaires des données et SQL : requêtes, etc)
  * Ouvrir le fichier "database/1_ImportationDumpSql.py"
    * Cliquer avec le bouton droit sur l'onglet de ce fichier et choisir "run" (CTRL-MAJ-F10)
    * En cas d'erreurs : ouvrir le fichier ".env" à la racine du projet, contrôler les indications de connexion pour la
      bd.
* Test simple de la connexion à la BD
    * Ouvrir le fichier "database/2_test_connection_bd.py"
	* Modifier "MA" requête par votre requête
    * Cliquer avec le bouton droit sur l'onglet de ce fichier et choisir "run" (CTRL-MAJ-F10)	  
	  
A) Modifier MES requêtes AFFICHER (READ) du CRUD(Create Read Update Delete) sur la table "t_genre"
  *	Ouvrir le fichier "genres/gestion_genres_crud.py"
  * Modifier les requêtes "SELECT" sur la table "t_genre" par des "SELECT" sur une de vos "t_????"
  * Modifier dans le répertoire "TEMPLATES" la page html consacrée à l'affichage pour ma "t_genre", il faut ouvrir "templates/genres_afficher.html"
  * Vous devez vous aider de "CTRL-R"(scope : fichier) ou "CTRL-SHIFT-R"(scope : tout le projet)
  * utiliser la commande "magique" de "PyCharm" comparer deux fichiers "CTRL-D" (menu "View"-->"Compare With...") entre le fichier de mon projet qui fonctionne et le votre qui est presque fonctionnel.

B) Une fois que l'affichage est fonctionnel et uniquement dans ce cas :
  * Vous devez alors changer les noms de variables en Python pour les adapter à votre sujet
    * Exemple : "strsql_genres_afficher" doit s'écrire avec un nom qui correspond mieux à votre sujet de BD

C) Faites souvent des "COMMITS" et des "PUSH" sur votre "GITHUB" (VOTRENOM_VOTREPRENOM_VOTRECLASSE_VOTRESUJET_164_V3TABLES)

D) Recommencer les étapes A) à C) pour l'action "CREATE" pour la table "t_genre"

E) Recommencer les étapes A) à C) pour l'action "UPDATE" pour la table "t_genre"

F) Recommencer les étapes A) à C) pour l'action "DELETE" pour la table "t_genre"

G) Passez à une autre table (MAIS PAS UNE TABLE INTERMÉDIAIRE) de votre BD

# Évaluation de votre module 164
Dans le but de l'évaluation du module 164, chaque semaine, vous devez déposer votre travail (fichier zip du repository de votre Github) sur le moodle de l'EPSIC
 
  * Si vous ne pouvez pas avancer, vous DEVEZ vous entraider (votre groupe DISCORD est là pour cela)
  * Je suis là pour vous aider, mais il faut que vous me posiez des questions, par mail, cela est parfaitement possible
  * Je vais observer votre avance sur votre github où vous avez défini mon adresse couriel officielle comme "collaborateur" à votre github
  * Réaliser un "COMMIT" avec un message qui indique votre avance en quelques mots
  * Réaliser un "PUSH" dans votre "GITHUB" privé, n'oubliez pas de m'inviter avec mon adresse officielle (déjà donnée)

  * Dans votre github. Créer un fichier "zip" à télécharger sur votre disque local vous DEVEZ le déposer sur Moodle de l'EPSIC dans la semaine correspondante
  * Le lien de votre github doit être dans un fichier "txt" que vous DEVEZ déposer sur Moodle de l'EPSIC dans la semaine correspondante
  * Il faut respecter mes consignes énoncées dans ce fichier "readme.md" et sur le MOODLE de l'EPSIC. Sinon, vous ne pourrez plus prétendre à l'excellence, soit la note de "6"
    * Le but de ce module 164 est de faire un CRUD sur votre BD, pas de faire du code. Donc faites ce qui est demandé pas plus, ni moins


# Pour "rafraîchir" les versions des packages (Terminal de "PyCharm") 

  * pip3 freeze > requirements.txt
  * pip3 install pipupgrade
  * pipupgrade --verbose --latest --yes

