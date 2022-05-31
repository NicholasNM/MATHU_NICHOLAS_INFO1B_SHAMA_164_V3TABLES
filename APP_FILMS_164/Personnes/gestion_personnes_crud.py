"""Gestion des "routes" FLASK et des données pour les personnes_html.
Fichier : gestion_personnes_crud.py
Auteur : OM 2021.03.16
"""
from pathlib import Path

from flask import redirect
from flask import request
from flask import session
from flask import url_for

from APP_FILMS_164 import app
from APP_FILMS_164.database.database_tools import DBconnection
from APP_FILMS_164.erreurs.exceptions import *
from APP_FILMS_164.Personnes.gestion_personnes_wtf_forms import FormWTFAjouterPersonnes
from APP_FILMS_164.Personnes.gestion_personnes_wtf_forms import FormWTFDeletePersonnes
from APP_FILMS_164.Personnes.gestion_personnes_wtf_forms import FormWTFUpdatePersonnes

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /personnes_afficher
    
    Test : ex : http://127.0.0.1:5005/personnes_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_personnes_sel = 0 >> tous les personnes_html.
                id_personnes_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/personnes_afficher/<string:order_by>/<int:id_personnes_sel>", methods=['GET', 'POST'])
def personnes_afficher(order_by, id_personnes_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_personnes_sel == 0:
                    strsql_personnes_afficher = """SELECT id_personnes, nom_personnes, prenom_personnes
                    FROM t_personnes ORDER BY id_personnes ASC"""
                    mc_afficher.execute(strsql_personnes_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_personnes"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_personnes_selected_dictionnaire = {"value_id_personnes_selected": id_personnes_sel}
                    strsql_personnes_afficher = """SELECT id_personnes, nom_personnes, prenom_personnes 
                    FROM t_personnes WHERE id_personnes = %(value_id_personnes_selected)s"""

                    mc_afficher.execute(strsql_personnes_afficher, valeur_id_personnes_selected_dictionnaire)
                else:
                    strsql_personnes_afficher = """SELECT id_personnes, nom_personnes, prenom_personnes 
                    FROM t_personnes ORDER BY id_personnes  DESC"""

                    mc_afficher.execute(strsql_personnes_afficher)

                data_personnes = mc_afficher.fetchall()

                print("data_personnes ", data_personnes, " Type : ", type(data_personnes))

                # Différencier les messages si la table est vide.
                if not data_personnes and id_personnes_sel == 0:
                    flash("""La table "t_personnes" est vide. !!""", "warning")
                elif not data_personnes and id_personnes_sel > 0:
                    # Si l'utilisateur change l'id_genre dans l'URL et que le genre n'existe pas,
                    flash(f"La personne demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_personnes" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Voici les personnes dans l'entreprise!!!", "success")

        except Exception as Exception_personnes_afficher:
            raise ExceptionPersonnesAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{personnes_afficher.__name__} ; "
                                          f"{Exception_personnes_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("personnes_html/personnes_afficher.html", data=data_personnes)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /personnes_ajouter
    
    Test : ex : http://127.0.0.1:5005/personnes_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "nom_shop_html" du formulaire "personnes_html/personnes_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/personnes_ajouter", methods=['GET', 'POST'])
def personnes_ajouter_wtf():
    form = FormWTFAjouterPersonnes()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                nom_personnes_wtf = form.nom_personnes_wtf.data
                prenom_personnes_wtf = form.prenom_personnes_wtf.data
                valeurs_insertion_dictionnaire = {"value_nom_personnes": nom_personnes_wtf,
                                                  "value_prenom_personnes": prenom_personnes_wtf
                                                  }

                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_personnes = """INSERT INTO t_personnes (id_personnes, nom_personnes, prenom_personnes) 
                VALUES (NULL,%(value_nom_personnes)s,%(value_prenom_personnes)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_personnes, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('personnes_afficher', order_by='DESC', id_personnes_sel=0))

        except Exception as Exception_personnes_ajouter_wtf:
            raise ExceptionPersonnesAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{personnes_ajouter_wtf.__name__} ; "
                                            f"{Exception_personnes_ajouter_wtf}")

    return render_template("personnes_html/personnes_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /personnes_update
    
    Test : ex cliquer sur le menu "personnes_html" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "personnes_afficher.html"
    
    Remarque :  Dans le champ "nom_personnes_update_wtf" du formulaire "personnes_html/personnes_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/personnes_update", methods=['GET', 'POST'])
def personnes_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    id_personnes_update = request.values['id_personnes_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdatePersonnes()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "personnes_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            nom_personnes_update = form_update.nom_personnes_update_wtf.data
            prenom_personnes_update = form_update.prenom_personnes_update_wtf.data

            valeur_update_dictionnaire = {"value_id_personnes": id_personnes_update,
                                          "value_nom_personnes": nom_personnes_update,
                                          "value_prenom_personnes": prenom_personnes_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_personnes = """UPDATE t_personnes SET nom_personnes = %(value_nom_personnes)s, 
                                              prenom_personnes = %(value_prenom_personnes)s 
                                              WHERE id_personnes = %(value_id_personnes)s """
            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_personnes, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"value_id_personnes"
            return redirect(url_for('personnes_afficher', order_by="ASC", id_personnes_sel=id_personnes_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_personnes"
            str_sql_id_personnes = "SELECT id_personnes, nom_personnes, prenom_personnes FROM t_personnes " \
                                   "WHERE id_personnes = %(value_id_personnes)s"
            valeur_select_dictionnaire = {"value_id_personnes": id_personnes_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_personnes, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_personnes = mybd_conn.fetchone()
            print("data_personnes ", data_personnes, " type ", type(data_personnes), " entreprise ",
                  data_personnes["nom_personnes"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "personnes_update_wtf.html"
            form_update.nom_personnes_update_wtf.data = data_personnes["nom_personnes"]
            form_update.prenom_personnes_update_wtf.data = data_personnes["prenom_personnes"]

    except Exception as Exception_personnes_update_wtf:
        raise ExceptionPersonnesUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{personnes_update_wtf.__name__} ; "
                                      f"{Exception_personnes_update_wtf}")

    return render_template("personnes_html/personnes_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /personnes_delete
    
    Test : ex. cliquer sur le menu "personnes_html" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "personnes_afficher.html"
    
    Remarque :  Dans le champ "nom_personnes_delete_wtf" du formulaire "personnes_html/personnes_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/personnes_delete", methods=['GET', 'POST'])
def personnes_delete_wtf():
    data_entreprise_attribue_personnes_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_genre"
    id_personnes_delete = request.values['id_personnes_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = FormWTFDeletePersonnes()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("personnes_afficher", order_by="ASC", id_personnes_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "personnes_html/personnes_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_entreprise_attribue_personnes_delete = session['data_entreprise_attribue_personnes_delete']
                print("data_entreprise_attribue_personnes_delete ", data_entreprise_attribue_personnes_delete)

                flash(f"Effacer cette personne de façon définitive de la BD !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_personnes": id_personnes_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_entreprise_personnes = """DELETE FROM t_e_personnes WHERE fk_personnes = %(value_id_personnes)s"""
                str_sql_delete_id_personnes = """DELETE FROM t_personnes WHERE id_personnes = %(value_id_personnes)s"""
                # Manière brutale d'effacer d'abord la "fk_personnes", même si elle n'existe pas dans la "t_e_personnes"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "t_e_personnes"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_entreprise_personnes, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_id_personnes, valeur_delete_dictionnaire)

                flash(f"Personne définitivement effacé !!", "success")
                print(f"Personne définitivement effacé !!")

                # afficher les données
                return redirect(url_for('personnes_afficher', order_by="ASC", id_personnes_sel=0))
        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_personnes": id_personnes_delete}
            print(id_personnes_delete, type(id_personnes_delete))

            # Requête qui affiche tous les entreprise_personnes qui ont le genre que l'utilisateur veut effacer
            str_sql_personnes_entreprise_delete = """SELECT id_entreprise, nom_entreprise, num_entreprise, email_entreprise
                                                     FROM t_entreprise ent
                                                     INNER JOIN t_e_personnes epers ON epers.fk_entreprise = ent.id_entreprise
                                                     INNER JOIN t_personnes pers ON epers.fk_personnes = pers.id_personnes
                                                     WHERE fk_personnes = %(value_id_personnes)s
                                                     """

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_personnes_entreprise_delete, valeur_select_dictionnaire)
                data_entreprise_attribue_personnes_delete = mydb_conn.fetchall()
                print("data_entreprise_attribue_personnes_delete...", data_entreprise_attribue_personnes_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "personnes_html/personnes_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_entreprise_attribue_personnes_delete'] = data_entreprise_attribue_personnes_delete

                # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_personnes"
                str_sql_id_personnes = "SELECT id_personnes, nom_personnes FROM t_personnes " \
                                       "WHERE id_personnes = %(value_id_personnes)s"

                mydb_conn.execute(str_sql_id_personnes, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
                data_personnes = mydb_conn.fetchone()
                print("data_personnes ", data_personnes, " type ", type(data_personnes), " entreprise ",
                      data_personnes["nom_personnes"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "personnes_delete_wtf.html"

            form_delete.nom_personnes_delete_wtf.data = data_personnes["nom_personnes"]

            # Le bouton pour l'action "DELETE" dans le form. "personnes_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_personnes_delete_wtf:
        raise ExceptionPersonnesDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{personnes_delete_wtf.__name__} ; "
                                      f"{Exception_personnes_delete_wtf}")

    return render_template("personnes_html/personnes_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_entreprise_associes=data_entreprise_attribue_personnes_delete)
