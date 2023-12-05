import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from pandas.api.types import is_numeric_dtype

def select_features(dataframe, num_features):
    """
    Selects the most explanatory variables of the model using a RandomForest model.

    Parameters:
    - dataframe (DataFrame): The DataFrame containing the data.
    - num_features (int): The number of features to select.

    Returns:
    - selected_dataframe (DataFrame): The DataFrame containing the selected features.
    - importances_df (DataFrame): The DataFrame of feature importances.

    Raises:
    - AssertionError: If the preconditions are not satisfied.

    Example:
    >>> df = pd.DataFrame({'Target': [0, 1, 0], 'Feature1': [1, 2, 3], 'Feature2': [4, 5, 6]})
    >>> selected, importances = select_features(df, 2)

    The RandomForest model is trained on the independent features of the DataFrame,
    and the most important features are selected based on the nb_feature parameter.
    The resulting DataFrame contains the dependent variable and the selected features.

    Note:
    - The RandomForestClassifier model is used with 50 trees and a fixed random seed (random_state=42).
    """
    
    # Preconditions
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("The 'dataframe' parameter must be a DataFrame.")

    if not isinstance(num_features, int):
        raise TypeError("The 'num_features' parameter must be an integer.")

    if num_features <= 0:
        raise ValueError("The 'num_features' parameter must be greater than zero.")

    if num_features > len(dataframe.columns) - 1:
        raise ValueError("The 'num_features' parameter must not exceed the number of columns in the dataframe minus 1.")

    if len(dataframe.columns) == 0:
        raise ValueError("The DataFrame cannot be empty.")

    if not all(is_numeric_dtype(dataframe[col]) for col in dataframe.columns):
        raise TypeError("Data types of columns in the training dataframe must be int or float.\nUse the custom preprocessing function.")

    # Extracting dependent and independent variables
    dependent_variable = dataframe.iloc[:, 0]
    independent_variables = dataframe.iloc[:, 1:]

    # Training a Random Forest model
    rf_model = RandomForestClassifier(n_estimators=200, random_state=42)
    rf_model.fit(independent_variables.values, dependent_variable.values)

    # Calculating feature importances
    feature_importances = rf_model.feature_importances_
    importances_df = pd.DataFrame({'Feature': dataframe.iloc[:, 1:].columns, 'Importance': feature_importances})
    importances_df = importances_df.sort_values(by='Importance', ascending=False)

    # Selecting features based on num_features
    if num_features == len(importances_df):
        raise ValueError("The 'num_features' parameter must be less than or equal to the number of available features.")
        
    selected_dataframe = importances_df[:num_features]

    # Retrieving the names of the selected features
    selected_features = selected_dataframe['Feature'].tolist()

    # Creating the resulting DataFrame with the selected features
    selected_dataframe = pd.concat([dependent_variable, independent_variables[selected_features]], axis=1)

    if not isinstance(selected_dataframe, pd.DataFrame):
        raise TypeError("The result must be a DataFrame.")
    
    return selected_dataframe.columns, importances_df
