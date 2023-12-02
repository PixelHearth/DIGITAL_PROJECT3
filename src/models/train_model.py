
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from pandas.api.types import is_numeric_dtype
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,roc_auc_score,log_loss
from sklearn.model_selection import train_test_split
import shap
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
        self.dataframe = self.dataframe.sample(frac=1, random_state=42) 

        # Test DataFrame
        self.individual_features = individual_features
        

    def standardize_training_data(self):
        """Standardize the train dataframe
        """
        # Select Number type
        numeric_columns = self.dataframe.select_dtypes(include=['number']).columns

        # Initialize scaler
        scaler = StandardScaler()

        # apply scaler to num col
        self.dataframe[numeric_columns] = scaler.fit_transform(self.dataframe[numeric_columns])

        # return df
        self.dependent_variable = self.dataframe.iloc[:, 0].values

        # return df
        self.independent_variable = self.dataframe.iloc[:, 1:].values

    def standardize_test_data(self):
        """Standardize the test dataframe
        """
        # Select number col
        numeric_columns_test = self.individual_features.select_dtypes(include=['number']).columns

        # Initialize scaler
        scaler = StandardScaler()

        # Apply to num col
        self.individual_features[numeric_columns_test] = scaler.fit_transform(self.individual_features[numeric_columns_test])
        
        # Independent variables of the test individual
        self.np_individual_features = self.individual_features.iloc[:, 1:].values

    def metric_knn(self):
        """Function to get the k optimal for the KNN"""
        # Split dataframe into train and test frame
        X_train, X_test, y_train, y_test = train_test_split(self.independent_variable,self.dependent_variable, test_size=0.3, random_state=42)
        roc_auc_scores = []
        # Test between 50 value for k 
        for k in range(1, 50):  # Vous pouvez ajuster la plage selon vos besoins
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(X_train, y_train)
            y_prob = knn.predict(X_test)  # Probabilité de la classe positive
            roc_auc = accuracy_score(y_test, y_prob)
            # store accuracy_score
            roc_auc_scores.append(round(roc_auc, 2))
        print(roc_auc_scores)
        
        # get k optimal
        best_k_index = roc_auc_scores.index(max(roc_auc_scores))
        best_k = range(1, 50)[best_k_index]
        
        return best_k
    
    def k_neighbors(self, best_k):
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
        neigh = KNeighborsClassifier(n_neighbors=best_k)
        
        # Training data on the training database
        neigh.fit(self.independent_variable, self.dependent_variable)

        # Prediction on the test individual data
        prediction = neigh.predict(self.np_individual_features)
        proba = neigh.predict_proba(self.np_individual_features)
        

        # make a function to get prediction for 1 class and a function to predict for 2 class
        sorted_class_indices = np.argsort(proba[0])[::-1]

        # Select 3 representatives classes
        top_classes = sorted_class_indices[:3]
        
        # Make a list
        proba = [{"classe": class_index, "probabilite": proba[0][class_index]} for class_index in top_classes]

        # Returning a DataFrame with the prediction and independent variables of the test individual
        self.independant_variable_test = self.np_individual_features.flatten()
        result = np.concatenate([prediction, self.independant_variable_test])
        
        dataframe_decoded = pd.DataFrame(result).transpose()

        dataframe_decoded.columns = self.dataframe.columns
        
        # # Créer un explainer SHAP
        # explainer = shap.KernelExplainer(neigh.predict_proba, self.independent_variable)
        # # Choisissez un échantillon (par exemple, le premier échantillon dans l'ensemble de test)
        # sample = self.np_individual_features

        # # Calculer les valeurs SHAP pour l'échantillon choisi
        # shap_values = explainer.shap_values(sample)
        #         # Résumé des valeurs SHAP
        # shap.summary_plot(shap_values, features=dataframe_decoded.iloc[:,1:])
        
        if not isinstance(dataframe_decoded, pd.DataFrame):
            raise TypeError("Must be DataFrame")
        
        return dataframe_decoded,proba
