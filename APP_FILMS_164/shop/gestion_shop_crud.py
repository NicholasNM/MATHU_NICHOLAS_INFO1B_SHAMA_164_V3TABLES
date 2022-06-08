"""Gestion des "routes" FLASK et des données pour les shop.
Fichier : gestion_shop_crud.py
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
from APP_FILMS_164.shop.gestion_shop_wtf_forms import FormWTFAjouterShop
from APP_FILMS_164.shop.gestion_shop_wtf_forms import FormWTFDeleteShop
from APP_FILMS_164.shop.gestion_shop_wtf_forms import FormWTFUpdateShop

"""
    Auteur : OM 2021.03.16
    Définition d'une "route" /shop_afficher
    
    Test : ex : http://127.0.0.1:5005/shop_afficher
    
    Paramètres : order_by : ASC : Ascendant, DESC : Descendant
                id_shop_sel = 0 >> tous les shop.
                id_shop_sel = "n" affiche le genre dont l'id est "n"
"""


@app.route("/shop_afficher/<string:order_by>/<int:id_shop_sel>", methods=['GET', 'POST'])
def shop_afficher(order_by, id_shop_sel):
    if request.method == "GET":
        try:
            with DBconnection() as mc_afficher:
                if order_by == "ASC" and id_shop_sel == 0:
                    strsql_shop_afficher = """SELECT id_shop, nom_shop, email_shop, volumes_shop, argent_shop
                                                FROM t_shop ORDER BY id_shop ASC"""
                    mc_afficher.execute(strsql_shop_afficher)
                elif order_by == "ASC":
                    # C'EST LA QUE VOUS ALLEZ DEVOIR PLACER VOTRE PROPRE LOGIQUE MySql
                    # la commande MySql classique est "SELECT * FROM t_genre"
                    # Pour "lever"(raise) une erreur s'il y a des erreurs sur les noms d'attributs dans la table
                    # donc, je précise les champs à afficher
                    # Constitution d'un dictionnaire pour associer l'id du genre sélectionné avec un nom de variable
                    valeur_id_shop_selected_dictionnaire = {"value_id_shop_selected": id_shop_sel}
                    strsql_shop_afficher = """SELECT id_shop, nom_shop, email_shop, volumes_shop, argent_shop
                                                FROM t_shop WHERE id_shop = %(value_id_shop_selected)s"""

                    mc_afficher.execute(strsql_shop_afficher, valeur_id_shop_selected_dictionnaire)
                else:
                    strsql_shop_afficher = """SELECT id_shop, nom_shop, email_shop, volumes_shop, argent_shop
                                                FROM t_shop ORDER BY id_shop DESC"""

                    mc_afficher.execute(strsql_shop_afficher)

                data_shop = mc_afficher.fetchall()

                print("data_shop ", data_shop, " Type : ", type(data_shop))

                # Différencier les messages si la table est vide.
                if not data_shop and id_shop_sel == 0:
                    flash("""La table "t_shop" est vide. !!""", "warning")
                elif not data_shop and id_shop_sel > 0:
                    # Si l'utilisateur change l'id_genre dans l'URL et que le genre n'existe pas,
                    flash(f"Le shop demandé n'existe pas !!", "warning")
                else:
                    # Dans tous les autres cas, c'est que la table "t_genre" est vide.
                    # OM 2020.04.09 La ligne ci-dessous permet de donner un sentiment rassurant aux utilisateurs.
                    flash(f"Données des shops affichés !!", "success")

        except Exception as Exception_shop_afficher:
            raise ExceptionShopAfficher(f"fichier : {Path(__file__).name}  ;  "
                                          f"{shop_afficher.__name__} ; "
                                          f"{Exception_shop_afficher}")

    # Envoie la page "HTML" au serveur.
    return render_template("shop/shop_afficher.html", data=data_shop)


"""
    Auteur : OM 2021.03.22
    Définition d'une "route" /shop_ajouter
    
    Test : ex : http://127.0.0.1:5005/shop_ajouter
    
    Paramètres : sans
    
    But : Ajouter un genre pour un film
    
    Remarque :  Dans le champ "nom_shop_html" du formulaire "shop/shop_ajouter.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/shop_ajouter", methods=['GET', 'POST'])
