import os
import pandas as pd
from openpyxl import load_workbook

def importation_excel(nom_fichier_excel, nom_feuille):
    """
    Importe les données à partir d'un fichier Excel spécifié.

    :param nom_fichier_excel: Chemin du fichier Excel.
    :type nom_fichier_excel: str
    :param nom_feuille: Nom de la feuille dans le fichier Excel.
    :type nom_feuille: str
    :return: DataFrame pandas contenant les données de la feuille spécifiée.
    :rtype: pandas.DataFrame

    :raises AssertionError: Si le fichier Excel ou la feuille spécifiée n'existe pas.
    :raises AssertionError: Si les noms de colonnes sont vides.

    Exemple d'utilisation:
    
    >>> importation_excel('mon_fichier.xlsx', 'Feuille1')
    """

    # Vérifie si le fichier Excel existe
    assert os.path.exists(nom_fichier_excel), f"Le fichier Excel '{nom_fichier_excel}' n'existe pas."

    # Charge le classeur Excel en mode lecture seule
    classeur = load_workbook(nom_fichier_excel, read_only=True, data_only=True)

    # Vérifie si la feuille spécifiée existe dans le fichier Excel
    assert nom_feuille in classeur.sheetnames, f"La feuille '{nom_feuille}' n'existe pas dans le fichier Excel."

    # Sélectionne la feuille spécifiée
    feuille = classeur[nom_feuille]

    # Récupère les noms de colonnes depuis la première ligne de la feuille
    noms_de_colonnes = [cell.value for cell in feuille[1]]

    # Vérifie si les noms de colonnes ne sont pas vides
    assert all(nom is not None for nom in noms_de_colonnes), "Les noms de colonnes ne peuvent pas être vides."

    # Récupère les données depuis la deuxième ligne de la feuille
    ligne_data = [cell.value for cell in feuille[2]]

    # Crée un DataFrame pandas avec les données et les noms de colonnes
    df = pd.DataFrame([ligne_data], columns=noms_de_colonnes)

    # Retourne le DataFrame créé
    return df
