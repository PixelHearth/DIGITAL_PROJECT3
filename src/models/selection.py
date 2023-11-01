import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def select_variables(dataframe, individual_features, nb_feature):
    """
    Sélectionne les variables les plus explicatives du modèle à l'aide d'un modèle RandomForest.

    Parameters:
    dataframe (DataFrame): Le DataFrame contenant les données.
    individual_features (DataFrame): Le DataFrame des caractéristiques individuelles.
    nb_feature (int): Le nombre de caractéristiques à sélectionner.

    Returns:
    selected_dataframe (DataFrame): Le DataFrame contenant les caractéristiques sélectionnées.
    selected_new_variable (DataFrame): Le DataFrame des caractéristiques individuelles correspondantes.
    selected_new_variable_col (Index): L'Index des colonnes de selected_new_variable.
    importances_df (DataFrame): Le DataFrame des importances des caractéristiques.
    """
    # Extraction des variables dépendantes et indépendantes
    dependent_variable = dataframe.iloc[:, 0]
    independent_variable = dataframe.iloc[:, 1:]
    individual_independante_features = individual_features.iloc[:, 1:]

    # Entraînement d'un modèle Random Forest
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(independent_variable.values, dependent_variable.values)

    # Calcul des importances des caractéristiques
    feature_importances = rf_model.feature_importances_
    importances_df = pd.DataFrame({'Feature': dataframe.iloc[:, 1:].columns, 'Importance': feature_importances})
    importances_df = importances_df.sort_values(by='Importance', ascending=False)

    # Sélection des caractéristiques en fonction de nb_feature
    selection_dataframe = importances_df[:nb_feature]

    # Récupération des noms des caractéristiques sélectionnées
    selected_features = selection_dataframe['Feature'].tolist()

    # Création du DataFrame résultant avec les caractéristiques sélectionnées
    selected_dataframe = pd.concat([dependent_variable, independent_variable[selected_features]], axis=1)
    selected_new_variable = pd.concat([individual_features.iloc[:, 0], individual_independante_features[selected_features]], axis=1)
    selected_new_variable_col = selected_new_variable.columns

    return selected_dataframe, selected_new_variable, selected_new_variable_col, importances_df