def shop_ajouter_wtf():
    form = FormWTFAjouterShop()
    if request.method == "POST":
        try:
            if form.validate_on_submit():
                nom_shop_wtf = form.nom_shop_wtf.data
                email_shop_wtf = form.email_shop_wtf.data
                volumes_shop_wtf = form.volumes_shop_wtf.data
                argent_shop_wtf = form.argent_shop_wtf.data


                valeurs_insertion_dictionnaire = {"value_nom_shop": nom_shop_wtf,
                                                  "value_email_shop": email_shop_wtf,
                                                  "value_volumes_shop": volumes_shop_wtf,
                                                  "value_argent_shop": argent_shop_wtf}

                print("valeurs_insertion_dictionnaire ", valeurs_insertion_dictionnaire)

                strsql_insert_shop = """INSERT INTO t_shop (id_shop,nom_shop,email_shop,volumes_shop,argent_shop) 
                                         VALUES (NULL,%(value_nom_shop)s,%(value_email_shop)s,%(value_volumes_shop)s,%(value_argent_shop)s) """
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(strsql_insert_shop, valeurs_insertion_dictionnaire)

                flash(f"Données insérées !!", "success")
                print(f"Données insérées !!")

                # Pour afficher et constater l'insertion de la valeur, on affiche en ordre inverse. (DESC)
                return redirect(url_for('shop_afficher', order_by='DESC', id_shop_sel=0))

        except Exception as Exception_shop_ajouter_wtf:
            raise ExceptionShopAjouterWtf(f"fichier : {Path(__file__).name}  ;  "
                                            f"{shop_ajouter_wtf.__name__} ; "
                                            f"{Exception_shop_ajouter_wtf}")

    return render_template("shop/shop_ajouter_wtf.html", form=form)


"""
    Auteur : OM 2021.03.29
    Définition d'une "route" /shop_update
    
    Test : ex cliquer sur le menu "shop" puis cliquer sur le bouton "EDIT" d'un "genre"
    
    Paramètres : sans
    
    But : Editer(update) un genre qui a été sélectionné dans le formulaire "shop_afficher.html"
    
    Remarque :  Dans le champ "nom_shop_update_wtf" du formulaire "shop/shop_update_wtf.html",
                le contrôle de la saisie s'effectue ici en Python.
                On transforme la saisie en minuscules.
                On ne doit pas accepter des valeurs vides, des valeurs avec des chiffres,
                des valeurs avec des caractères qui ne sont pas des lettres.
                Pour comprendre [A-Za-zÀ-ÖØ-öø-ÿ] il faut se reporter à la table ASCII https://www.ascii-code.com/
                Accepte le trait d'union ou l'apostrophe, et l'espace entre deux mots, mais pas plus d'une occurence.
"""


