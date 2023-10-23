import pandas as pd
import fonctions_filtrage as ff


###IMPORTATION DE LA BASE###
chemin_fichier_excel = 'BDD.xlsx'
Base = pd.read_excel(chemin_fichier_excel)


###SELECTION DES COLONNES A GARDER ET DE COMMENT LES TRAITER###
Colonnes= Base.columns.tolist()
Colonnes_listes="scinde"     #"scinde" pour scinder, "compte" pour compter


###NETTOYAGE ET MISE EN FORME DE LA BASE###

##On place la variable à prédire en première position
Base = ff.deplacer_colonne_en_premier(Base, 'classe_bilan_dpe')   

##On supprime de la base les colonnes qui ne nous servent à rien
Base = ff.selectionner_colonnes(Base, Colonnes)

##Pour chaque colonne dans la base, on fusionne les modalitées trop proches

#type_adjacence_principal_plancher_haut
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_haut", "comble faiblement ventilÃ©", "comble")
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_haut", "comble fortement ventilÃ©", "comble")
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_haut", "comble trÃ¨s faiblement ventilÃ©", "comble")
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_haut", "circulation avec ouverture directe sur l'extÃ©rieur", "circulation")
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_haut", "circulation sans ouverture directe sur l'extÃ©rieur", "circulation")

#local_non_chauffe_principal_plancher_haut#
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "hall d'entrÃ©e avec dispositif de fermeture automatique", "hall")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "hall d'entrÃ©e sans dispositif de fermeture automatique", "hall")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "circulation avec ouverture directe sur l'extÃ©rieur", "circulation")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "circulation sans ouverture directe sur l'extÃ©rieur", "circulation")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "circulation avec bouche ou gaine de dÃ©senfumage ouverte en permanence", "circulation")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "comble faiblement ventilÃ©", "comble")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "comble trÃ¨s faiblement ventilÃ©", "comble")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_haut", "comble fortement ventilÃ©", "comble")

#type_plancher_haut_deperditif
Base = ff.replace_value_in_column(Base, "type_plancher_haut_deperditif", "autre type de plafond non rÃ©pertoriÃ©", "autre")
Base = ff.replace_value_in_column(Base, "type_plancher_haut_deperditif", "bardeaux et remplissage", "autre")
Base = ff.replace_value_in_column(Base, "type_plancher_haut_deperditif", "plafond bois sous solives mÃ©talliques", "autre")
Base = ff.replace_value_in_column(Base, "type_plancher_haut_deperditif", "plafond bois sur solives mÃ©talliques", "autre")
Base = ff.replace_value_in_column(Base, "type_plancher_haut_deperditif", "plafond entre solives mÃ©talliques avec ou sans remplissage", "autre")
Base = ff.replace_value_in_column(Base, "type_plancher_haut_deperditif", "plafond lourd type entrevous terre-cuite, poutrelles bÃ©ton", "autre")
Base = ff.replace_value_in_column(Base, "type_plancher_haut_deperditif", "toitures en Bac acier", "autre")

#type_adjacence_principal_plancher_bas
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "circulation avec bouche ou gaine de désenfumage ouverte en permanence", "circulation")
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "circulation avec ouverture directe sur l'extérieur", "circulation")
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "circulation sans ouverture directe sur l'extérieur", "circulation")
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "hall d'entrée avec dispositif de fermeture automatique", "hall")
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "hall d'entrée sans dispositif de fermeture automatique", "hall")
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "espace tampon solarisé (véranda, loggia fermée)", "autres dépendances")
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "garage privé collectif", "garage")
Base = ff.remplacer_valeurs(Base, "type_adjacence_principal_plancher_bas", "cellier", "autres dépendances")

#local_non_chauffe_principal_plancher_bas
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "circulation avec bouche ou gaine de désenfumage ouverte en permanence", "circulation")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "circulation avec ouverture directe sur l'extérieur", "circulation")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "circulation sans ouverture directe sur l'extérieur", "circulation")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "hall d'entrée avec dispositif de fermeture automatique", "hall")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "hall d'entrée sans dispositif de fermeture automatique", "hall")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "espace tampon solarisé (véranda, loggia fermée)", "autres dépendances")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "garage privé collectif", "garage")
Base = ff.remplacer_valeurs(Base, "local_non_chauffe_principal_plancher_bas", "cellier", "autres dépendances")

