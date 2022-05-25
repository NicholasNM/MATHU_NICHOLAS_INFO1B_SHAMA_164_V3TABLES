"""Gestion des formulaires avec WTF pour les entreprise
Fichier : gestion_entreprise_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from wtforms.validators import Regexp
from wtforms.widgets import TextArea


class FormWTFAddEntreprise(FlaskForm):
    """
        Dans le formulaire "personnes_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_entreprise_add_wtf = StringField("Nom de l'entreprise ", validators=[Length(min=2, max=2000, message="min 2 max 20"),

                                                               ])
    num_entreprise_add_wtf  = StringField("Numéro de l'entreprise ", validators=[Length(min=2, max=2000, message="min 2 max 20"),

                                                               ])
    email_entreprise_add_wtf = StringField("Email de l'entreprise ",
                                         validators=[Length(min=2, max=2000, message="min 2 max 20"),

                                                     ])
    submit = SubmitField("Enregistrer une Entreprise")


class FormWTFUpdateEntreprise(FlaskForm):
    """
        Dans le formulaire "entreprise_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_entreprise_update_wtf = StringField("Nom de l'entreprise ",
                                         validators=[Length(min=2, max=2000, message="min 2 max 20"),

                                                     ])
    num_entreprise_update_wtf = StringField("Numéro de l'entreprise ",
                                         validators=[Length(min=2, max=2000, message="min 2 max 20"),

                                                     ])
    email_entreprise_update_wtf = StringField("Email de l'entreprise ",
                                           validators=[Length(min=2, max=2000, message="min 2 max 20"),

                                                       ])
    submit = SubmitField("Mettre à jour l' Entreprise")


class FormWTFDeleteEntreprise(FlaskForm):
    """
        Dans le formulaire "entreprise_delete_wtf.html"

        nom_entreprise_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_entreprise".
    """
    nom_entreprise_delete_wtf = StringField("Effacer cet Entreprise")
    submit_btn_del_film = SubmitField("Effacer Entreprise")
    submit_btn_conf_del_film = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
