import pandas as pd
import numpy as np


#################supprimer_lignes_na################################
#Entrée :
#Un dataframe et un nom de colonne 
#Sortie :
#Un dataframe
#Utilitée :
#Supprime toutes les lignes du dataframe qui renvoient NaN sur la 
#colonne selectionée 

def supprimer_lignes_na(df, nom_colonne):
    # Vérifiez si la colonne spécifiée est dans le DataFrame
    if nom_colonne in df.columns:
        # Utilisez la méthode dropna pour supprimer les lignes contenant des NA dans la colonne spécifiée
        df_sans_na = df.dropna(subset=[nom_colonne])
        return df_sans_na
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")
        return df

#######################remplacer_valeurs################################
#Entrée :
#Un dataframe, un nom de colonne, une valeur a et une valeur b (str, float ou int)
#Sortie :
#Un dataframe
#Utilitée :
#Remplace dans la colonne selectionnée, toutes les cases qui prennent la valeur a
#par la valeur b

def remplacer_valeurs(df, nom_colonne, valeur_a, valeur_b):
    # Vérifiez si la colonne spécifiée est dans le DataFrame
    if nom_colonne in df.columns:
        # Utilisez la méthode 'replace' pour remplacer les valeurs dans la colonne spécifiée
        df[nom_colonne] = df[nom_colonne].replace({valeur_a: valeur_b})
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")

    return df

#######################scinde_colonnes###############################
#Entrée :
#Un dataframe, un nom de colonne, une liste de str
#Sortie :
#Un dataframe
#Utilitée :
#Dans notre base, certaines colonnes renvoient une liste de modalitées
#(nord, sud, est, ouest par exemple pour les murs exposés), on va alors 
#scinder cette colonne en 4 colonnes nommées par exemple "nom_colonne nord"
#qui renvera 1 si la ligne contient "nord" dans la colonne "nom_colonne", Nan
#si la colonne renvoie un NaN, 0 sinon
#La colonne initiale "nom_colonne" est alors supprimée


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

######################compter_virgules##############################
#Entrée :
#Une chaine de caractère (de la forme "['modalité1','modalité2','ta capté'])
#Sortie :
#Un int (ou None)
#Utilitée :
#Pour traiter les colonnes type "liste de modalitées" on peut aussi juste remplacer
#la liste par le nombre de modalitées qu'elle renvoie, d'ou l'interet de cette
#fonction qui, en se basant sur le nombre de virgules, renverra NaN ou le nombre 
#de modalitées

def compter_virgules(chaine):
        if pd.notna(chaine):
            return chaine.count(',')+1 if isinstance(chaine, str) else 0
        else:
            return np.nan

####################convertir_listes_en_nombre#############################
#Entrée :
#Un dataframe et un nom de colonne
#Sortie :
#Un dataframe
#Utilitée :
#A l'aide de la fonction précédente, compte les modalitées de chaque
#ligne de la colonne selectionnée
        
def convertir_listes_en_nombre(df, nom_colonne):
    if nom_colonne in df.columns:
        df[nom_colonne] = df[nom_colonne].apply(compter_virgules)
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")
    return df

#######################selectionner_colonnes###############################
#Entrée :
#Un dataframe et une liste de noms de colonnes
#Sortie :
#Un dataframe
#Utilitée :
#Renvoie un dataframe avec uniquement les colonnes désirées

def selectionner_colonnes(df, colonnes_a_garder):
    # Vérifiez si toutes les colonnes spécifiées sont présentes dans le DataFrame
    colonnes_presentes = [col for col in colonnes_a_garder if col in df.columns]
    df_selectionne = df[colonnes_presentes]
    return df_selectionne

#####################deplacer_colonne_en_premier###########################
#Entrée :
#Un dataframe et un nom de colonne
#Sortie :
#Un dataframe
#Utilitée :
#Déplace une colonne à la première place. Ici le score DPE, pour coller au 
#programme de Guillaume

def deplacer_colonne_en_premier(df, nom_colonne):
    if nom_colonne not in df.columns:
        print(f"La colonne '{nom_colonne}' n'existe pas dans le DataFrame.")
        return df
    
    # Créez une liste de colonnes en réorganisant la colonne sélectionnée en première position
    colonnes_reorganisees = [nom_colonne] + [col for col in df.columns if col != nom_colonne]
    
    # Utilisez l'opérateur [] pour réorganiser les colonnes du DataFrame
    df_reorganise = df[colonnes_reorganisees]
    
    return df_reorganise

###################remplacer_na_par_valeur############################
#Entrée :
#Un dataframe, un nom de colonne, une valeur
#Sortie :
#Un dataframe
#Utilitée :
#Remplace tous les NaN d'une colonne par la valeur selectionnée
#

def remplacer_na_par_valeur(df, nom_colonne, valeur_remplacement):
    # Vérifiez si la colonne spécifiée est dans le DataFrame
    if nom_colonne in df.columns:
        # Utilisez la méthode 'fillna' pour remplacer les valeurs manquantes (NA) dans la colonne spécifiée
        df[nom_colonne] = df[nom_colonne].fillna(valeur_remplacement)
        return df
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")
        return df

####################count_na_per_column############################
#Entrée :
#Un dataframe
#Sortie :
#Un dataframe
#Utilitée :
#Renvoie un dataframe avec deux colonnes: une contenant le nom de chaque colonne
#de notre dataframe initiale, l'autre le nombre de nan pour chaque colonne

def count_na_per_column(df):
    # Utilisez la méthode isna() pour obtenir un DataFrame booléen où True représente les valeurs manquantes.
    is_na_df = df.isna()
    
    # Utilisez la méthode sum() sur le DataFrame booléen pour compter le nombre de valeurs manquantes par colonne.
    na_count_series = is_na_df.sum()
    
    # Créez un nouveau DataFrame à partir de la série de comptage des valeurs manquantes.
    result_df = pd.DataFrame({'Column': na_count_series.index, 'NA_Count': na_count_series.values})
    
    return result_df