#materiaux_structure_mur_exterieur
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "murs bois (rondin)", "murs en pan de bois")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "murs en pan de bois sans remplissage tout venant", "murs en pan de bois")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "murs en pan de bois avec remplissage tout venant", "murs en pan de bois")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "murs en ossature bois avec isolant en remplissage <2001", "murs en ossature bois")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "murs en ossature bois avec isolant en remplissage 2001-2005", "murs en ossature bois")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "murs en ossature bois avec isolant en remplissage â‰¥ 2006", "murs en ossature bois")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "murs en ossature bois avec remplissage tout venant", "murs en ossature bois")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "murs en ossature bois sans remplissage", "murs en ossature bois")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "bÃ©ton cellulaire", "murs en béton")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "murs en bÃ©ton banchÃ©", "murs en béton")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "murs en bÃ©ton de mÃ¢chefer", "murs en béton")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "brique terre cuite alvÃ©olaire", "autre matÃ©riau non rÃ©pertoriÃ©")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "cloison de plÃ¢tre", "autre matÃ©riau non rÃ©pertoriÃ©")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "murs en ossature bois", "autre matÃ©riau non rÃ©pertoriÃ©")
Base = ff.replace_value_in_column(Base, "materiaux_structure_mur_exterieur", "murs sandwich bÃ©ton/isolant/bÃ©ton (sans isolation rapportÃ©e)", "autre matÃ©riau non rÃ©pertoriÃ©")

#type_ventilation
Base = ff.remplacer_valeurs(Base, "type_ventilation", "Ventilation mécanique double flux avec échangeur", "Ventilation mécanique double flux")
Base = ff.remplacer_valeurs(Base, "type_ventilation", "Ventilation mécanique double flux sans échangeur", "Ventilation mécanique double flux")

#type_generateur_ecs
Base = ff.remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere fioul basse temperature", "chaudiere fioul")
Base = ff.remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere fioul condensation", "chaudiere fioul")
Base = ff.remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere fioul standard", "chaudiere fioul")
Base = ff.remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gaz basse temperature", "chaudiere gaz")
Base = ff.remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gaz condensation", "chaudiere gaz")
Base = ff.remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gaz standard", "chaudiere gaz")
Base = ff.remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gpl/butane/propane basse temperature", "chaudiere gpl/butane/propane")
Base = ff.remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gpl/butane/propane condensation", "chaudiere gpl/butane/propane")
Base = ff.remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gpl/butane/propane standard", "chaudiere gpl/butane/propane")
Base = ff.remplacer_valeurs(Base, "type_generateur_ecs", "chaudiere gpl/butane/propaneindependant", "chaudiere gpl/butane/propane")

#type_generateur_chauffage
Base = ff.replace_value_in_column(Base, "type_generateur_chauffage", "chaudiere fioul basse temperature", "chaudiere fioul")
Base = ff.replace_value_in_column(Base, "type_generateur_chauffage", "chaudiere fioul condensation", "chaudiere fioul")
Base = ff.replace_value_in_column(Base, "type_generateur_chauffage", "chaudiere fioul standard", "chaudiere fioul")
Base = ff.replace_value_in_column(Base, "type_generateur_chauffage", "chaudiere gaz basse temperature", "chaudiere gaz")
Base = ff.replace_value_in_column(Base, "type_generateur_chauffage", "chaudiere gaz condensation", "chaudiere gaz")
Base = ff.replace_value_in_column(Base, "type_generateur_chauffage", "chaudiere gaz standard", "chaudiere gaz")
Base = ff.replace_value_in_column(Base, "type_generateur_chauffage", "chaudiere gpl/butane/propane basse temperature", "chaudiere gpl/butane/propane")
Base = ff.replace_value_in_column(Base, "type_generateur_chauffage", "chaudiere gpl/butane/propane condensation", "chaudiere gpl/butane/propane")
Base = ff.replace_value_in_column(Base, "type_generateur_chauffage", "chaudiere gpl/butane/propane standard", "chaudiere gpl/butane/propane")






##Pour les colonnes représentées par des listes de modalitées, on 
##convertit les str en liste avec la bibliothèque ast
colonnesliste=["l_orientation_baie_vitree","l_local_non_chauffe_mur",
               "l_orientation_mur_exterieur","l_local_non_chauffe_plancher_bas",
               "l_local_non_chauffe_plancher_haut"]

for i in colonnesliste :
    Base = ff.convertir_modalites_en_listes(Base, i)
    
    
    
    
##Pour les colonnes représentées par des listes de modalitées, on 
##les scindes/convertit en entier suivant la méthode choisie
if Colonnes_listes=="scinde" :
    for i in colonnesliste :
        Base = ff.ajouter_colonnes_directions(Base, i)
else : 
    for i in colonnesliste :
        Base = ff.convertir_listes_en_nombre(Base, i)

##On remplace les NA de chaque colonne par la valeur souaitée

##On supprime les lignes contenant des NA

##On sauvegarde la base nettoyée au format csv
Base.to_csv("Base_clean.csv", index=False)
