import pandas as pd
import numpy as np



def supprimer_lignes_na(df, nom_colonne):
    """
    Cette fonction prend en entrée un DataFrame et le nom d'une colonne.
    Elle retourne un nouveau DataFrame qui est le résultat de la suppression
    des lignes contenant des valeurs NaN dans la colonne spécifiée.

    Paramètres :
    - df (pandas DataFrame) : Le DataFrame à traiter.
    - nom_colonne (str) : Le nom de la colonne sur laquelle baser la suppression des lignes NaN.

    Retour :
    - pandas DataFrame : Le DataFrame résultant après la suppression des lignes contenant NaN dans la colonne spécifiée.

    Exemple :
    >>> df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]})
    >>> nom_colonne = 'A'
    >>> df_resultat = supprimer_lignes_na(df, nom_colonne)
    >>> print(df_resultat)
       A    B
    0  1.0  5.0
    1  2.0  NaN
    3  4.0  8.0
    """
    # Vérifie si la colonne spécifiée est présente dans le DataFrame
    if nom_colonne in df.columns:
        # Utilise la méthode dropna pour supprimer les lignes contenant des NaN dans la colonne spécifiée
        df_sans_na = df.dropna(subset=[nom_colonne])
        return df_sans_na
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")
        # Si la colonne n'est pas présente, retourne le DataFrame d'origine
        return df


def remplacer_valeurs(df, nom_colonne, valeur_a, valeur_b):
    """
    Cette fonction prend en entrée un DataFrame, le nom d'une colonne, une valeur à remplacer (valeur_a),
    et une valeur de remplacement (valeur_b). Elle retourne un nouveau DataFrame résultant
    du remplacement de toutes les occurrences de la valeur a par la valeur b dans la colonne spécifiée.

    Paramètres :
    - df (pandas DataFrame) : Le DataFrame à traiter.
    - nom_colonne (str) : Le nom de la colonne dans laquelle effectuer le remplacement de valeurs.
    - valeur_a (str, float, ou int) : La valeur à remplacer.
    - valeur_b (str, float, ou int) : La valeur de remplacement.

    Retour :
    - pandas DataFrame : Le DataFrame résultant après le remplacement des valeurs spécifiées.

    Exemple :
    >>> df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'a', 'c']})
    >>> nom_colonne = 'B'
    >>> valeur_a = 'a'
    >>> valeur_b = 'x'
    >>> df_resultat = remplacer_valeurs(df, nom_colonne, valeur_a, valeur_b)
    >>> print(df_resultat)
       A  B
    0  1  x
    1  2  b
    2  3  x
    3  4  c
    """
    # Vérifie si la colonne spécifiée est présente dans le DataFrame
    if nom_colonne in df.columns:
        # Utilise la méthode 'replace' pour remplacer les valeurs dans la colonne spécifiée
        df[nom_colonne] = df[nom_colonne].replace({valeur_a: valeur_b})
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")

    return df
    
def conditional_fill_na(df):
    """
    Conditional fill missing values in a DataFrame based on the data type of each column.

    For columns of type 'object', fill NaN values with the string 'unknown' ('inconnu' in French).
    For numeric columns, fill NaN values with the mean of the column.

    Args:
        df (pd.DataFrame): The DataFrame to be processed.

    Returns:
        pd.DataFrame: A new DataFrame with missing values filled based on the specified conditions.
    
    Example:
        >>> import pandas as pd
        >>> data = {'col1': [1, 2, None], 'col2': ['a', 'b', None], 'col3': [4.0, 5.0, None]}
        >>> df = pd.DataFrame(data)
        >>> df
           col1 col2  col3
        0   1.0    a   4.0
        1   2.0    b   5.0
        2   NaN  NaN   NaN
        
        >>> df = conditional_fill_na(df)
        >>> df
           col1 col2  col3
        0   1.0    a   4.0
        1   2.0    b   5.0
        2   1.5    inconnu   4.5
    """
    assert isinstance(df, pd.DataFrame), "Input must be a DataFrame"

    for column in df.columns:
        if df[column].dtype == "object":
            # For 'object' columns, fill NaN with the string 'unknown'
            df[column].fillna("unknown", inplace=True)
        else:
            # For numeric columns, fill NaN with the mean of the column
            df[column].fillna(df[column].mean(), inplace=True)

    return df

