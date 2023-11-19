from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
import pandas.api.types as ptypes
class Models:
    """
    Classe représentant un ensemble de modèles pour l'analyse de données.

    :param dataframe: Le dataframe d'entraînement contenant les données à expliquer et explicatives.
    :type dataframe: pandas.DataFrame

    :param individual_features: Le dataframe des caractéristiques de l'individu test.
    :type individual_features: pandas.DataFrame

    :raises AssertionError: Si les données d'entraînement et de test ne sont pas des dataframes pandas.

    :Example:

    >>> data = pd.DataFrame({'Target': [1, 0, 1], 'Feature1': [0.2, 0.4, 0.6], 'Feature2': [0.1, 0.3, 0.5]})
    >>> individual_data = pd.DataFrame({'Feature1': [0.7], 'Feature2': [0.4]})
    >>> models_instance = Models(data, individual_data)
    >>> models_instance.k_neighbors()
    Précision du modèle : 0.85
    # Output: Un DataFrame contenant les prédictions et les variables indépendantes.

    """

    def __init__(self, dataframe, individual_features):
        assert isinstance(dataframe, pd.DataFrame), "Les données d'entraînement doivent être sous forme de dataframe"
        assert isinstance(individual_features, pd.DataFrame), "Les données de test doivent être sous forme de dataframe"
        assert (len(dataframe.columns) or len(individual_features.columns)) >0, "votre dataframe est vide"
        assert len(dataframe.columns) == (len(individual_features.columns)), "les bases de données n'ont pas le même nombre de variables,  utiliser l'algorithme de selection des variables"

        assert all(ptypes.is_numeric_dtype(dataframe[col])for col in dataframe.columns), "Les types de données des colonnes du dataframe d'entrainement doivent être int ou float. utiliser l'algorithme de preprocessing"
        assert all(ptypes.is_numeric_dtype(individual_features[col])for col in individual_features.columns), " Les types de données des colonnes du dataframe de test doivent être int ou float. utiliser l'algorithme de preprocessing"

        # Dataframe d'entraînement
        self.dataframe = dataframe

        # Variable à expliquer
        self.dependent_variable = self.dataframe.iloc[:, 0].values

        # Variables explicatives
        self.independent_variable = self.dataframe.iloc[:, 1:].values

        # Dataframe de test
        self.individual_features = individual_features

        # Variables explicatives de l'individu test
        self.np_individual_features = individual_features.iloc[:, 1:].values

    def k_neighbors(self):
        """
        Crée un algorithme de k_neighbors basé sur les données de propriétés.

        Cette fonction utilise l'algorithme KNeighborsClassifier pour entraîner un modèle
        et effectuer des prédictions sur les données fournies.

        :return: Un DataFrame contenant les prédictions du modèle et les variables indépendantes.
        :rtype: pandas.DataFrame

        :raises ValueError: Si les données indépendantes et dépendantes ne sont pas correctement définies.

        :Example:

        >>> model = Models(data, individual_data)
        >>> model.k_neighbors()
        Précision du modèle : 0.85
        # Output: Un DataFrame contenant les prédictions et les variables indépendantes de l'individu test.

        """
        # Instance du k-neighbors avec 5 individus proches
        neigh = KNeighborsClassifier(n_neighbors=3)

        # Entraînement des données sur la base de donnée d'entrainement
        neigh.fit(self.independent_variable, self.dependent_variable)

        # Prédiction sur les données de l'individu test
        prediction = neigh.predict(self.np_individual_features)

        proba_predict = neigh.predict_proba(self.np_individual_features)
        # Création et affichage du score de fiabilité de la prédiction
        score = neigh.score(self.independent_variable, self.dependent_variable)
        print(f"Précision du modèle : {score}")
        print(proba_predict)

        # Restitution d'un DataFrame avec la prédiction et les variables indépendantes de l'individu test
        self.independant_variable_test = self.np_individual_features.flatten()
        result = np.concatenate([prediction, self.independant_variable_test])
        dataframe_decoded = pd.DataFrame(result).transpose()
        assert isinstance(dataframe_decoded, pd.DataFrame)
        return dataframe_decoded
