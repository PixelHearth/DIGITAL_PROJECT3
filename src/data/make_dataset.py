# -*- coding: utf-8 -*-
import pandas as pd
from openpyxl import load_workbook
import os

def importation_excel(nom_fichier_excel, nom_feuille):
    assert os.path.exists(nom_fichier_excel), f"Le fichier Excel '{nom_fichier_excel}' n'existe pas."
    
    classeur = load_workbook(nom_fichier_excel, read_only=True, data_only=True)
    assert nom_feuille in classeur.sheetnames, f"La feuille '{nom_feuille}' n'existe pas dans le fichier Excel."

    feuille = classeur[nom_feuille]
    noms_de_colonnes = [cell.value for cell in feuille[1]]
    assert all(nom is not None for nom in noms_de_colonnes), "Les noms de colonnes ne peuvent pas être vides."

    ligne_data = [cell.value for cell in feuille[2]]
    df = pd.DataFrame([ligne_data], columns=noms_de_colonnes)
    return df