"""Gestion des "routes" FLASK et des données pour les adresse.
Fichier : gestion_adresse_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.adresse.gestion_adresse_wtf_forms import FormWTFUpdateAdresse, FormWTFAddFilm, FormWTFDeleteFilm

"""Ajouter un film grâce au formulaire "adresse_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /adresse_add

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "ADD" d'un "film"

Paramètres : sans


Remarque :  Dans le champ "nom_adresse_update_wtf" du formulaire "adresse/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/adresse_add", methods=['GET', 'POST'])
def adresse_add_wtf():
    # Objet formulaire pour AJOUTER un film
    form_add_film = FormWTFAddFilm()
    if request.method == "POST":
        try:
            if form_add_film.validate_on_submit():
                rue_add = form_add_film.rue_add_wtf.data
                numero_add = form_add_film.numero_add_wtf.data
                localite_add = form_add_film.localite_add_wtf.data

                valeurs_insertion_dictionnaire = {"value_rue": rue_add,
                                                  "value_numero": numero_add,
                                                  "value_localite": localite_add}
                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_adresse = """INSERT INTO t_adresse (id_adresse, Rue, Numero, Localite) VALUES
                                        (NULL,%(value_rue)s,%(value_numero)s,%(value_localite)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_adresse, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion du nouveau film (id_adresse_sel=0 => afficher tous les adresse)
                return redirect(url_for('adresse_personnes_afficher', id_adresse_sel=0))

        except Exception as Exception_personnes_ajouter_wtf:
            raise ExceptionPersonnesAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{adresse_add_wtf.__name__} ; "
                                            f"{Exception_personnes_ajouter_wtf}")

    return render_template("adresse/adresse_add_wtf.html", form_add_film=form_add_film)


"""Editer(update) un film qui a été sélectionné dans le formulaire "adresse_personnes_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /adresse_update

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "EDIT" d'un "film"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "genres_afficher.html"

Remarque :  Dans le champ "nom_adresse_update_wtf" du formulaire "adresse/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/adresse_update", methods=['GET', 'POST'])
def adresse_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_adresse"
    id_adresse_update = request.values['id_adresse_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_adresse = FormWTFUpdateAdresse()
    try:
        print(" on submit ", form_update_adresse.validate_on_submit())
        if form_update_adresse.validate_on_submit():
            # Récupèrer la valeur du champ depuis "genre_update_wtf.html" après avoir cliqué sur "SUBMIT".
            rue_update = form_update_adresse.rue_update_wtf.data
            numero_update = form_update_adresse.numero_update_wtf.data
            localite_update = form_update_adresse.localite_update_wtf.data

            valeur_update_dictionnaire = {"value_id_adresse": id_adresse_update,
                                          "value_rue": rue_update,
                                          "value_numero": numero_update,
                                          "value_localite": localite_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_adresse = """UPDATE t_adresse SET Rue = %(value_rue)s,
                                                            Numero = %(value_numero)s,
                                                            Localite = %(value_localite)s
                                                            WHERE id_adresse = %(value_id_adresse)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_adresse, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le film modifié, "ASC" et l'"id_adresse_update"
            return redirect(url_for('adresse_personnes_afficher', id_adresse_sel=id_adresse_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_adresse" et "intitule_genre" de la "t_genre"
            str_sql_id_adresse = "SELECT * FROM t_adresse WHERE id_adresse = %(value_id_adresse)s"
            valeur_select_dictionnaire = {"value_id_adresse": id_adresse_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_adresse, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_adresse = mybd_conn.fetchone()
            print("data_adresse ", data_adresse, " type ", type(data_adresse), " personnes ",
                  data_adresse["Rue"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "adresse_update_wtf.html"
            form_update_adresse.rue_update_wtf.data = data_adresse["Rue"]
            form_update_adresse.numero_update_wtf.data = data_adresse["Numero"]
            form_update_adresse.localite_update_wtf.data = data_adresse["Localite"]
            # Debug simple pour contrôler la valeur dans la console "run" de PyCharm
            print(f" Localite  ", data_adresse["Localite"], "  type ", type(data_adresse["Localite"]))

    except Exception as Exception_adresse_update_wtf:
        raise ExceptionAdresseUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{adresse_update_wtf.__name__} ; "
                                     f"{Exception_adresse_update_wtf}")

    return render_template("adresse/adresse_update_wtf.html", form_update_adresse=form_update_adresse)


"""Effacer(delete) un film qui a été sélectionné dans le formulaire "adresse_personnes_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /film_delete
    
Test : ex. cliquer sur le menu "film" puis cliquer sur le bouton "DELETE" d'un "film"
    
Paramètres : sans

Remarque :  Dans le champ "nom_film_delete_wtf" du formulaire "adresse/adresse_delete_wtf.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/film_delete", methods=['GET', 'POST'])
def film_delete_wtf():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_adresse_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_adresse"
    id_adresse_delete = request.values['id_adresse_btn_delete_html']

    # Objet formulaire pour effacer le film sélectionné.
    form_delete_film = FormWTFDeleteFilm()
    try:
        # Si on clique sur "ANNULER", afficher tous les adresse.
        if form_delete_film.submit_btn_annuler.data:
            return redirect(url_for("adresse_personnes_afficher", id_adresse_sel=0))

        if form_delete_film.submit_btn_conf_del_film.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "adresse/adresse_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_adresse_delete = session['data_adresse_delete']
            print("data_adresse_delete ", data_adresse_delete)

            flash(f"Effacer l'adresse de façon définitive de la BD !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_film.submit_btn_del_film.data:
            valeur_delete_dictionnaire = {"value_id_adresse": id_adresse_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_film_genre = """DELETE FROM t_pers_adresse WHERE fk_adresse = %(value_id_adresse)s"""
            str_sql_delete_film = """DELETE FROM t_adresse WHERE id_adresse = %(value_id_adresse)s"""
            # Manière brutale d'effacer d'abord la "fk_film", même si elle n'existe pas dans la "t_genre_film"
            # Ensuite on peut effacer le film vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_film_genre, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_film, valeur_delete_dictionnaire)

            flash(f"Adresse définitivement effacé !!", "success")
            print(f"Adresse définitivement effacé !!")

            # afficher les données
            return redirect(url_for('adresse_personnes_afficher', id_adresse_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_adresse": id_adresse_delete}
            print(id_adresse_delete, type(id_adresse_delete))

            # Requête qui affiche le film qui doit être efffacé.
            str_sql_genres_films_delete = """SELECT * FROM t_adresse WHERE id_adresse = %(value_id_adresse)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                data_adresse_delete = mydb_conn.fetchall()
                print("data_adresse_delete...", data_adresse_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "adresse/adresse_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_adresse_delete'] = data_adresse_delete

            # Le bouton pour l'action "DELETE" dans le form. "adresse_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_film_delete_wtf:
        raise ExceptionFilmDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{film_delete_wtf.__name__} ; "
                                     f"{Exception_film_delete_wtf}")

    return render_template("adresse/adresse_delete_wtf.html",
                           form_delete_film=form_delete_film,
                           btn_submit_del=btn_submit_del,
                           data_adresse_del=data_adresse_delete
                           )