def convert_object_columns_to_integers(df):
    """
    Converts columns of type 'object' to integers if there is at least one element convertible to an integer inside,
    otherwise returns the unchanged DataFrame.
    
    Objective: Allows removing non-NaN values from a column while retaining maximum information.

    Args:
        df (pd.DataFrame): The DataFrame to be processed.

    Returns:
        pd.DataFrame: A new DataFrame with columns converted to integers, if possible.
    
    Raises:
        AssertionError: If the argument is not of type DataFrame.
        AssertionError: If the DataFrame contains non-NaN values. Use the drop_na_rows function before calling this function.
    
    Example:
        >>> import pandas as pd
        >>> data = {'col1': ['1', 'A', '2'], 'col2': ['a', 'b', 'c']}
        >>> df = pd.DataFrame(data)
        >>> df
          col1 col2
        0    1    a
        1    2    b
        2    3    c
        
        >>> df = convert_object_columns_to_integers(df)
        >>> df
          col1   col2
        0    1    a
        1  NaN    b
        2    3    c
    """
    assert isinstance(df, pd.DataFrame), "Input must be a DataFrame"
    assert df.notnull().all().all(), "No NoneType Allowed, use the drop_na_rows function"

    # Select object columns (ambiguous)
    object_columns = df.select_dtypes(include=['object']).columns

    # Iterate through each column and check elements
    for col in object_columns:
        # Initialize a counter to calculate the number of int or float elements
        count = 0
        list_numeric = []
        list_string = []

        # Iterate through the column
        for element in df[col]:
            try:
                int_value = float(element)
                count += 1
                list_numeric.append(int_value)
                list_string.append(None)
            except ValueError:
                list_numeric.append(None)
                list_string.append(element)
        
        # If there are no numeric elements, keep string values; otherwise, convert to numeric
        if count == 0:
            df[col] = list_string
        else:
            df[col] = list_numeric
            df[col] = df[col].astype(float)

    return df

def scinde_colonnes(df, nom_colonne, noms_colonnes_personnalisees):
    """
    Cette fonction prend en entrée un DataFrame, le nom d'une colonne, et une liste de noms de colonnes personnalisées.
    Elle crée de nouvelles colonnes dans le DataFrame en fonction des noms spécifiés dans la liste.
    Chaque nouvelle colonne contient des valeurs binaires indiquant la présence de la sous-chaîne correspondante dans la colonne d'origine.

    Paramètres :
    - df (pandas DataFrame) : Le DataFrame à traiter.
    - nom_colonne (str) : Le nom de la colonne à scinder.
    - noms_colonnes_personnalisees (list) : La liste des noms de colonnes personnalisées à créer.

    Retour :
    - pandas DataFrame : Le DataFrame résultant après la création des nouvelles colonnes.

    Exemple :
    >>> df = pd.DataFrame({'Tags': ['python, data', 'data science', 'java', 'python', np.nan]})
    >>> nom_colonne = 'Tags'
    >>> noms_colonnes_personnalisees = ['python', 'java', 'data']
    >>> df_resultat = scinde_colonnes(df, nom_colonne, noms_colonnes_personnalisees)
    >>> print(df_resultat)
       Tags python  Tags java  Tags data
    0    'python, data'         0         1
    1    'data science'         0         0
    2              'java'         1         0
    3            'python'         0         1
    4                NaN      None      None
    """
    # Vérifie si la colonne spécifiée est présente dans le DataFrame
    if nom_colonne in df.columns:
        # Crée de nouvelles colonnes vides avec les noms spécifiés dans la liste
        for nom in noms_colonnes_personnalisees:
            df[nom_colonne + ' ' + nom] = df[nom_colonne].apply(lambda x: 1 if isinstance(x, str) and nom in x else (0 if not pd.isna(x) else None))
        # Supprime la colonne d'origine
        df = df.drop(columns=[nom_colonne])
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")

    return df



