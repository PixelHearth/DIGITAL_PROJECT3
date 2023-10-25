import pandas as pd
import ast
import numpy as np

def supprimer_lignes_na(df, nom_colonne):
    # Vérifiez si la colonne spécifiée est dans le DataFrame
    if nom_colonne in df.columns:
        # Utilisez la méthode dropna pour supprimer les lignes contenant des NA dans la colonne spécifiée
        df_sans_na = df.dropna(subset=[nom_colonne])
        return df_sans_na
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")
        return df


def remplacer_valeurs(df, nom_colonne, valeur_a, valeur_b):
    # Vérifiez si la colonne spécifiée est dans le DataFrame
    if nom_colonne in df.columns:
        # Utilisez la méthode 'replace' pour remplacer les valeurs dans la colonne spécifiée
        df[nom_colonne] = df[nom_colonne].replace({valeur_a: valeur_b})
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")

    return df



def scinde_colonnes(df, nom_colonne, noms_colonnes_personnalisees):
    # Vérifiez si la colonne spécifiée est dans le DataFrame
    if nom_colonne in df.columns:
        # Créez de nouvelles colonnes vides avec les noms spécifiés dans la liste
        for nom in noms_colonnes_personnalisees:
            df[nom_colonne + ' ' + nom] = df[nom_colonne].apply(lambda x: 1 if isinstance(x, str) and nom in x else (0 if not pd.isna(x) else None))
        df = df.drop(columns=[nom_colonne])
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")

    return df

def compter_virgules(chaine):
        if pd.notna(chaine):
            return chaine.count(',')+1 if isinstance(chaine, str) else 0
        else:
            return np.nan
        
def convertir_listes_en_nombre(df, nom_colonne):
    if nom_colonne in df.columns:
        df[nom_colonne] = df[nom_colonne].apply(compter_virgules)
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")
    return df

def selectionner_colonnes(df, colonnes_a_garder):
    # Vérifiez si toutes les colonnes spécifiées sont présentes dans le DataFrame
    colonnes_presentes = [col for col in colonnes_a_garder if col in df.columns]
    df_selectionne = df[colonnes_presentes]
    return df_selectionne




def deplacer_colonne_en_premier(df, nom_colonne):
    if nom_colonne not in df.columns:
        print(f"La colonne '{nom_colonne}' n'existe pas dans le DataFrame.")
        return df
    
    # Créez une liste de colonnes en réorganisant la colonne sélectionnée en première position
    colonnes_reorganisees = [nom_colonne] + [col for col in df.columns if col != nom_colonne]
    
    # Utilisez l'opérateur [] pour réorganiser les colonnes du DataFrame
    df_reorganise = df[colonnes_reorganisees]
    
    return df_reorganise


def remplacer_na_par_valeur(df, nom_colonne, valeur_remplacement):
    # Vérifiez si la colonne spécifiée est dans le DataFrame
    if nom_colonne in df.columns:
        # Utilisez la méthode 'fillna' pour remplacer les valeurs manquantes (NA) dans la colonne spécifiée
        df[nom_colonne] = df[nom_colonne].fillna(valeur_remplacement)
        return df
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")
        return df


def count_na_per_column(df):
    # Utilisez la méthode isna() pour obtenir un DataFrame booléen où True représente les valeurs manquantes.
    is_na_df = df.isna()
    
    # Utilisez la méthode sum() sur le DataFrame booléen pour compter le nombre de valeurs manquantes par colonne.
    na_count_series = is_na_df.sum()
    
    # Créez un nouveau DataFrame à partir de la série de comptage des valeurs manquantes.
    result_df = pd.DataFrame({'Column': na_count_series.index, 'NA_Count': na_count_series.values})
    
    return result_df
