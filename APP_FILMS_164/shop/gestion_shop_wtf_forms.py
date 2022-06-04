"""
    Fichier : gestion_shop_wtf_forms.py
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
        Dans le formulaire "shop_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_shop_wtf = StringField("Clavioter le nom du shop ", validators=[Length(min=2, max=20, message="min 2 max 20"),

                                                                   ])
    email_shop_wtf = StringField("Clavioter l'email du shop ", validators=[Length(min=2, max=20, message="min 2 max 20"),

                                                                   ])
    volumes_shop_wtf = StringField("Clavioter le volume actuel (litres) ",
                                 validators=[Length(min=2, max=20, message="min 2 max 20"),

                                             ])
    argent_shop_wtf = StringField("Clavioter l'argent actuel (shillings)",
                                  validators=[Length(min=2, max=20, message="min 2 max 20"),

                                              ])

    submit = SubmitField("Enregistrer le shop")


class FormWTFUpdateGenre(FlaskForm):
    """
        Dans le formulaire "shop_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    nom_shop_update_wtf = StringField("Clavioter le nom du shop ", validators=[Length(min=2, max=20, message="min 2 max 20"),

                                                                        ])
    email_shop_update_wtf = StringField("Clavioter l'email du shop ",
                                 validators=[Length(min=2, max=20, message="min 2 max 20"),

                                             ])
    volumes_shop_update_wtf = StringField("Clavioter le volume actuel (litres) ",
                                   validators=[Length(min=2, max=20, message="min 2 max 20"),

                                               ])
    argent_shop_update_wtf = StringField("Clavioter l'argent actuel (shillings)",
                                  validators=[Length(min=2, max=20, message="min 2 max 20"),

                                              ])
    submit = SubmitField("Update genre")


class FormWTFDeleteGenre(FlaskForm):
    """
        Dans le formulaire "shop_delete_wtf.html"

        nom_shop_delete_wtf : Champ qui reçoit la valeur du genre, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "genre".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_genre".
    """
    nom_shop_delete_wtf = StringField("Effacer ce shop")
    submit_btn_del = SubmitField("Effacer shop")
    submit_btn_conf_del = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
