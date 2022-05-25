"""Gestion des "routes" FLASK et des données pour les entreprise.
Fichier : gestion_entreprise_crud.py
Auteur : OM 2022.04.11
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.entreprise.gestion_entreprise_wtf_forms import FormWTFUpdateEntreprise, FormWTFAddEntreprise, FormWTFDeleteEntreprise

"""Ajouter un film grâce au formulaire "entreprise_add_wtf.html"
Auteur : OM 2022.04.11
Définition d'une "route" /entreprise_add

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "ADD" d'un "film"

Paramètres : sans


Remarque :  Dans le champ "nom_entreprise_update_wtf" du formulaire "entreprise/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python dans le fichier ""
            On ne doit pas accepter un champ vide.
"""


@app.route("/entreprise_add", methods=['GET', 'POST'])
def entreprise_add_wtf():
    # Objet formulaire pour AJOUTER un film
    form_add_entreprise = FormWTFAddEntreprise()
    if request.method == "POST":
        try:
            if form_add_entreprise.validate_on_submit():
                nom_entreprise_add = form_add_entreprise.nom_entreprise_add_wtf.data
                num_entreprise_add = form_add_entreprise.num_entreprise_add_wtf.data
                email_entreprise_add = form_add_entreprise.email_entreprise_add_wtf.data

                valeurs_insertion_dictionnaire = {"value_nom_entreprise": nom_entreprise_add,
                                                  "value_num_entreprise": num_entreprise_add,
                                                  "value_email_entreprise": email_entreprise_add}

                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_entreprise = """INSERT INTO t_entreprise 
                (id_entreprise,fk_adresse,nom_entreprise,num_entreprise,email_entreprise) VALUES 
                (NULL,NULL,%(value_nom_entreprise)s,
                %(value_num_entreprise)s,%(value_email_entreprise)s) """

                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_entreprise, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion du nouveau film (id_entreprise_sel=0 => afficher tous les entreprise)
                return redirect(url_for('entreprise_personnes_afficher', id_entreprise_sel=0))

        except Exception as Exception_genres_ajouter_wtf:
            raise ExceptionGenresAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{entreprise_add_wtf.__name__} ; "
                                            f"{Exception_genres_ajouter_wtf}")

    return render_template("entreprise/entreprise_add_wtf.html", form_add_entreprise=form_add_entreprise)


"""Editer(update) un film qui a été sélectionné dans le formulaire "entreprise_personnes_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /entreprise_update

Test : exemple: cliquer sur le menu "Films/Genres" puis cliquer sur le bouton "EDIT" d'un "film"

Paramètres : sans

But : Editer(update) un genre qui a été sélectionné dans le formulaire "personnes_afficher.html"

Remarque :  Dans le champ "nom_entreprise_update_wtf" du formulaire "entreprise/films_update_wtf.html",
            le contrôle de la saisie s'effectue ici en Python.
            On ne doit pas accepter un champ vide.
"""


@app.route("/entreprise_update", methods=['GET', 'POST'])
def entreprise_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_film"
    id_entreprise_update = request.values['id_entreprise_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update_entreprise = FormWTFUpdateEntreprise()
    try:
        print(" on submit ", form_update_entreprise.validate_on_submit())
        if form_update_entreprise.validate_on_submit():
            # Récupèrer la valeur du champ depuis "personnes_update_wtf.html" après avoir cliqué sur "SUBMIT".
            nom_entreprise_update = form_update_entreprise.nom_entreprise_update_wtf.data
            num_entreprise_update = form_update_entreprise.num_entreprise_update_wtf.data
            email_entreprise_update = form_update_entreprise.email_entreprise_update_wtf.data

            valeur_update_dictionnaire = {"value_id_entreprise": id_entreprise_update,
                                          "value_nom_entreprise": nom_entreprise_update,
                                          "value_num_entreprise": num_entreprise_update,
                                          "value_email_entreprise": email_entreprise_update,
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_entreprise = """UPDATE t_entreprise SET nom_entreprise = %(value_nom_entreprise)s,
                                                            num_entreprise = %(value_num_entreprise)s,
                                                            email_entreprise = %(value_email_entreprise)s
                                                            WHERE id_entreprise = %(value_id_entreprise)s"""
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_entreprise, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Afficher seulement le film modifié, "ASC" et l'"id_entreprise_update"
            return redirect(url_for('entreprise_personnes_afficher', id_entreprise_sel=id_entreprise_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_film" et "intitule_genre" de la "t_genre"
            str_sql_id_entreprise = "SELECT * FROM t_entreprise WHERE id_entreprise = %(value_id_entreprise)s"
            valeur_select_dictionnaire = {"value_id_entreprise": id_entreprise_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_entreprise, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_entreprise = mybd_conn.fetchone()
            print("data_entreprise ", data_entreprise, " type ", type(data_entreprise), " genre ",
                  data_entreprise["nom_entreprise"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "entreprise_update_wtf.html"
            form_update_entreprise.nom_entreprise_update_wtf.data = data_entreprise["nom_entreprise"]
            form_update_entreprise.num_entreprise_update_wtf.data = data_entreprise["num_entreprise"]
            # Debug simple pour contrôler la valeur dans la console "run" de PyCharm
            print(f" duree film  ", data_entreprise["num_entreprise"], "  type ", type(data_entreprise["num_entreprise"]))
            form_update_entreprise.nom_entreprise_update_wtf.data = data_entreprise["nom_entreprise"]
            form_update_entreprise.num_entreprise_update_wtf.data = data_entreprise["num_entreprise"]
            form_update_entreprise.email_entreprise_update_wtf.data = data_entreprise["email_entreprise"]

    except Exception as Exception_entreprise_update_wtf:
        raise ExceptionEntrepriseUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{entreprise_update_wtf.__name__} ; "
                                     f"{Exception_entreprise_update_wtf}")

    return render_template("entreprise/entreprise_update_wtf.html", form_update_entreprise=form_update_entreprise)


"""Effacer(delete) un film qui a été sélectionné dans le formulaire "entreprise_personnes_afficher.html"
Auteur : OM 2022.04.11
Définition d'une "route" /entreprise_delete
    
