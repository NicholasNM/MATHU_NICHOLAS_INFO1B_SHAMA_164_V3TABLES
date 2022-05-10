-- OM 2021.02.17
-- FICHIER MYSQL POUR FAIRE FONCTIONNER LES EXEMPLES
-- DE REQUETES MYSQL
-- Database: zzz_xxxxx_NOM_PRENOM_INFO1X_SUJET_104_2021

-- Détection si une autre base de donnée du même nom existe

DROP DATABASE IF EXISTS zxzx_crud_tot_NOM_PRENOM_INFO1X_SUJET_164_2022;

-- Création d'un nouvelle base de donnée

CREATE DATABASE IF NOT EXISTS zxzx_crud_tot_NOM_PRENOM_INFO1X_SUJET_164_2022;

-- Utilisation de cette base de donnée

USE zxzx_crud_tot_NOM_PRENOM_INFO1X_SUJET_164_2022;
-- --------------------------------------------------------

--
-- Table structure for table `t_adresse`
--

CREATE TABLE `t_adresse` (
  `id_adresse` int(11) NOT NULL,
  `rue` varchar(255) DEFAULT NULL,
  `No` int(255) DEFAULT NULL,
  `localite` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_adresse`
--

INSERT INTO `t_adresse` (`id_adresse`, `rue`, `No`, `localite`) VALUES
(1, 'Rue de Neuchatel', 6, '1201 Geneve'),
(2, 'Chemin de Rennier', 52, '1009 Pully'),
(3, 'Le Monteiller', 17, '1071 Chexbres'),
(4, 'Rue Daubin', 31, ' 1203 Geneve'),
(5, 'Rue du Colombier', 5, '1202 Geneve'),
(6, 'Chemin des Corbillettes', 36, '1218 le Grand-Saconnex'),
(7, 'Chemin de Hauts-Tierdoz', 24, '1683 Brenles'),
(8, 'Via Gabbietta', 65, '2830 Vellerat'),
(9, 'Hauptstrasse ', 132, '1125 Monnaz'),
(10, 'Flueliweg ', 29, '3145 Koniz'),
(11, 'Eichstrasse', 6, '8045 Zurich'),
(12, 'Via Francesco Petrarca', 4, '6900  Lugano'),
(13, 'Kranzweg', 11, '8049 Zurich'),
(14, 'Im Davidsboden', 25, '4056 Basel'),
(15, 'Schleusenweg', 35, '2508 Biel'),
(16, 'Heiterweid ', 30, '6015 Luzern'),
(17, 'Hocklerweg', 10, '8041 Zurich'),
(18, 'Place des Eaux-Vives', 14, '1207 Geneve'),
(19, 'Place de la Madeleine', 10, '1204 Geneve');

-- --------------------------------------------------------

--
-- Table structure for table `t_departement`
--

CREATE TABLE `t_departement` (
  `id_departement` int(255) NOT NULL,
  `nom_departement` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_departement`
--

INSERT INTO `t_departement` (`id_departement`, `nom_departement`) VALUES
(1, 'Direction'),
(2, 'Ressources Humaines'),
(3, 'Comptabilite'),
(4, 'Marketing'),
(5, 'Logistique'),
(6, 'Commercial'),
(7, 'Juridique');

-- --------------------------------------------------------

--
-- Table structure for table `t_entites`
--

CREATE TABLE `t_entites` (
  `id_entreprise` int(255) NOT NULL,
  `fk_adresse` int(255) DEFAULT NULL,
  `nom_entreprise` varchar(255) DEFAULT NULL,
  `num_entreprise` int(255) DEFAULT NULL,
  `email_entreprise` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_entites`
--

INSERT INTO `t_entites` (`id_entreprise`, `fk_adresse`, `nom_entreprise`, `num_entreprise`, `email_entreprise`) VALUES
(1, 1, 'Shama Premier', 798956365, 'shamapremier@gmail.com'),
(2, 2, 'Shama Milk', 796855452, 'shamamilk@gmail.com'),
(3, 1, 'Direction', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `t_e_personnes`
--

CREATE TABLE `t_e_personnes` (
  `id_e_personnes` int(255) NOT NULL,
  `fk_entreprise` int(255) DEFAULT NULL,
  `fk_personnes` int(255) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_e_personnes`
--

INSERT INTO `t_e_personnes` (`id_e_personnes`, `fk_entreprise`, `fk_personnes`, `date`) VALUES
(1, 3, 1, '2022-03-07 22:00:00'),
(2, 3, 2, '2022-03-08 22:00:00'),
(3, 3, 3, '2022-03-20 22:00:00'),
(4, 3, 4, '2022-03-07 22:00:00'),
(5, 3, 5, '2022-03-18 22:00:00'),
(6, 3, 6, '2022-03-07 22:00:00'),
(7, 3, 7, '2022-03-22 22:00:00'),
(8, 1, 8, '2022-03-18 22:00:00'),
(9, 1, 9, '2022-03-20 22:00:00'),
(10, 1, 10, '2022-03-16 22:00:00'),
(11, 1, 2, '2022-02-16 22:00:00'),
(12, 1, 12, '2022-02-09 22:00:00'),
(13, 1, 13, '2022-01-31 22:00:00'),
(14, 1, 14, '2022-03-23 22:00:00'),
(15, 1, 15, '2022-02-24 22:00:00'),
(16, 2, 16, '2022-02-16 22:00:00'),
(17, 2, 17, '2022-02-07 22:00:00'),
(18, 2, 18, '2022-02-06 22:00:00'),
(19, 2, 19, '2022-02-11 22:00:00'),
(20, 2, 20, '2022-02-05 22:00:00'),
(21, 2, 21, '2022-02-10 22:00:00'),
(22, 2, 22, '2022-02-09 22:00:00'),
(23, 2, 23, '2022-02-11 22:00:00'),
(24, 2, 24, '2022-02-09 22:00:00'),
(25, 2, 25, '2022-02-21 22:00:00'),
(26, 2, 26, '2022-02-10 22:00:00'),
(27, 2, 27, '2022-02-06 22:00:00'),
(28, 2, 28, '2022-02-21 22:00:00'),
(29, 2, 29, '2022-02-16 22:00:00'),
(30, 2, 30, '2022-03-11 22:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `t_e_reservoirs`
--

CREATE TABLE `t_e_reservoirs` (
  `id_e_reservoirs` int(255) NOT NULL,
  `fk_entreprise` int(255) DEFAULT NULL,
  `fk_reservoirs` int(255) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_e_reservoirs`
--

INSERT INTO `t_e_reservoirs` (`id_e_reservoirs`, `fk_entreprise`, `fk_reservoirs`, `date`) VALUES
(1, 1, 1, '2022-04-30 13:39:09'),
(2, 1, 2, '2022-04-30 13:39:09'),
(3, 1, 3, '2022-04-30 13:39:09'),
(4, 1, 4, '2022-04-30 13:39:09'),
(5, 2, 5, '2022-04-30 13:39:09'),
(6, 2, 6, '2022-04-30 13:39:09'),
(7, 2, 7, '2022-04-30 13:39:09'),
(8, 2, 8, '2022-04-30 13:39:09'),
(9, 2, 9, '2022-04-30 13:39:09'),
(10, 2, 10, '2022-04-30 13:39:09');

-- --------------------------------------------------------

--
-- Table structure for table `t_e_shop`
--

CREATE TABLE `t_e_shop` (
  `id_e_shop` int(255) NOT NULL,
  `fk_shop` int(255) DEFAULT NULL,
  `fk_entreprise` int(255) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_e_shop`
--

INSERT INTO `t_e_shop` (`id_e_shop`, `fk_shop`, `fk_entreprise`, `date`) VALUES
(10, 1, 1, '2022-02-28 22:00:00'),
(11, 2, 1, '2022-02-28 22:00:00'),
(12, 3, 1, '2022-02-28 22:00:00'),
(13, 4, 2, '2022-03-08 22:00:00'),
(14, 5, 2, '2022-03-08 22:00:00'),
(15, 6, 2, '2022-03-08 22:00:00'),
(16, 7, 2, '2022-03-08 22:00:00'),
(17, 8, 2, '2022-03-08 22:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `t_fonctions`
--

CREATE TABLE `t_fonctions` (
  `id_fonctions` int(255) NOT NULL,
  `nom_fonction` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_fonctions`
--

INSERT INTO `t_fonctions` (`id_fonctions`, `nom_fonction`) VALUES
(1, 'Directeur'),
(2, 'Responsable RH'),
(3, 'Responsable Comptabilite'),
(4, 'Responsable Marketing'),
(5, 'Responsable Logistique'),
(6, 'Responsable Commercial'),
(7, 'Responsable Juridique'),
(8, 'Consultant'),
(9, 'Employe'),
(10, 'Apprenti');

-- --------------------------------------------------------

--
-- Table structure for table `t_personnes`
--

CREATE TABLE `t_personnes` (
  `id_personnes` int(255) NOT NULL,
  `nom_personnes` varchar(255) DEFAULT NULL,
  `prenom_personnes` varchar(255) DEFAULT NULL,
  `num_personne` int(255) DEFAULT NULL,
  `email_personne` varchar(255) DEFAULT NULL,
  `date_naissance` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_personnes`
--

INSERT INTO `t_personnes` (`id_personnes`, `nom_personnes`, `prenom_personnes`, `num_personne`, `email_personne`, `date_naissance`) VALUES
(1, 'Mathu', 'Nicholas', 793779960, 'mathu.nicholas@gmail.com', '1997-08-18 20:00:00'),
(2, 'Nicceta', 'Ricardo', 789586562, 'nicceta.ricardo@gmail.com', '1998-01-10 22:00:00'),
(3, 'Cordai', 'Thomas', 765985254, 'cordai.thomas@gmail.com', '1999-11-14 22:00:00'),
(4, 'Tschanz', 'Patrik', 745896598, 'tschanz.patrik@hotmail.com', '1985-11-09 22:00:00'),
(5, 'Barata', 'Julie', 736526598, 'batata.julie@hotmail.com', '2000-12-07 22:00:00'),
(6, 'Gates', 'Kevin', 732659895, 'gates.kevin@outlook.com', '2000-05-20 20:00:00'),
(7, 'Sloan', 'Euan', 786598568, 'euan.sloan@gmail.com', '2015-07-28 20:00:00'),
(8, 'Knowles', 'Arnold', 756542885, NULL, '2022-03-23 22:00:00'),
(9, 'Barker', 'Esha', 772046924, 'barker.esha@hotmail', '2022-03-23 22:00:00'),
(10, 'Cooley', 'Clodagh', 752827708, NULL, '2022-03-23 22:00:00'),
(11, 'Roth', 'Zoe', 723921522, NULL, '2022-03-23 22:00:00'),
(12, 'Fulton', 'Riley-James', NULL, 'fulton.james@hotmail.com', '2022-03-23 22:00:00'),
(13, 'Barr', 'Tara', 780494969, 'barr.tara@gmail.com', '2022-03-23 22:00:00'),
(14, 'Clarkson', 'Melissa', 779204038, 'clarkson.melissa@hotmail.com', '2022-03-23 22:00:00'),
(15, 'Hobbs', 'Rahima', 785858066, 'hobbs.rahima@hotmail.com', '2022-03-23 22:00:00'),
(16, 'Beltran', 'Kerry', NULL, 'beltran.kerry@hotmail.com', '2022-03-23 22:00:00'),
(17, 'Hudson', 'Vinay', 725623265, 'hudson.vinay@gmail.com', '2022-03-24 12:38:03'),
(18, 'Mercado', 'Maryam', 766589895, 'mercado.maryan@gmail.com', '2022-03-24 12:38:03'),
(19, 'Marks', 'Jay-Jay', 753244519, 'marks.jayjay@outlook.com', '2022-03-24 12:38:03'),
(20, 'Sumner', 'Lyle', 779841256, 'sumner.lyle@lolo.com', '2022-03-24 12:38:03'),
(21, 'Paterson', 'Zahid', 789589858, 'Paterson725@gmail.com', '1997-06-13 20:00:00'),
(22, 'Cannon', 'Deon', 73659598, 'Cannon756@gmail.com', '1987-03-11 22:00:00'),
(23, 'Paul', 'Ivie', 745896589, 'Paul14@gmail.com', '1984-11-14 22:00:00'),
(24, 'Reese', 'Vivien', 745856959, 'Reese753@gmail.com', '1995-06-15 20:00:00'),
(25, 'Atherton', 'Emmy', 789588895, 'Atherton4534@gmail.com', '2001-05-25 20:00:00'),
(26, 'Bailey', 'Lacy', 754256989, 'Bailey737@gmail.com', '2002-11-14 22:00:00'),
(27, 'Goodman', 'Bethaney', 775488932, 'Good7534man@gmail.com', '1995-07-21 20:00:00'),
(28, 'Naylor', 'Tre', 725011250, 'Naylor753@gmail.com', '1997-08-17 20:00:00'),
(29, 'Vargas', 'Bill', 707589631, 'Vargas123@gmail.com', '1988-03-30 20:00:00'),
(30, 'Gibbs', 'Daria', NULL, 'Gibbs85@gmail.com', '2000-12-24 22:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `t_pers_adresse`
--

CREATE TABLE `t_pers_adresse` (
  `id_pers_adresse` int(255) NOT NULL,
  `fk_adresse` int(255) DEFAULT NULL,
  `fk_personnes` int(255) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_pers_adresse`
--

INSERT INTO `t_pers_adresse` (`id_pers_adresse`, `fk_adresse`, `fk_personnes`, `date`) VALUES
(1, 1, 1, '2021-06-14 20:00:00'),
(2, 9, 2, '2021-12-15 22:00:00'),
(3, 10, 3, '2021-12-26 22:00:00'),
(4, 8, 4, '2021-12-26 22:00:00'),
(5, 14, 5, '2021-12-02 22:00:00'),
(6, 17, 6, '2021-12-22 22:00:00'),
(7, 6, 7, '2021-12-22 22:00:00'),
(8, 3, 8, '2021-12-08 22:00:00'),
(9, 17, 9, '2021-12-26 22:00:00'),
(10, 16, 10, '2021-12-19 22:00:00'),
(11, 4, 11, '2021-12-07 22:00:00'),
(12, 14, 12, '2021-12-29 22:00:00'),
(13, 2, 13, '2021-12-15 22:00:00'),
(14, 15, 14, '2021-12-13 22:00:00'),
(15, 8, 15, '2021-12-09 22:00:00'),
(16, 8, 16, '2021-12-29 22:00:00'),
(17, 18, 17, '2021-12-16 22:00:00'),
(18, 19, 18, '2021-12-21 22:00:00'),
(19, 13, 19, '2022-03-28 20:00:00'),
(20, 10, 20, '2022-01-18 22:00:00'),
(21, 10, 21, '2022-01-16 22:00:00'),
(22, 8, 22, '2021-12-31 22:00:00'),
(23, 11, 23, '2022-01-30 22:00:00'),
(24, 14, 24, '2022-01-29 22:00:00'),
(25, 16, 25, '2022-01-03 22:00:00'),
(26, 15, 26, '2022-01-07 22:00:00'),
(27, 9, 27, '2022-01-20 22:00:00'),
(28, 11, 28, '2022-01-13 22:00:00'),
(29, 10, 29, '2022-01-11 22:00:00'),
(30, 16, 30, '2022-01-09 22:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `t_pers_departement`
--

CREATE TABLE `t_pers_departement` (
  `id_pers_departement` int(255) NOT NULL,
  `fk_personnes` int(255) DEFAULT NULL,
  `fk_departements` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_pers_departement`
--

INSERT INTO `t_pers_departement` (`id_pers_departement`, `fk_personnes`, `fk_departements`) VALUES
(1, 1, 1),
(2, 2, 1),
(3, 2, 2),
(4, 3, 1),
(5, 3, 3),
(6, 4, 1),
(7, 4, 4),
(8, 5, 1),
(9, 5, 5),
(10, 6, 1),
(11, 6, 6),
(12, 7, 1),
(13, 7, 7),
(14, 8, 2),
(15, 9, 3),
(16, 10, 4),
(17, 11, 5),
(18, 12, 6),
(19, 13, 6),
(20, 14, 6),
(21, 15, 6),
(22, 16, 2),
(23, 17, 2),
(24, 18, 3),
(25, 19, 4),
(26, 20, 5),
(27, 21, 5),
(28, 22, 6),
(29, 23, 6),
(30, 24, 6),
(31, 25, 6);

-- --------------------------------------------------------

--
-- Table structure for table `t_pers_fonctions`
--

CREATE TABLE `t_pers_fonctions` (
  `id_pers_fonctions` int(255) NOT NULL,
  `fk_personnes` int(255) DEFAULT NULL,
  `fk_fonctions` int(255) DEFAULT NULL,
  `date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_pers_fonctions`
--

INSERT INTO `t_pers_fonctions` (`id_pers_fonctions`, `fk_personnes`, `fk_fonctions`, `date`) VALUES
(1, 1, 1, '2021-12-31 22:00:00'),
(2, 2, 2, '2022-01-01 22:00:00'),
(3, 3, 3, '2022-01-02 22:00:00'),
(4, 4, 4, '2021-12-31 22:00:00'),
(5, 5, 5, '2022-01-01 22:00:00'),
(6, 6, 6, '2022-01-07 22:00:00'),
(7, 7, 7, '2022-01-04 22:00:00'),
(8, 8, 8, '2022-03-28 19:45:48'),
(9, 9, 9, '2022-03-23 22:00:00'),
(10, 10, 9, '2022-03-22 22:00:00'),
(11, 11, 9, '2022-03-11 22:00:00'),
(12, 12, 9, '2022-03-28 20:02:09'),
(13, 13, 9, '2022-03-20 22:00:00'),
(14, 14, 9, '2022-03-14 22:00:00'),
(15, 15, 9, '2022-03-14 22:00:00'),
(16, 16, 9, '2022-04-12 20:00:00'),
(17, 17, 9, '2022-04-21 20:00:00'),
(18, 18, 9, '2022-04-10 20:00:00'),
(19, 19, 9, '2022-04-04 20:00:00'),
(20, 20, 9, '2022-04-14 20:00:00'),
(21, 21, 9, '2022-04-04 20:00:00'),
(22, 22, 9, '2022-04-07 20:00:00'),
(23, 23, 9, '2022-04-01 20:00:00'),
(24, 24, 10, '2022-04-03 20:00:00'),
(25, 25, 10, '2022-04-06 20:00:00');

-- --------------------------------------------------------

--
-- Table structure for table `t_reservoirs`
--

CREATE TABLE `t_reservoirs` (
  `id_reservoirs` int(255) NOT NULL,
  `fk_adresse` int(255) DEFAULT NULL,
  `nom_reservoir` varchar(255) DEFAULT NULL,
  `volume` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_reservoirs`
--

INSERT INTO `t_reservoirs` (`id_reservoirs`, `fk_adresse`, `nom_reservoir`, `volume`) VALUES
(1, 5, 'Alpha', 693),
(2, 5, 'Bravo', 899),
(3, 5, 'Charlie', 424),
(4, 6, 'Delta', 952),
(5, 6, 'Echo', 457),
(6, 6, 'Foxtrot', 230),
(7, 7, 'Golf', 691),
(8, 7, 'Hotel', 631),
(9, 9, 'India', 400),
(10, 10, 'Juliet', 620);

-- --------------------------------------------------------

--
-- Table structure for table `t_shop`
--

CREATE TABLE `t_shop` (
  `id_shop` int(255) NOT NULL,
  `fk_adresse` int(255) DEFAULT NULL,
  `nom_shop` varchar(255) DEFAULT NULL,
  `email_shop` varchar(255) DEFAULT NULL,
  `volumes_shop` int(255) DEFAULT NULL,
  `argent_shop` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_shop`
--

INSERT INTO `t_shop` (`id_shop`, `fk_adresse`, `nom_shop`, `email_shop`, `volumes_shop`, `argent_shop`) VALUES
(1, 10, 'Adroa', 'adora@shama.com', 459, 8945),
(2, 11, 'Anansi', 'anansi@shama.com', 684, 795),
(3, 12, 'Bumba', 'bumba@shama.com', 746, 9862),
(4, 13, 'Kaang', 'kaang@shama.com', 659, 598),
(5, 14, 'Anubis', 'anubis@shama.com', 359, 2645),
(6, 15, 'Gu', 'gu@shama.com', 628, 498),
(7, 16, 'Mami Wata', 'mamiwata@shama.com', 846, 259),
(8, 17, 'Nana-Buluku', 'nana-buluku@shama.com', 35, 249);

-- --------------------------------------------------------

--
-- Table structure for table `t_volumes`
--

CREATE TABLE `t_volumes` (
  `id_volumes` int(255) NOT NULL,
  `fk_shop` int(255) DEFAULT NULL,
  `fk_reservoirs` int(255) DEFAULT NULL,
  `volumes` int(255) DEFAULT NULL,
  `dates` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `t_volumes`
--

INSERT INTO `t_volumes` (`id_volumes`, `fk_shop`, `fk_reservoirs`, `volumes`, `dates`) VALUES
(1, 1, 1, 154, '2022-03-13 22:00:00'),
(2, 5, 2, 516, '2021-12-15 22:00:00'),
(3, 2, 8, 256, '2021-10-04 20:00:00'),
(4, 7, 5, 96, '2022-03-13 22:00:00'),
(5, 6, 2, 685, '2021-12-19 22:00:00'),
(6, 3, 7, 186, '2021-09-21 20:00:00'),
(7, 8, 5, 75, '2021-06-16 20:00:00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `t_adresse`
--
ALTER TABLE `t_adresse`
  ADD PRIMARY KEY (`id_adresse`);

--
-- Indexes for table `t_departement`
--
ALTER TABLE `t_departement`
  ADD PRIMARY KEY (`id_departement`);

--
-- Indexes for table `t_entites`
--
ALTER TABLE `t_entites`
  ADD PRIMARY KEY (`id_entreprise`),
  ADD KEY `fk_adresse` (`fk_adresse`);

--
-- Indexes for table `t_e_personnes`
--
ALTER TABLE `t_e_personnes`
  ADD PRIMARY KEY (`id_e_personnes`),
  ADD KEY `fk_entreprise` (`fk_entreprise`),
  ADD KEY `fk_personnes` (`fk_personnes`);

--
-- Indexes for table `t_e_reservoirs`
--
ALTER TABLE `t_e_reservoirs`
  ADD PRIMARY KEY (`id_e_reservoirs`),
  ADD KEY `fk_entreprise` (`fk_entreprise`),
  ADD KEY `fk_reservoirs` (`fk_reservoirs`);

--
-- Indexes for table `t_e_shop`
--
ALTER TABLE `t_e_shop`
  ADD PRIMARY KEY (`id_e_shop`),
  ADD KEY `fk_shop` (`fk_shop`),
  ADD KEY `fk_entreprise` (`fk_entreprise`);

--
-- Indexes for table `t_fonctions`
--
ALTER TABLE `t_fonctions`
  ADD PRIMARY KEY (`id_fonctions`);

--
-- Indexes for table `t_personnes`
--
ALTER TABLE `t_personnes`
  ADD PRIMARY KEY (`id_personnes`);

--
-- Indexes for table `t_pers_adresse`
--
ALTER TABLE `t_pers_adresse`
  ADD PRIMARY KEY (`id_pers_adresse`),
  ADD KEY `fk_adresse` (`fk_adresse`),
  ADD KEY `fk_reservoirs` (`fk_personnes`);

--
-- Indexes for table `t_pers_departement`
--
ALTER TABLE `t_pers_departement`
  ADD PRIMARY KEY (`id_pers_departement`),
  ADD KEY `fk_personnes` (`fk_personnes`),
  ADD KEY `fk_departements` (`fk_departements`);

--
-- Indexes for table `t_pers_fonctions`
--
ALTER TABLE `t_pers_fonctions`
  ADD PRIMARY KEY (`id_pers_fonctions`),
  ADD KEY `fk_personnes` (`fk_personnes`),
  ADD KEY `fk_fonctions` (`fk_fonctions`);

--
-- Indexes for table `t_reservoirs`
--
ALTER TABLE `t_reservoirs`
  ADD PRIMARY KEY (`id_reservoirs`),
  ADD KEY `fk_adresse` (`fk_adresse`);

--
-- Indexes for table `t_shop`
--
ALTER TABLE `t_shop`
  ADD PRIMARY KEY (`id_shop`),
  ADD KEY `fk_adresse` (`fk_adresse`);

--
-- Indexes for table `t_volumes`
--
ALTER TABLE `t_volumes`
  ADD PRIMARY KEY (`id_volumes`),
  ADD KEY `fk_shop` (`fk_shop`),
  ADD KEY `fk_reservoirs` (`fk_reservoirs`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `t_adresse`
--
ALTER TABLE `t_adresse`
  MODIFY `id_adresse` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `t_departement`
--
ALTER TABLE `t_departement`
  MODIFY `id_departement` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `t_entites`
--
ALTER TABLE `t_entites`
  MODIFY `id_entreprise` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `t_e_personnes`
--
ALTER TABLE `t_e_personnes`
  MODIFY `id_e_personnes` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT for table `t_e_reservoirs`
--
ALTER TABLE `t_e_reservoirs`
  MODIFY `id_e_reservoirs` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `t_e_shop`
--
ALTER TABLE `t_e_shop`
  MODIFY `id_e_shop` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- AUTO_INCREMENT for table `t_fonctions`
--
ALTER TABLE `t_fonctions`
  MODIFY `id_fonctions` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `t_personnes`
--
ALTER TABLE `t_personnes`
  MODIFY `id_personnes` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT for table `t_pers_adresse`
--
ALTER TABLE `t_pers_adresse`
  MODIFY `id_pers_adresse` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
--
-- AUTO_INCREMENT for table `t_pers_departement`
--
ALTER TABLE `t_pers_departement`
  MODIFY `id_pers_departement` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
--
-- AUTO_INCREMENT for table `t_pers_fonctions`
--
ALTER TABLE `t_pers_fonctions`
  MODIFY `id_pers_fonctions` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
--
-- AUTO_INCREMENT for table `t_reservoirs`
--
ALTER TABLE `t_reservoirs`
  MODIFY `id_reservoirs` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `t_shop`
--
ALTER TABLE `t_shop`
  MODIFY `id_shop` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
--
-- AUTO_INCREMENT for table `t_volumes`
--
ALTER TABLE `t_volumes`
  MODIFY `id_volumes` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `t_entites`
--
ALTER TABLE `t_entites`
  ADD CONSTRAINT `t_entites_ibfk_1` FOREIGN KEY (`fk_adresse`) REFERENCES `t_adresse` (`id_adresse`);

--
-- Constraints for table `t_e_personnes`
--
ALTER TABLE `t_e_personnes`
  ADD CONSTRAINT `t_e_personnes_ibfk_1` FOREIGN KEY (`fk_entreprise`) REFERENCES `t_entites` (`id_entreprise`),
  ADD CONSTRAINT `t_e_personnes_ibfk_2` FOREIGN KEY (`fk_personnes`) REFERENCES `t_personnes` (`id_personnes`);

--
-- Constraints for table `t_e_reservoirs`
--
ALTER TABLE `t_e_reservoirs`
  ADD CONSTRAINT `t_e_reservoirs_ibfk_1` FOREIGN KEY (`fk_entreprise`) REFERENCES `t_entites` (`id_entreprise`),
  ADD CONSTRAINT `t_e_reservoirs_ibfk_2` FOREIGN KEY (`fk_reservoirs`) REFERENCES `t_reservoirs` (`id_reservoirs`);

--
-- Constraints for table `t_e_shop`
--
ALTER TABLE `t_e_shop`
  ADD CONSTRAINT `t_e_shop_ibfk_1` FOREIGN KEY (`fk_shop`) REFERENCES `t_shop` (`id_shop`),
  ADD CONSTRAINT `t_e_shop_ibfk_2` FOREIGN KEY (`fk_entreprise`) REFERENCES `t_entites` (`id_entreprise`);

--
-- Constraints for table `t_pers_adresse`
--
ALTER TABLE `t_pers_adresse`
  ADD CONSTRAINT `t_pers_adresse_ibfk_1` FOREIGN KEY (`fk_adresse`) REFERENCES `t_adresse` (`id_adresse`),
  ADD CONSTRAINT `t_pers_adresse_ibfk_2` FOREIGN KEY (`fk_personnes`) REFERENCES `t_personnes` (`id_personnes`);

--
-- Constraints for table `t_pers_departement`
--
ALTER TABLE `t_pers_departement`
  ADD CONSTRAINT `t_pers_departement_ibfk_1` FOREIGN KEY (`fk_personnes`) REFERENCES `t_personnes` (`id_personnes`),
  ADD CONSTRAINT `t_pers_departement_ibfk_2` FOREIGN KEY (`fk_departements`) REFERENCES `t_departement` (`id_departement`);

--
-- Constraints for table `t_pers_fonctions`
--
ALTER TABLE `t_pers_fonctions`
  ADD CONSTRAINT `t_pers_fonctions_ibfk_1` FOREIGN KEY (`fk_personnes`) REFERENCES `t_personnes` (`id_personnes`),
  ADD CONSTRAINT `t_pers_fonctions_ibfk_2` FOREIGN KEY (`fk_fonctions`) REFERENCES `t_fonctions` (`id_fonctions`);

--
-- Constraints for table `t_reservoirs`
--
ALTER TABLE `t_reservoirs`
  ADD CONSTRAINT `t_reservoirs_ibfk_1` FOREIGN KEY (`fk_adresse`) REFERENCES `t_adresse` (`id_adresse`);

--
-- Constraints for table `t_shop`
--
ALTER TABLE `t_shop`
  ADD CONSTRAINT `t_shop_ibfk_1` FOREIGN KEY (`fk_adresse`) REFERENCES `t_adresse` (`id_adresse`);

--
-- Constraints for table `t_volumes`
--
ALTER TABLE `t_volumes`
  ADD CONSTRAINT `t_volumes_ibfk_1` FOREIGN KEY (`fk_shop`) REFERENCES `t_shop` (`id_shop`),
  ADD CONSTRAINT `t_volumes_ibfk_2` FOREIGN KEY (`fk_reservoirs`) REFERENCES `t_reservoirs` (`id_reservoirs`);
