import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pandas.api.types as ptypes

def select_variables(dataframe, nb_feature):
    """
    Sélectionne les variables les plus explicatives du modèle à l'aide d'un modèle RandomForest.

    Parameters:
    - dataframe (DataFrame): Le DataFrame contenant les données.
    - nb_feature (int): Le nombre de caractéristiques à sélectionner.

    Returns:
    - selected_dataframe (DataFrame): Le DataFrame contenant les caractéristiques sélectionnées.
    - importances_df (DataFrame): Le DataFrame des importances des caractéristiques.

    Raises:
    - AssertionError: Si les conditions préalables ne sont pas satisfaites.

    Example:
    >>> df = pd.DataFrame({'Target': [0, 1, 0], 'Feature1': [1, 2, 3], 'Feature2': [4, 5, 6]})
    >>> selected, importances = select_variables(df, 2)

    Le modèle RandomForest est entraîné sur les caractéristiques indépendantes du DataFrame,
    et les caractéristiques les plus importantes sont sélectionnées en fonction du paramètre nb_feature.
    Le DataFrame résultant contient la variable dépendante et les caractéristiques sélectionnées.

    Note:
    - Le modèle RandomForestClassifier est utilisé avec 100 arbres et une graine aléatoire fixe (random_state=42).
    """
    # création d'assert préalable 
    assert isinstance(dataframe, pd.DataFrame), "Le paramètre 'dataframe' doit être un objet DataFrame."
    assert isinstance(nb_feature, int), "Le paramètre 'nb_feature' doit être un entier."
    assert nb_feature > 0, "Le paramètre 'nb_feature' doit être supérieur à zéro."
    assert nb_feature <= len(dataframe.columns) - 1, "Le paramètre 'nb_feature' ne doit pas dépasser le nombre de colonnes dans le dataframe - 1."
    assert len(dataframe.columns) > 0, "Le DataFrame ne peut pas être vide."

    assert all(ptypes.is_numeric_dtype(dataframe[col])for col in dataframe.columns), "Les types de données des colonnes du dataframe d'entrainement doivent être int ou float.\n, utiliser la fonction custompreprocessing"

    # Extraction des variables dépendantes et indépendantes
    dependent_variable = dataframe.iloc[:, 0]
    independent_variable = dataframe.iloc[:, 1:]

    # Entraînement d'un modèle Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(independent_variable.values, dependent_variable.values)

    # Calcul des importances des caractéristiques
    feature_importances = rf_model.feature_importances_
    importances_df = pd.DataFrame({'Feature': dataframe.iloc[:, 1:].columns, 'Importance': feature_importances})
    importances_df = importances_df.sort_values(by='Importance', ascending=False)

    # Sélection des caractéristiques en fonction de nb_feature
    assert nb_feature <= len(importances_df), "Le paramètre 'nb_feature' doit être inférieur ou égal au nombre de caractéristiques disponibles."
    selection_dataframe = importances_df[:nb_feature]

    # Récupération des noms des caractéristiques sélectionnées
    selected_features = selection_dataframe['Feature'].tolist()

    # Création du DataFrame résultant avec les caractéristiques sélectionnées
    selected_dataframe = pd.concat([dependent_variable, independent_variable[selected_features]], axis=1)
    assert isinstance(selected_dataframe,pd.DataFrame), "le résultat doit être un dataframe"
    return selected_dataframe, importances_df