Test : ex. cliquer sur le menu "film" puis cliquer sur le bouton "DELETE" d'un "film"
    
Paramètres : sans

Remarque :  Dans le champ "nom_entreprise_delete_wtf" du formulaire "entreprise/entreprise_delete_wtf.html"
            On doit simplement cliquer sur "DELETE"
"""


@app.route("/entreprise_delete", methods=['GET', 'POST'])
def entreprise_delete_wtf():
    # Pour afficher ou cacher les boutons "EFFACER"
    data_entreprise_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_film"
    id_entreprise_delete = request.values['id_entreprise_btn_delete_html']

    # Objet formulaire pour effacer le film sélectionné.
    form_delete_entreprise = FormWTFDeleteEntreprise()
    try:
        # Si on clique sur "ANNULER", afficher tous les entreprise.
        if form_delete_entreprise.submit_btn_annuler.data:
            return redirect(url_for("entreprise_personnes_afficher", id_entreprise_sel=0))

        if form_delete_entreprise.submit_btn_conf_del_film.data:
            # Récupère les données afin d'afficher à nouveau
            # le formulaire "entreprise/entreprise_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
            data_entreprise_delete = session['data_entreprise_delete']
            print("data_entreprise_delete ", data_entreprise_delete)

            flash(f"Effacer l'entreprise de façon définitive de la Base de données !!!", "danger")
            # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
            # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
            btn_submit_del = True

        # L'utilisateur a vraiment décidé d'effacer.
        if form_delete_entreprise.submit_btn_del_film.data:
            valeur_delete_dictionnaire = {"value_id_entreprise": id_entreprise_delete}
            print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

            str_sql_delete_fk_film_genre = """DELETE FROM t_e_personnes WHERE fk_entreprise = %(value_id_entreprise)s"""
            str_sql_delete_film = """DELETE FROM t_entreprise WHERE id_entreprise = %(value_id_entreprise)s"""
            # Manière brutale d'effacer d'abord la "fk_film", même si elle n'existe pas dans la "t_genre_film"
            # Ensuite on peut effacer le film vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_delete_fk_film_genre, valeur_delete_dictionnaire)
                mconn_bd.execute(str_sql_delete_film, valeur_delete_dictionnaire)

            flash(f"Entreprise définitivement effacé", "success")
            print(f"Entreprise définitivement effacé")

            # afficher les données
            return redirect(url_for('entreprise_personnes_afficher', id_entreprise_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_entreprise": id_entreprise_delete}
            print(id_entreprise_delete, type(id_entreprise_delete))

            # Requête qui affiche le film qui doit être efffacé.
            str_sql_genres_films_delete = """SELECT * FROM t_entreprise WHERE id_entreprise = %(value_id_entreprise)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_genres_films_delete, valeur_select_dictionnaire)
                data_entreprise_delete = mydb_conn.fetchall()
                print("data_entreprise_delete...", data_entreprise_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "entreprise/entreprise_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_entreprise_delete'] = data_entreprise_delete

            # Le bouton pour l'action "DELETE" dans le form. "entreprise_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_entreprise_delete_wtf:
        raise ExceptionFilmDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                     f"{entreprise_delete_wtf.__name__} ; "
                                     f"{Exception_entreprise_delete_wtf}")

    return render_template("entreprise/entreprise_delete_wtf.html",
                           form_delete_entreprise=form_delete_entreprise,
                           btn_submit_del=btn_submit_del,
                           data_entreprise_del=data_entreprise_delete
                           )
