import pandas as pd
from  .fonctions_filtrage import *
chemin=""
def clean(chemin):
    
    #import dataframes
    files = ["dpe_logement", "dpe_logement1", "dpe_logement2", "dpe_logement3", "dpe_logement4", "dpe_logement5", "dpe_logement6"]

    dataframes = []

    for file in files:
        mini_df = pd.read_csv(f"{file}.csv")
        dataframes.append(mini_df)

    df=dataframes[dataframes.type_batiment_dpe=="appartement"][dataframes.version>=1]

    #columns to keep
    colonnes= ['classe_bilan_dpe', 'annee_construction_dpe','version', 'surface_habitable_logement',
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
        'surface_vitree_ouest', 'surface_vitree_est', 'traversant', 'facteur_solaire_baie_vitree', 'presence_balcon',
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
    colonnes_listes="compte"     #"scinde" to split, "compte" to count


    #put classe_bilan_dpe to first column
    df = deplacer_colonne_en_premier(df, 'classe_bilan_dpe')   

    #keep columns useful
    df = selectionner_colonnes(df, colonnes)

    #take a near modality to descrease number of modality
    #type_adjacence_principal_plancher_haut
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_haut", "comble faiblement ventilÃ©", "comble")
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_haut", "comble fortement ventilÃ©", "comble")
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_haut", "comble trÃ¨s faiblement ventilÃ©", "comble")
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_haut", "circulation avec ouverture directe sur l'extÃ©rieur", "circulation")
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_haut", "circulation sans ouverture directe sur l'extÃ©rieur", "circulation")

    #local_non_chauffe_principal_plancher_haut#
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_haut", "hall d'entrÃ©e avec dispositif de fermeture automatique", "hall")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_haut", "hall d'entrÃ©e sans dispositif de fermeture automatique", "hall")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_haut", "circulation avec ouverture directe sur l'extÃ©rieur", "circulation")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_haut", "circulation sans ouverture directe sur l'extÃ©rieur", "circulation")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_haut", "circulation avec bouche ou gaine de dÃ©senfumage ouverte en permanence", "circulation")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_haut", "comble faiblement ventilÃ©", "comble")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_haut", "comble trÃ¨s faiblement ventilÃ©", "comble")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_haut", "comble fortement ventilÃ©", "comble")

    #type_plancher_haut_deperditif
    df = remplacer_valeurs(df, "type_plancher_haut_deperditif", "autre type de plafond non rÃ©pertoriÃ©", "autre")
    df = remplacer_valeurs(df, "type_plancher_haut_deperditif", "bardeaux et remplissage", "autre")
    df = remplacer_valeurs(df, "type_plancher_haut_deperditif", "plafond bois sous solives mÃ©talliques", "autre")
    df = remplacer_valeurs(df, "type_plancher_haut_deperditif", "plafond bois sur solives mÃ©talliques", "autre")
    df = remplacer_valeurs(df, "type_plancher_haut_deperditif", "plafond entre solives mÃ©talliques avec ou sans remplissage", "autre")
    df = remplacer_valeurs(df, "type_plancher_haut_deperditif", "plafond lourd type entrevous terre-cuite, poutrelles bÃ©ton", "autre")
    df = remplacer_valeurs(df, "type_plancher_haut_deperditif", "toitures en Bac acier", "autre")

    #type_adjacence_principal_plancher_bas
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_bas", "circulation avec bouche ou gaine de désenfumage ouverte en permanence", "circulation")
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_bas", "circulation avec ouverture directe sur l'extérieur", "circulation")
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_bas", "circulation sans ouverture directe sur l'extérieur", "circulation")
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_bas", "hall d'entrée avec dispositif de fermeture automatique", "hall")
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_bas", "hall d'entrée sans dispositif de fermeture automatique", "hall")
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_bas", "espace tampon solarisé (véranda, loggia fermée)", "autres dépendances")
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_bas", "garage privé collectif", "garage")
    df = remplacer_valeurs(df, "type_adjacence_principal_plancher_bas", "cellier", "autres dépendances")

    #local_non_chauffe_principal_plancher_bas
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_bas", "circulation avec bouche ou gaine de désenfumage ouverte en permanence", "circulation")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_bas", "circulation avec ouverture directe sur l'extérieur", "circulation")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_bas", "circulation sans ouverture directe sur l'extérieur", "circulation")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_bas", "hall d'entrée avec dispositif de fermeture automatique", "hall")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_bas", "hall d'entrée sans dispositif de fermeture automatique", "hall")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_bas", "espace tampon solarisé (véranda, loggia fermée)", "autres dépendances")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_bas", "garage privé collectif", "garage")
    df = remplacer_valeurs(df, "local_non_chauffe_principal_plancher_bas", "cellier", "autres dépendances")

    #materiaux_structure_mur_exterieur
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "murs bois (rondin)", "murs en pan de bois")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "murs en pan de bois sans remplissage tout venant", "murs en pan de bois")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "murs en pan de bois avec remplissage tout venant", "murs en pan de bois")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "murs en ossature bois avec isolant en remplissage <2001", "murs en ossature bois")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "murs en ossature bois avec isolant en remplissage 2001-2005", "murs en ossature bois")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "murs en ossature bois avec isolant en remplissage â‰¥ 2006", "murs en ossature bois")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "murs en ossature bois avec remplissage tout venant", "murs en ossature bois")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "murs en ossature bois sans remplissage", "murs en ossature bois")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "bÃ©ton cellulaire", "murs en béton")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "murs en bÃ©ton banchÃ©", "murs en béton")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "murs en bÃ©ton de mÃ¢chefer", "murs en béton")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "brique terre cuite alvÃ©olaire", "autre matÃ©riau non rÃ©pertoriÃ©")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "cloison de plÃ¢tre", "autre matÃ©riau non rÃ©pertoriÃ©")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "murs en ossature bois", "autre matÃ©riau non rÃ©pertoriÃ©")
    df = remplacer_valeurs(df, "materiaux_structure_mur_exterieur", "murs sandwich bÃ©ton/isolant/bÃ©ton (sans isolation rapportÃ©e)", "autre matÃ©riau non rÃ©pertoriÃ©")

    #type_ventilation
    df = remplacer_valeurs(df, "type_ventilation", "Ventilation mécanique double flux avec échangeur", "Ventilation mécanique double flux")
    df = remplacer_valeurs(df, "type_ventilation", "Ventilation mécanique double flux sans échangeur", "Ventilation mécanique double flux")

    #type_generateur_ecs
    df = remplacer_valeurs(df, "type_generateur_ecs", "chaudiere fioul basse temperature", "chaudiere fioul")
    df = remplacer_valeurs(df, "type_generateur_ecs", "chaudiere fioul condensation", "chaudiere fioul")
    df = remplacer_valeurs(df, "type_generateur_ecs", "chaudiere fioul standard", "chaudiere fioul")
    df = remplacer_valeurs(df, "type_generateur_ecs", "chaudiere gaz basse temperature", "chaudiere gaz")
    df = remplacer_valeurs(df, "type_generateur_ecs", "chaudiere gaz condensation", "chaudiere gaz")
    df = remplacer_valeurs(df, "type_generateur_ecs", "chaudiere gaz standard", "chaudiere gaz")
    df = remplacer_valeurs(df, "type_generateur_ecs", "chaudiere gpl/butane/propane basse temperature", "chaudiere gpl/butane/propane")
    df = remplacer_valeurs(df, "type_generateur_ecs", "chaudiere gpl/butane/propane condensation", "chaudiere gpl/butane/propane")
    df = remplacer_valeurs(df, "type_generateur_ecs", "chaudiere gpl/butane/propane standard", "chaudiere gpl/butane/propane")
    df = remplacer_valeurs(df, "type_generateur_ecs", "chaudiere gpl/butane/propaneindependant", "chaudiere gpl/butane/propane")

    #type_generateur_chauffage
    df = remplacer_valeurs(df, "type_generateur_chauffage", "chaudiere fioul basse temperature", "chaudiere fioul")
    df = remplacer_valeurs(df, "type_generateur_chauffage", "chaudiere fioul condensation", "chaudiere fioul")
    df = remplacer_valeurs(df, "type_generateur_chauffage", "chaudiere fioul standard", "chaudiere fioul")
    df = remplacer_valeurs(df, "type_generateur_chauffage", "chaudiere gaz basse temperature", "chaudiere gaz")
    df = remplacer_valeurs(df, "type_generateur_chauffage", "chaudiere gaz condensation", "chaudiere gaz")
    df = remplacer_valeurs(df, "type_generateur_chauffage", "chaudiere gaz standard", "chaudiere gaz")
    df = remplacer_valeurs(df, "type_generateur_chauffage", "chaudiere gpl/butane/propane basse temperature", "chaudiere gpl/butane/propane")
    df = remplacer_valeurs(df, "type_generateur_chauffage", "chaudiere gpl/butane/propane condensation", "chaudiere gpl/butane/propane")
    df = remplacer_valeurs(df, "type_generateur_chauffage", "chaudiere gpl/butane/propane standard", "chaudiere gpl/butane/propane")


    #transform to binary data
    #list of columns to transform
    colonnesliste=["l_orientation_baie_vitree","l_local_non_chauffe_mur",
                   "l_orientation_mur_exterieur","l_local_non_chauffe_plancher_bas",
                   "l_local_non_chauffe_plancher_haut"]
    
    #modality for each column in colonneslistes
    modcolonneliste=[["nord","sud","est","ouest"],
                     ["garage","comble","cellier","hall","circulation"],
                     ["nord","sud","est","ouest"],
                     ["circulation","autre","hall","cellier","garage"],
                     ["circulation","locaux","comble","garage"]]

        
    #split columns by the comma and transform to binary
    if colonnes_listes=="scinde" :
        k=0
        for i in colonnesliste :
            df = scinde_colonnes(df, i,modcolonneliste[k])
            k+=1
    else : 
        for i in colonnesliste :
            df = convertir_listes_en_nombre(df, i)

    #replace na by "inconnu" if columns is object, else replace na by mean of the column
    df = conditional_fill_na(df)

    #convert if its possible object columns to integer
    df = convert_object_columns_to_integers(df)
    
    #delete na
    for colonne in df.columns :
        df=supprimer_lignes_na(df, colonne)
        
    # duplicate drop
    df.drop_duplicates(inplace = True)
    
    return df
clean(chemin).to_csv("df_clean.csv", index=False)
