import pandas as pd
import ast

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
            df[nom_colonne + ' ' + nom] = df[nom_colonne].apply(lambda x: 1 if isinstance(x, list) and nom in x else (0 if pd.isna(x) else None))
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")

    return df

def convertir_listes_en_nombre(df, nom_colonne):
    # Vérifiez si la colonne spécifiée est dans le DataFrame
    if nom_colonne in df.columns:
        # Utilisez la méthode 'apply' pour appliquer la fonction lambda à chaque élément de la colonne
        df[nom_colonne] = df[nom_colonne].apply(lambda x: len(x) if isinstance(x, list) else None)
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")
    
    return df

def selectionner_colonnes(df, colonnes_a_garder):
    # Vérifiez si toutes les colonnes spécifiées sont présentes dans le DataFrame
    colonnes_presentes = [col for col in colonnes_a_garder if col in df.columns]

    if colonnes_presentes:
        # Utilisez l'opérateur [] pour sélectionner les colonnes spécifiées
        df_selectionne = df[colonnes_presentes]
        return df_selectionne
    else:
        print("Aucune des colonnes spécifiées n'est présente dans le DataFrame.")
        return df



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


def convertir_en_liste(chaine):
    try:
        return ast.literal_eval(chaine)
    except (ValueError, SyntaxError):
        return chaine
    
    
def convertir_modalites_en_listes(df, nom_colonne):
    # Vérifiez si la colonne spécifiée existe dans le DataFrame
    if nom_colonne in df.columns:
        # Appliquez la fonction de conversion à la colonne spécifiée
        df[nom_colonne] = df[nom_colonne].apply(convertir_en_liste)
        return df
    else:
        print(f"La colonne '{nom_colonne}' n'existe pas dans le DataFrame.")
        return df