def compter_virgules(chaine):
    """
    Cette fonction prend en entrée une chaîne de caractères représentant une liste de modalités.
    Elle renvoie le nombre de modalités dans la liste (le nombre de virgules + 1) ou None si la chaîne est NaN.

    Paramètres :
    - chaine (str) : Une chaîne de caractères représentant une liste de modalités.

    Retour :
    - int ou None : Le nombre de modalités dans la liste (le nombre de virgules + 1) ou None si la chaîne est NaN.

    Exemple :
    >>> chaine = "['modalité1','modalité2','ta capté']"
    >>> resultat = compter_virgules(chaine)
    >>> print(resultat)
    3
    """
    if pd.notna(chaine):
        return chaine.count(',') + 1 if isinstance(chaine, str) else 0
    else:
        return None


 def convertir_listes_en_nombre(df, nom_colonne):
    """
    Cette fonction prend en entrée un DataFrame et le nom d'une colonne contenant des listes de modalités.
    Elle remplace les listes par le nombre de modalités qu'elles contiennent en utilisant la fonction compter_virgules.

    Paramètres :
    - df (pandas DataFrame) : Le DataFrame à traiter.
    - nom_colonne (str) : Le nom de la colonne à convertir.

    Retour :
    - pandas DataFrame : Le DataFrame résultant après la conversion des listes en nombre de modalités.

    Exemple :
    >>> df = pd.DataFrame({'Modalites': ["['modalité1','modalité2','ta capté']", "['option1','option2']", np.nan]})
    >>> nom_colonne = 'Modalites'
    >>> df_resultat = convertir_listes_en_nombre(df, nom_colonne)
    >>> print(df_resultat)
       Modalites
    0            3
    1            2
    2         None
    """
    if nom_colonne in df.columns:
        # Applique la fonction compter_virgules à la colonne spécifiée
        df[nom_colonne] = df[nom_colonne].apply(compter_virgules)
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")

    return df

def selectionner_colonnes(df, colonnes_a_garder):
    """
    Cette fonction prend en entrée un DataFrame et une liste de noms de colonnes.
    Elle renvoie un nouveau DataFrame contenant uniquement les colonnes spécifiées.

    Paramètres :
    - df (pandas DataFrame) : Le DataFrame à traiter.
    - colonnes_a_garder (list) : La liste des noms de colonnes à conserver dans le DataFrame résultant.

    Retour :
    - pandas DataFrame : Le DataFrame résultant avec uniquement les colonnes désirées.

    Exemple :
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [True, False, True]})
    >>> colonnes_a_garder = ['A', 'C']
    >>> df_resultat = selectionner_colonnes(df, colonnes_a_garder)
    >>> print(df_resultat)
       A     C
    0  1  True
    1  2 False
    2  3  True
    """
    # Vérifie si toutes les colonnes spécifiées sont présentes dans le DataFrame
    colonnes_presentes = [col for col in colonnes_a_garder if col in df.columns]
    # Sélectionne uniquement les colonnes présentes
    df_selectionne = df[colonnes_presentes]
    return df_selectionne

