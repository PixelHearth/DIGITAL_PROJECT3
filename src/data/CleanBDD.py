import pandas as pd
from  .fonctions_filtrage import *

def clean(chemin):
    ###IMPORTATION DE LA BASE###
    try:
        Base = pd.read_excel(chemin)
    except:
        Base = pd.read_csv(chemin)

    ###SELECTION DES COLONNES A GARDER ET DE COMMENT LES TRAITER###
    Colonnes= ['classe_bilan_dpe', 'annee_construction_dpe','version', 'surface_habitable_logement',
        'type_installation_chauffage', 'type_energie_chauffage',
        'type_generateur_chauffage', 'type_generateur_chauffage_anciennete',
        'nb_generateur_chauffage', 'nb_installation_chauffage',
        'type_generateur_climatisation',
        'type_generateur_climatisation_anciennete', 'type_installation_ecs',
        'type_energie_ecs', 'type_generateur_ecs',
        'type_generateur_ecs_anciennete', 'ecs_solaire', 'nb_generateur_ecs',
        'nb_installation_ecs', 'plusieurs_facade_exposee', 'type_ventilation',
        'type_production_energie_renouvelable', 'type_vitrage',
        'type_materiaux_menuiserie', 'type_gaz_lame', 'type_fermeture',
        'vitrage_vir', 'surface_vitree_nord', 'surface_vitree_sud',
        'surface_vitree_ouest', 'surface_vitree_est', 'traversant',
        'u_baie_vitree', 'facteur_solaire_baie_vitree', 'presence_balcon',
        'l_orientation_baie_vitree', 'type_isolation_mur_exterieur',
        'materiaux_structure_mur_exterieur',
        'epaisseur_structure_mur_exterieur', 'surface_mur_totale',
        'surface_mur_exterieur', 'surface_mur_deperditif',
        'local_non_chauffe_principal_mur', 'l_orientation_mur_exterieur',
        'type_isolation_plancher_bas', 'type_plancher_bas_deperditif',
        'surface_plancher_bas_totale', 'surface_plancher_bas_deperditif',
        'local_non_chauffe_principal_plancher_bas',
        'type_adjacence_principal_plancher_bas', 'type_isolation_plancher_haut',
        'type_plancher_haut_deperditif', 'surface_plancher_haut_totale',
        'surface_plancher_haut_deperditif',
        'local_non_chauffe_principal_plancher_haut',
        'type_adjacence_principal_plancher_haut', 'type_porte', 'surface_porte',
        'classe_inertie']
    Colonnes_listes="compte"     #"scinde" pour scinder, "compte" pour compter


    ###NETTOYAGE ET MISE EN FORME DE LA BASE###

    ##On place la variable à prédire en première position
    Base = deplacer_colonne_en_premier(Base, 'classe_bilan_dpe')   

    ##On supprime de la base les colonnes qui ne nous servent à rien
    Base = selectionner_colonnes(Base, Colonnes)

    ##Pour chaque colonne dans la base, on fusionne les modalitées trop proches

    #type_adjacence_principal_plancher_haut
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_haut", "comble faiblement ventilÃ©", "comble")
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_haut", "comble fortement ventilÃ©", "comble")
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_haut", "comble trÃ¨s faiblement ventilÃ©", "comble")
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_haut", "circulation avec ouverture directe sur l'extÃ©rieur", "circulation")
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_haut", "circulation sans ouverture directe sur l'extÃ©rieur", "circulation")

    #local_non_chauffe_principal_plancher_haut#
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "hall d'entrÃ©e avec dispositif de fermeture automatique", "hall")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "hall d'entrÃ©e sans dispositif de fermeture automatique", "hall")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "circulation avec ouverture directe sur l'extÃ©rieur", "circulation")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "circulation sans ouverture directe sur l'extÃ©rieur", "circulation")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "circulation avec bouche ou gaine de dÃ©senfumage ouverte en permanence", "circulation")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "comble faiblement ventilÃ©", "comble")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "comble trÃ¨s faiblement ventilÃ©", "comble")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "comble fortement ventilÃ©", "comble")

    #type_plancher_haut_deperditif
    Base = remplacer_valeurs(Base, "type_plancher_haut_deperditif", "autre type de plafond non rÃ©pertoriÃ©", "autre")
    Base = remplacer_valeurs(Base, "type_plancher_haut_deperditif", "bardeaux et remplissage", "autre")
    Base = remplacer_valeurs(Base, "type_plancher_haut_deperditif", "plafond bois sous solives mÃ©talliques", "autre")
    Base = remplacer_valeurs(Base, "type_plancher_haut_deperditif", "plafond bois sur solives mÃ©talliques", "autre")
    Base = remplacer_valeurs(Base, "type_plancher_haut_deperditif", "plafond entre solives mÃ©talliques avec ou sans remplissage", "autre")
    Base = remplacer_valeurs(Base, "type_plancher_haut_deperditif", "plafond lourd type entrevous terre-cuite, poutrelles bÃ©ton", "autre")
    Base = remplacer_valeurs(Base, "type_plancher_haut_deperditif", "toitures en Bac acier", "autre")

    #type_adjacence_principal_plancher_bas
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "circulation avec bouche ou gaine de désenfumage ouverte en permanence", "circulation")
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "circulation avec ouverture directe sur l'extérieur", "circulation")
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "circulation sans ouverture directe sur l'extérieur", "circulation")
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "hall d'entrée avec dispositif de fermeture automatique", "hall")
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "hall d'entrée sans dispositif de fermeture automatique", "hall")
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "espace tampon solarisé (véranda, loggia fermée)", "autres dépendances")
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "garage privé collectif", "garage")
    Base = remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "cellier", "autres dépendances")

    #local_non_chauffe_principal_plancher_bas
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "circulation avec bouche ou gaine de désenfumage ouverte en permanence", "circulation")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "circulation avec ouverture directe sur l'extérieur", "circulation")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "circulation sans ouverture directe sur l'extérieur", "circulation")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "hall d'entrée avec dispositif de fermeture automatique", "hall")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "hall d'entrée sans dispositif de fermeture automatique", "hall")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "espace tampon solarisé (véranda, loggia fermée)", "autres dépendances")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "garage privé collectif", "garage")
    Base = remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "cellier", "autres dépendances")

    #materiaux_structure_mur_exterieur
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "murs bois (rondin)", "murs en pan de bois")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "murs en pan de bois sans remplissage tout venant", "murs en pan de bois")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "murs en pan de bois avec remplissage tout venant", "murs en pan de bois")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "murs en ossature bois avec isolant en remplissage <2001", "murs en ossature bois")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "murs en ossature bois avec isolant en remplissage 2001-2005", "murs en ossature bois")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "murs en ossature bois avec isolant en remplissage â‰¥ 2006", "murs en ossature bois")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "murs en ossature bois avec remplissage tout venant", "murs en ossature bois")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "murs en ossature bois sans remplissage", "murs en ossature bois")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "bÃ©ton cellulaire", "murs en béton")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "murs en bÃ©ton banchÃ©", "murs en béton")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "murs en bÃ©ton de mÃ¢chefer", "murs en béton")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "brique terre cuite alvÃ©olaire", "autre matÃ©riau non rÃ©pertoriÃ©")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "cloison de plÃ¢tre", "autre matÃ©riau non rÃ©pertoriÃ©")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "murs en ossature bois", "autre matÃ©riau non rÃ©pertoriÃ©")
    Base = remplacer_valeurs(Base, "materiaux_structure_mur_exterieur", "murs sandwich bÃ©ton/isolant/bÃ©ton (sans isolation rapportÃ©e)", "autre matÃ©riau non rÃ©pertoriÃ©")

    #type_ventilation
    Base = remplacer_valeurs(Base, "type_ventilation", "Ventilation mécanique double flux avec échangeur", "Ventilation mécanique double flux")
    Base = remplacer_valeurs(Base, "type_ventilation", "Ventilation mécanique double flux sans échangeur", "Ventilation mécanique double flux")

    #type_generateur_ecs
    Base = remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere fioul basse temperature", "chaudiere fioul")
    Base = remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere fioul condensation", "chaudiere fioul")
    Base = remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere fioul standard", "chaudiere fioul")
    Base = remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gaz basse temperature", "chaudiere gaz")
    Base = remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gaz condensation", "chaudiere gaz")
    Base = remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gaz standard", "chaudiere gaz")
    Base = remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gpl/butane/propane basse temperature", "chaudiere gpl/butane/propane")
    Base = remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gpl/butane/propane condensation", "chaudiere gpl/butane/propane")
    Base = remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gpl/butane/propane standard", "chaudiere gpl/butane/propane")
    Base = remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gpl/butane/propaneindependant", "chaudiere gpl/butane/propane")

    #type_generateur_chauffage
    Base = remplacer_valeurs(Base, "type_generateur_chauffage", "chaudiere fioul basse temperature", "chaudiere fioul")
    Base = remplacer_valeurs(Base, "type_generateur_chauffage", "chaudiere fioul condensation", "chaudiere fioul")
    Base = remplacer_valeurs(Base, "type_generateur_chauffage", "chaudiere fioul standard", "chaudiere fioul")
    Base = remplacer_valeurs(Base, "type_generateur_chauffage", "chaudiere gaz basse temperature", "chaudiere gaz")
    Base = remplacer_valeurs(Base, "type_generateur_chauffage", "chaudiere gaz condensation", "chaudiere gaz")
    Base = remplacer_valeurs(Base, "type_generateur_chauffage", "chaudiere gaz standard", "chaudiere gaz")
    Base = remplacer_valeurs(Base, "type_generateur_chauffage", "chaudiere gpl/butane/propane basse temperature", "chaudiere gpl/butane/propane")
    Base = remplacer_valeurs(Base, "type_generateur_chauffage", "chaudiere gpl/butane/propane condensation", "chaudiere gpl/butane/propane")
    Base = remplacer_valeurs(Base, "type_generateur_chauffage", "chaudiere gpl/butane/propane standard", "chaudiere gpl/butane/propane")






    ##Pour les colonnes représentées par des listes de modalitées, on 
    ##liste les modalitées à compter
    colonnesliste=["l_orientation_baie_vitree","l_local_non_chauffe_mur",
                "l_orientation_mur_exterieur","l_local_non_chauffe_plancher_bas",
                "l_local_non_chauffe_plancher_haut"]
    modcolonneliste=[["nord","sud","est","ouest"],
                            ["garage","comble","cellier","hall","circulation"],
                            ["nord","sud","est","ouest"],
                            ["circulation","autre","hall","cellier","garage"],
                            ["circulation","locaux","comble","garage"]]


        
    ##Pour les colonnes représentées par des listes de modalitées, on 
    ##les scindes/convertit en entier suivant la méthode choisie
    if Colonnes_listes=="scinde" :
        k=0
        for i in colonnesliste :
            Base = scinde_colonnes(Base, i,modcolonneliste[k])
            k+=1
    else : 
        for i in colonnesliste :
            Base = convertir_listes_en_nombre(Base, i)

    ##On remplace les NA de chaque colonne par la valeur souaitée
    remplace = 'inconnu'
    colonnesaclean = ['type_installation_chauffage',
                'type_energie_chauffage',
                'type_generateur_chauffage',
                'type_installation_ecs',
                'type_energie_ecs',
                'type_generateur_ecs',
                'type_vitrage',
                'type_materiaux_menuiserie',
                'type_fermeture',
                'local_non_chauffe_principal_plancher_haut',
                'local_non_chauffe_principal_plancher_bas',
                'type_production_energie_renouvelable',
                'type_generateur_ecs_anciennete',
                'type_generateur_chauffage_anciennete',
                'type_plancher_bas_deperditif',
                'type_plancher_haut_deperditif',
                'type_adjacence_principal_plancher_bas',
                'type_isolation_plancher_bas',
                'type_adjacence_principal_plancher_haut',
                'type_isolation_plancher_haut',
                'type_porte',
                'type_ventilation',
                'type_gaz_lame',
                'annee_construction_dpe',
                'l_orientation_mur_exterieur nord',
                'l_orientation_mur_exterieur sud',
                'l_orientation_mur_exterieur est',
                'l_orientation_mur_exterieur ouest',
                'type_isolation_mur_exterieur',
                'l_orientation_baie_vitree nord',
                'l_orientation_baie_vitree sud',
                'l_orientation_baie_vitree est',
                'l_orientation_baie_vitree ouest',
                'presence_balcon',
                'local_non_chauffe_principal_mur']
    for colonne in colonnesaclean:
        Base=remplacer_na_par_valeur(Base, colonne, remplace)
        
    remplace = 0
    colonnesaclean = ['surface_vitree_ouest',
                    'surface_vitree_est',
                    'surface_plancher_bas_deperditif',
                    'surface_plancher_haut_deperditif',
                    'surface_vitree_nord',
                    'surface_vitree_sud',
                    'epaisseur_structure_mur_exterieur',
                    'surface_plancher_bas_totale',
                    'surface_plancher_haut_totale',
                    'surface_porte',
                    ]
    for colonne in colonnesaclean:
        Base=remplacer_na_par_valeur(Base, colonne, remplace)
    ##On supprime les colonnes contenant beaucoup trop de NA
    # tropNA=['type_generateur_climatisation',
    #         'type_generateur_climatisation_anciennete',
    #         ]
    # for colonne in tropNA:
    #     Base=Base.drop(columns=colonne)
        
        

    na=count_na_per_column(Base)
    ##On supprime les lignes contenant des NA
    for colonne in Base.columns :
        Base=supprimer_lignes_na(Base, colonne)
    Base = convert_object_columns_to_integers(Base)
    for colonne in Base.columns :
        Base=supprimer_lignes_na(Base, colonne)
    Base.drop_duplicates(inplace = False)
    ##On sauvegarde la base nettoyée au format csv
    return Base
    # Base.to_csv("C:/Users/Guillaume Baroin/Documents/M2_sep/DIGITAL_PROJECT3/data/processed/bdd_clean.csv")
