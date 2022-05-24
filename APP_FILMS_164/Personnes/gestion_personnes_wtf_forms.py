"""
    Fichier : gestion_personnes_wtf_forms.py
    Auteur : OM 2021.03.22
    Gestion des formulaires avec WTF
"""
from flask_wtf import FlaskForm
from wtforms import StringField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, DataRequired
from wtforms.validators import Regexp


class FormWTFAjouterGenres(FlaskForm):
    """
        Dans le formulaire "personnes_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_personnes_wtf = StringField("Écrivez le nom ", validators=[Length(min=2, max=20, message="min 2 max 20"),

                                                                   ])
    prenom_personnes_wtf = StringField("Écrivez le prénom ", validators=[Length(min=2, max=20, message="min 2 max 20"),

                                                                       ])
    submit = SubmitField("Enregistrer la personne")


class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "personnes_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    nom_personnes_update_wtf = StringField("Changez le nom ", validators=[Length(min=2, max=20, message="min 2 max 20"),

                                                                          ])
    prenom_personnes_update_wtf = StringField("Changez le prénom ", validators=[Length(min=2, max=20, message="min 2 max 20"),

                                                                          ])

    submit = SubmitField("Enregistrer la modification")


class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "personnes_delete_wtf.html"

        nom_personnes_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_personnes".
    """
    nom_personnes_delete_wtf = StringField("Effacer cette personne")
    submit_btn_del = SubmitField("Effacer")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