@app.route("/shop_update", methods=['GET', 'POST'])
def shop_update_wtf():
    # L'utilisateur vient de cliquer sur le bouton "EDIT". Récupère la valeur de "id_genre"
    id_shop_update = request.values['id_shop_btn_edit_html']

    # Objet formulaire pour l'UPDATE
    form_update = FormWTFUpdateShop()
    try:
        print(" on submit ", form_update.validate_on_submit())
        if form_update.validate_on_submit():
            # Récupèrer la valeur du champ depuis "shop_update_wtf.html" après avoir cliqué sur "SUBMIT".
            # Puis la convertir en lettres minuscules.
            nom_shop_update = form_update.nom_shop_update_wtf.data
            email_shop_update = form_update.email_shop_update_wtf.data
            volumes_shop_update = form_update.volumes_shop_update_wtf.data
            argent_shop_update = form_update.argent_shop_update_wtf.data

            valeur_update_dictionnaire = {"value_id_shop": id_shop_update,
                                          "value_nom_shop": nom_shop_update,
                                          "value_email_shop": email_shop_update,
                                          "value_volumes_shop": volumes_shop_update,
                                          "value_argent_shop": argent_shop_update
                                          }
            print("valeur_update_dictionnaire ", valeur_update_dictionnaire)

            str_sql_update_nom_shop = """UPDATE t_shop SET nom_shop = %(value_nom_shop)s, 
                                              email_shop = %(value_email_shop)s, 
                                              volumes_shop = %(value_volumes_shop)s, 
                                              argent_shop = %(value_argent_shop)s
                                              WHERE id_shop = %(value_id_shop)s """

            with DBconnection() as mconn_bd:
                mconn_bd.execute(str_sql_update_nom_shop, valeur_update_dictionnaire)

            flash(f"Donnée mise à jour !!", "success")
            print(f"Donnée mise à jour !!")

            # afficher et constater que la donnée est mise à jour.
            # Affiche seulement la valeur modifiée, "ASC" et l'"id_shop_update"
            return redirect(url_for('shop_afficher', order_by="ASC", id_shop_sel=id_shop_update))
        elif request.method == "GET":
            # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
            str_sql_id_shop = "SELECT id_shop, nom_shop, email_shop, volumes_shop, argent_shop FROM t_shop" \
                               " WHERE id_shop = %(value_id_shop)s"
            valeur_select_dictionnaire = {"value_id_shop": id_shop_update}
            with DBconnection() as mybd_conn:
                mybd_conn.execute(str_sql_id_shop, valeur_select_dictionnaire)
            # Une seule valeur est suffisante "fetchone()", vu qu'il n'y a qu'un seul champ "nom genre" pour l'UPDATE
            data_nom_shop = mybd_conn.fetchone()
            print("data_nom_shop ", data_nom_shop, " type ", type(data_nom_shop), " genre ",
                  data_nom_shop["nom_shop"])

            # Afficher la valeur sélectionnée dans les champs du formulaire "shop_update_wtf.html"
            form_update.nom_shop_update_wtf.data = data_nom_shop["nom_shop"]
            form_update.email_shop_update_wtf.data = data_nom_shop["email_shop"]
            form_update.volumes_shop_update_wtf.data = data_nom_shop["volumes_shop"]
            form_update.argent_shop_update_wtf.data = data_nom_shop["argent_shop"]

    except Exception as Exception_shop_update_wtf:
        raise ExceptionShopUpdateWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{shop_update_wtf.__name__} ; "
                                      f"{Exception_shop_update_wtf}")

    return render_template("shop/shop_update_wtf.html", form_update=form_update)


"""
    Auteur : OM 2021.04.08
    Définition d'une "route" /shop_delete
    
    Test : ex. cliquer sur le menu "shop" puis cliquer sur le bouton "DELETE" d'un "genre"
    
    Paramètres : sans
    
    But : Effacer(delete) un genre qui a été sélectionné dans le formulaire "shop_afficher.html"
    
    Remarque :  Dans le champ "nom_shop_delete_wtf" du formulaire "shop/shop_delete_wtf.html",
                le contrôle de la saisie est désactivée. On doit simplement cliquer sur "DELETE"
"""