def deplacer_colonne_en_premier(df, nom_colonne):
    """
    Cette fonction prend en entrée un DataFrame et le nom d'une colonne.
    Elle renvoie un nouveau DataFrame avec la colonne spécifiée déplacée en première position.

    Paramètres :
    - df (pandas DataFrame) : Le DataFrame à traiter.
    - nom_colonne (str) : Le nom de la colonne à déplacer en premier.

    Retour :
    - pandas DataFrame : Le DataFrame résultant avec la colonne déplacée en première position.

    Exemple :
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [True, False, True]})
    >>> nom_colonne = 'B'
    >>> df_resultat = deplacer_colonne_en_premier(df, nom_colonne)
    >>> print(df_resultat)
         B  A     C
    0    'a'  1  True
    1    'b'  2 False
    2    'c'  3  True
    """
    if nom_colonne in df.columns:
        # Liste des noms de colonnes
        columns = list(df.columns)
        
        # Supprimer la colonne de la liste
        columns.remove(nom_colonne)
        
        # Insérer la colonne au début de la liste
        columns.insert(0, nom_colonne)
        
        # Réorganiser le DataFrame selon la nouvelle séquence de colonnes
        df = df[columns]
        
        return df
    else:
        print(f"La colonne '{nom_colonne}' n'existe pas dans le DataFrame.")
        return df
        
def remplacer_na_par_valeur(df, nom_colonne, valeur_remplacement):
    """
    Cette fonction prend en entrée un DataFrame, le nom d'une colonne, et une valeur de remplacement.
    Elle remplace les valeurs manquantes (NA) dans la colonne spécifiée par la valeur de remplacement.

    Paramètres :
    - df (pandas DataFrame) : Le DataFrame à traiter.
    - nom_colonne (str) : Le nom de la colonne dans laquelle effectuer le remplacement.
    - valeur_remplacement : La valeur à utiliser pour remplacer les valeurs manquantes.

    Retour :
    - pandas DataFrame : Le DataFrame résultant après le remplacement des valeurs manquantes.

    Exemple :
    >>> df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': ['a', 'b', 'c', np.nan]})
    >>> nom_colonne = 'A'
    >>> valeur_remplacement = 0
    >>> df_resultat = remplacer_na_par_valeur(df, nom_colonne, valeur_remplacement)
    >>> print(df_resultat)
       A    B
    0  1    'a'
    1  2    'b'
    2  0    'c'
    3  4  None
    """
    # Vérifie si la colonne spécifiée est présente dans le DataFrame
    if nom_colonne in df.columns:
        # Utilise la méthode 'fillna' pour remplacer les valeurs manquantes (NA) dans la colonne spécifiée
        df[nom_colonne] = df[nom_colonne].fillna(valeur_remplacement)
        return df
    else:
        print(f"La colonne '{nom_colonne}' n'est pas présente dans le DataFrame.")
        return df

def count_na_per_column(df):
    """
    Cette fonction prend en entrée un DataFrame et renvoie un nouveau DataFrame
    contenant deux colonnes : le nom de chaque colonne du DataFrame initial
    et le nombre de valeurs manquantes (NaN) pour chaque colonne.

    Paramètres :
    - df (pandas DataFrame) : Le DataFrame à traiter.

    Retour :
    - pandas DataFrame : Un DataFrame contenant deux colonnes : le nom de chaque colonne du DataFrame initial
                        et le nombre de valeurs manquantes (NaN) pour chaque colonne.

    Exemple :
    >>> df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': ['a', 'b', 'c', np.nan], 'C': [np.nan, np.nan, 3, 4]})
    >>> df_resultat = count_na_per_column(df)
    >>> print(df_resultat)
      Column  NA_Count
    0      A         1
    1      B         1
    2      C         2
    """
    # Utilise la méthode isna() pour obtenir un DataFrame booléen où True représente les valeurs manquantes.
    is_na_df = df.isna()
    
    # Utilise la méthode sum() sur le DataFrame booléen pour compter le nombre de valeurs manquantes par colonne.
    na_count_series = is_na_df.sum()
    
    # Crée un nouveau DataFrame à partir de la série de comptage des valeurs manquantes.
    result_df = pd.DataFrame({'Column': na_count_series.index, 'NA_Count': na_count_series.values})
    
    return result_df
