/*commentaire*/

SELECT *
FROM t_personnes;


SELECT *
FROM t_adresse;

SELECT *
FROM t_fonctions;

SELECT *
FROM t_entites;

/*Regarder tout les noms qui ont la lettre M dans la table t_personnes*/

SELECT nom_personnes
FROM t_personnes
WHERE nom_personnes REGEXP '[A-Z]M[A-Z]';



/*Regarder tout les noms qui ont pas de numero dans la table t_personnes*/
SELECT *
FROM t_personnes
WHERE num_personnes IS NULL;



/*Afficher toutes les personnes avec leurs adresses respectives*/
SELECT *
FROM t_personnes pers
left join t_pers_adresse persad ON persad.fk_personnes = pers.id_personnes
left join t_adresse ad ON persad.fk_adresse = ad.id_adresse;


/*Affiche toute personne ayant le nom de fonction "directeur"*/
SELECT *
FROM t_personnes pers
left join t_pers_fonctions persfon ON persfon.fk_personnes = pers.id_personnes
left join t_fonctions fon ON persfon.fk_fonctions = fon.id_fonctions
WHERE nom_fonction Like '%Directeur%';


/*Affiche les addresses des différentes entitées"*/
SELECT *
FROM t_entites ent
LEFT JOIN t_adresse ad ON ad.id_adresse = ent.fk_adresse;


/*Affiche un magasin en particulier - le nom de magasin étant "Anansi""*/

SELECT *
FROM t_shop sh
LEFT JOIN t_volumes vol ON sh.id_shop = vol.fk_shop
LEFT JOIN t_reservoirs res ON res.id_reservoirs = vol.fk_reservoirs
WHERE nom_shop LIKE '%Anansi%';


/*montre les différents personnes dans le département Direction*/
SELECT nom_personnes, prenom_personnes
FROM t_personnes pers
left join t_pers_fonctions persfon ON persfon.fk_personnes = pers.id_personnes
left join t_fonctions fon ON persfon.fk_fonctions = fon.id_fonctions
LEFT JOIN t_pers_departement persdep ON persdep.fk_personnes = pers.id_personnes
LEFT JOIN t_departement dep ON dep.id_departement = persdep.fk_departements
WHERE nom_departement LIKE '%Direction%';


/*montre les réservoirs ayant une quantité au dessus de 500l*/

SELECT *
FROM t_reservoirs
WHERE volume > 500;



/*montre les volumes déplacées à partir d'une certaine date*/
SELECT *
FROM t_volumes
WHERE dates > '2022-03-13';


/*test*/
SELECT *
FROM t_volumes;