@app.route("/shop_delete", methods=['GET', 'POST'])
def shop_delete_wtf():
    data_entreprise_attribue_shop_delete = None
    btn_submit_del = None
    # L'utilisateur vient de cliquer sur le bouton "DELETE". Récupère la valeur de "id_genre"
    id_shop_delete = request.values['id_shop_btn_delete_html']

    # Objet formulaire pour effacer le genre sélectionné.
    form_delete = FormWTFDeleteShop()
    try:
        print(" on submit ", form_delete.validate_on_submit())
        if request.method == "POST" and form_delete.validate_on_submit():

            if form_delete.submit_btn_annuler.data:
                return redirect(url_for("shop_afficher", order_by="ASC", id_shop_sel=0))

            if form_delete.submit_btn_conf_del.data:
                # Récupère les données afin d'afficher à nouveau
                # le formulaire "shop/shop_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                data_entreprise_attribue_shop_delete = session['data_entreprise_attribue_shop_delete']
                print("data_entreprise_attribue_shop_delete ", data_entreprise_attribue_shop_delete)

                flash(f"Effacer le shop de façon définitive de la Base de Données !!!", "danger")
                # L'utilisateur vient de cliquer sur le bouton de confirmation pour effacer...
                # On affiche le bouton "Effacer genre" qui va irrémédiablement EFFACER le genre
                btn_submit_del = True

            if form_delete.submit_btn_del.data:
                valeur_delete_dictionnaire = {"value_id_shop": id_shop_delete}
                print("valeur_delete_dictionnaire ", valeur_delete_dictionnaire)

                str_sql_delete_entreprise_shop = """DELETE FROM t_e_shop WHERE fk_shop = %(value_id_shop)s"""
                str_sql_delete_idshop = """DELETE FROM t_shop WHERE id_shop = %(value_id_shop)s"""
                # Manière brutale d'effacer d'abord la "fk_genre", même si elle n'existe pas dans la "t_genre_film"
                # Ensuite on peut effacer le genre vu qu'il n'est plus "lié" (INNODB) dans la "t_genre_film"
                with DBconnection() as mconn_bd:
                    mconn_bd.execute(str_sql_delete_entreprise_shop, valeur_delete_dictionnaire)
                    mconn_bd.execute(str_sql_delete_idshop, valeur_delete_dictionnaire)

                flash(f"Shop définitivement effacé !!", "success")
                print(f"Shop définitivement effacé !!")

                # afficher les données
                return redirect(url_for('shop_afficher', order_by="ASC", id_shop_sel=0))

        if request.method == "GET":
            valeur_select_dictionnaire = {"value_id_shop": id_shop_delete}
            print(id_shop_delete, type(id_shop_delete))

            # Requête qui affiche tous les entreprise_shop qui ont le genre que l'utilisateur veut effacer
            str_sql_shop_entrperise_delete = """SELECT id_e_shop, nom_entreprise, id_shop, nom_shop FROM t_e_shop
                                            INNER JOIN t_entreprise ON t_e_shop.fk_entreprise = t_entreprise.id_entreprise
                                            INNER JOIN t_shop ON t_e_shop.fk_shop = t_shop.id_shop
                                            WHERE fk_shop = %(value_id_shop)s"""

            with DBconnection() as mydb_conn:
                mydb_conn.execute(str_sql_shop_entrperise_delete, valeur_select_dictionnaire)
                data_entreprise_attribue_shop_delete = mydb_conn.fetchall()
                print("data_entreprise_attribue_shop_delete...", data_entreprise_attribue_shop_delete)

                # Nécessaire pour mémoriser les données afin d'afficher à nouveau
                # le formulaire "shop/shop_delete_wtf.html" lorsque le bouton "Etes-vous sur d'effacer ?" est cliqué.
                session['data_entreprise_attribue_shop_delete'] = data_entreprise_attribue_shop_delete

                # Opération sur la BD pour récupérer "id_genre" et "intitule_genre" de la "t_genre"
                str_sql_id_shop = "SELECT id_shop, nom_shop, email_shop, volumes_shop, argent_shop FROM t_shop" \
                                   " WHERE id_shop = %(value_id_shop)s"

                mydb_conn.execute(str_sql_id_shop, valeur_select_dictionnaire)
                # Une seule valeur est suffisante "fetchone()",
                # vu qu'il n'y a qu'un seul champ "nom genre" pour l'action DELETE
                data_nom_shop = mydb_conn.fetchone()
                print("data_nom_shop ", data_nom_shop, " type ", type(data_nom_shop), " entreprise ",
                      data_nom_shop["nom_shop"])

            # Afficher la valeur sélectionnée dans le champ du formulaire "shop_delete_wtf.html"
            form_delete.nom_shop_delete_wtf.data = data_nom_shop["nom_shop"]

            # Le bouton pour l'action "DELETE" dans le form. "shop_delete_wtf.html" est caché.
            btn_submit_del = False

    except Exception as Exception_shop_delete_wtf:
        raise ExceptionShopDeleteWtf(f"fichier : {Path(__file__).name}  ;  "
                                      f"{shop_delete_wtf.__name__} ; "
                                      f"{Exception_shop_delete_wtf}")

    return render_template("shop/shop_delete_wtf.html",
                           form_delete=form_delete,
                           btn_submit_del=btn_submit_del,
                           data_entreprise_associes=data_entreprise_attribue_shop_delete)
