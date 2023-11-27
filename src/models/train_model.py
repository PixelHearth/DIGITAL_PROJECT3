
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from pandas.api.types import is_numeric_dtype
from sklearn.preprocessing import MinMaxScaler
class Models:

    """
    Class representing a model for KNN.
    
    Parameters:
    -dataframe (pd.DataFrame): The training DataFrame containing the data to be explained and explanatory.

    -individual_features (pd.DataFrame): The DataFrame of test individual features.

    Raises AssertionError: 
        If the training and test data are not pandas DataFrames.

    :Example:

    >>> data = pd.DataFrame({'Target': [1, 0, 1], 'Feature1': [0.2, 0.4, 0.6], 'Feature2': [0.1, 0.3, 0.5]})
    >>> individual_data = pd.DataFrame({'Feature1': [0.7], 'Feature2': [0.4]})
    >>> models_instance = Models(data, individual_data)
    >>> models_instance.k_neighbors()
    Model Accuracy: 0.85
    # Output: A DataFrame containing predictions and independent variables.

    """

    def __init__(self, dataframe, individual_features):
        
        assert isinstance(dataframe, pd.DataFrame), "Training data must be in the form of a DataFrame."
        assert isinstance(individual_features, pd.DataFrame), "Test data must be in the form of a DataFrame."
        assert (len(dataframe.columns) or len(individual_features.columns)) > 0, "Your DataFrame is empty."
        assert len(dataframe.columns) == len(individual_features.columns), "Databases do not have the same number of variables, use the variable selection algorithm."

        assert all(is_numeric_dtype(dataframe[col]) for col in dataframe.columns), "Data types of columns in the training dataframe must be int or float. Use the preprocessing algorithm."
        assert all(is_numeric_dtype(individual_features[col]) for col in individual_features.columns), "Data types of columns in the test dataframe must be int or float. Use the preprocessing algorithm."

        # Training DataFrame
        self.dataframe = dataframe

        # Dependent variable
        self.dependent_variable = self.dataframe.iloc[:, 0].values

        # Independent variables
        self.independent_variable = self.dataframe.iloc[:, 1:].values

        # Test DataFrame
        self.individual_features = individual_features

        # Independent variables of the test individual
        self.np_individual_features = individual_features.iloc[:, 1:].values
        
        

    def k_neighbors(self):
        """
        Creates a k_neighbors algorithm based on property data.

        This function uses the KNeighborsClassifier algorithm to train a model
        and make predictions on the provided data.

        Return: A DataFrame containing model predictions and independent variables.
        Rtype: pandas.DataFrame

        raises ValueError: If independent and dependent data are not properly defined.

        Example:

        >>> model = Models(data, individual_data)
        >>> model.k_neighbors()
        Model Accuracy: 0.85
        # Output: A DataFrame containing predictions and independent variables of the test individual.

        """
        # Instance of k-neighbors with 3 close individuals
        neigh = KNeighborsClassifier(n_neighbors=3)
        
        
        #! make a function then implement
        scaler = MinMaxScaler()

        # Normalization of data on properties dataset
        self.independent_variable = scaler.fit_transform(self.independent_variable)

        # Transform customer dataset
        self.np_individual_features = scaler.transform(self.np_individual_features)
        
        # Training data on the training database
        neigh.fit(self.independent_variable, self.dependent_variable)

        # Prediction on the test individual data
        prediction = neigh.predict(self.np_individual_features)
        proba = neigh.predict_proba(self.np_individual_features)

        # make a function to get prediction for 1 class and a function to predict for 2 class
        # Obtenir les indices triés des classes par probabilité décroissante
        sorted_class_indices = np.argsort(proba[0])[::-1]

        # Sélectionner les deux classes les mieux représentées
        top_classes = sorted_class_indices[:2]

        # Afficher les résultats
        for i,e in zip(top_classes,self.dataframe.iloc[:, 0]):
            print(f"{e}: {proba[0][i] * 100:.2f}%")

        # Output exemple :
        # Classe 1: 66.67%
        # Classe 0: 33.33%

            
        # Creation and display of the prediction reliability score
        score = neigh.score(self.independent_variable, self.dependent_variable)
        print(f"Model Accuracy: {score}")

        # Returning a DataFrame with the prediction and independent variables of the test individual
        self.independant_variable_test = self.np_individual_features.flatten()
        result = np.concatenate([prediction, self.independant_variable_test])
        dataframe_decoded = pd.DataFrame(result).transpose()
        dataframe_decoded.columns = self.dataframe.columns
        assert isinstance(dataframe_decoded, pd.DataFrame)
        return dataframe_decoded,proba
