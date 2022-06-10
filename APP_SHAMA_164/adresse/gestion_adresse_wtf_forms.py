"""Gestion des formulaires avec WTF pour les adresse
Fichier : gestion_adresse_wtf_forms.py
Auteur : OM 2022.04.11

"""
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField
from wtforms import SubmitField
from wtforms.validators import Length, InputRequired, NumberRange, DataRequired
from wtforms.validators import Regexp
from wtforms.widgets import TextArea


class FormWTFAddAdresse(FlaskForm):
    """
        Dans le formulaire "genres_ajouter_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """
    #rue_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    rue_add_wtf = StringField("Nom de la Rue ", validators=[Length(min=2, max=2000, message="min 2 max 20"),
                                                            Regexp(rue_regexp,
                                                                   #message="Pas de chiffres, de caractères "
                                                                           #"spéciaux, "
                                                                           #"d'espace à double, de double "
                                                                           #"apostrophe, de double trait union")
                                                               ])
    #numero_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"
    numero_add_wtf = StringField("Numéro d'appartement/maison ", validators=[Length(min=2, max=2000, message="min 2 max 20"),
                                                                             #Regexp(numero_regexp,
                                                                                    #message="Pas de chiffres, de caractères "
                                                                                            #"spéciaux, "
                                                                                            #"d'espace à double, de double "
                                                                                            #"apostrophe, de double trait union")
                                                                              ])

    #numero_regexp = "^([A-Z]|[a-zÀ-ÖØ-öø-ÿ])[A-Za-zÀ-ÖØ-öø-ÿ]*['\- ]?[A-Za-zÀ-ÖØ-öø-ÿ]+$"                                                           ])
    localite_add_wtf = StringField("Localité (NPA) ", validators=[Length(min=2, max=2000, message="min 2 max 20"),
                                                                  # Regexp(numero_regexp,
                                                                  # message="Pas de chiffres, de caractères "
                                                                  # "spéciaux, "
                                                                  # "d'espace à double, de double "
                                                                  # "apostrophe, de double trait union")
                                                               ])

    submit = SubmitField("Enregistrer l'adresse")


class FormWTFUpdateAdresse(FlaskForm):
    """
        Dans le formulaire "adresse_update_wtf.html" on impose que le champ soit rempli.
        Définition d'un "bouton" submit avec un libellé personnalisé.
    """

    rue_update_wtf = StringField("Nom de la Rue ", validators=[Length(min=2, max=2000, message="min 2 max 20"),

                                                            ])
    numero_update_wtf = StringField("Numéro d'appartement/maison ", validators=[Length(min=2, max=2000,
                                                                                       message="min 2 max 20"), ])

    localite_update_wtf = StringField("Localité (NPA) ", validators=[Length(min=2, max=2000, message="min 2 max 20"),

                                                                  ])
    submit = SubmitField("Update adresse")


class FormWTFDeleteAdresse(FlaskForm):
    """
        Dans le formulaire "adresse_delete_wtf.html"

        nom_adresse_delete_wtf : Champ qui reçoit la valeur du film, lecture seule. (readonly=true)
        submit_btn_del : Bouton d'effacement "DEFINITIF".
        submit_btn_conf_del : Bouton de confirmation pour effacer un "film".
        submit_btn_annuler : Bouton qui permet d'afficher la table "t_film".
    """
    nom_adresse_delete_wtf = StringField("Effacer cet adresse")
    submit_btn_del_film = SubmitField("Effacer Adresse")
    submit_btn_conf_del_film = SubmitField("Etes-vous sur d'effacer ?")
    submit_btn_annuler = SubmitField("Annuler")
