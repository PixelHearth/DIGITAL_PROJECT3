import pandas as pd
from pandas.api.types import is_numeric_dtype
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import shap
class Models:

    """
    Class representing a model for KNN.
    
    Parameters:
    -df (pd.df): The training df containing the data to be explained and explanatory.

    -individual_features (pd.df): The df of test individual features.

    Raises AssertionError: 
        If the training and test data are not pandas dfs.

    :Example:

    >>> data = pd.df({'Target': [1, 0, 1], 'Feature1': [0.2, 0.4, 0.6], 'Feature2': [0.1, 0.3, 0.5]})
    >>> individual_data = pd.df({'Feature1': [0.7], 'Feature2': [0.4]})
    >>> models_instance = Models(data, individual_data)
    >>> models_instance.k_neighbors()
    Model Accuracy: 0.85
    # Output: A df containing predictions and independent variables.

    """

    def __init__(self, df, df_customer):
        
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Training data must be in the form of a df.")

        if not isinstance(df_customer, pd.DataFrame):
            raise TypeError("Test data must be in the form of a df.")

        if len(df.columns) == 0 or len(df_customer.columns) == 0:
            raise ValueError("Your df is empty.")

        if len(df.columns) != (len(df_customer.columns) + 1):
            raise ValueError("Databases do not have the same number of variables, use the variable selection algorithm.")

        if not all(is_numeric_dtype(df[col]) for col in df.columns):
            raise TypeError("Data types of columns in the training df must be int or float. Use the preprocessing algorithm.")

        if not all(is_numeric_dtype(df_customer[col]) for col in df_customer.columns):
            raise TypeError("Data types of columns in the test df must be int or float. Use the preprocessing algorithm.")

        # Training df
        self.df = df

        # Test df
        self.df_customer = df_customer
        self.customer_features = self.df_customer.values

        # Train df
        self.dependent_variable = self.df.iloc[:, 0].values
        self.independent_variable = self.df.iloc[:, 1:].values

    def metric_knn(self):
        """
        Function to determine the optimal value of k for KNN.

        Description:
        This function performs a k-fold cross-validation to find the optimal number of neighbors (k) for a KNN (K-Nearest Neighbors) classifier. It evaluates the performance using the accuracy score on a test set.

        Inputs:
        - self.independent_variable: Pandas df, features or independent variables.
        - self.dependent_variable: Pandas Series, target or dependent variable.
        
        Outputs:
        - best_k: Integer, optimal number of neighbors (k) that maximizes the accuracy score.

        Example:
        
        # Instantiate the class with data
        >>> my_classifier = YourClassName(independent_variable, dependent_variable)
        
        # Call the metric_knn function to get the optimal k
        >>> optimal_k = my_classifier.metric_knn()
    
        ```
        """
        # Split df into train and test frame
        x_train, x_test, y_train, y_test = train_test_split(self.independent_variable, self.dependent_variable, test_size=0.2)
        accuracy_scores = []

        # Test between 50 value for k
        for k in range(5, 55):  
            knn = KNeighborsClassifier(n_neighbors=k)
            knn.fit(x_train, y_train)
            y_pred = knn.predict(x_test)
            # Compute accuracy_score
            cm = accuracy_score(y_test, y_pred)
            # Stock score in a list
            accuracy_scores.append(cm)
            
        # Get the max value
        best_k_index = np.argmax(accuracy_scores)

        # Get the k optimal
        best_k = range(5, 55)[best_k_index]

        return best_k

    
    def k_neighbors(self):
        """
        Creates a k_neighbors algorithm based on property data.

        This function uses the KNeighborsClassifier algorithm to train a model
        and make predictions on the provided data.

        Return: A df containing model predictions and independent variables.
        Rtype: pandas.df

        raises ValueError: If independent and dependent data are not properly defined.

        Example:

        >>> model = Models(data, individual_data)
        >>> model.k_neighbors()
        Model Accuracy: 0.85
        # Output: A df containing predictions and independent variables of the test individual.

        """
        # Instance of k-neighbors with 3 close individuals
        best_k = self.metric_knn()
        neigh = KNeighborsClassifier(n_neighbors=best_k)
        
        # Training data on the training database
        neigh.fit(self.independent_variable, self.dependent_variable)

        # Prediction on the test individual data
        prediction = neigh.predict(self.customer_features)
        # score = neigh.score()
        proba = neigh.predict_proba(self.customer_features)
        
        # make a function to get prediction for 1 class and a function to predict for 2 class
        sorted_class_indices = np.argsort(proba[0])[::-1]

        # Select 3 representatives classes
        top_classes = sorted_class_indices[:3]
        score = np.sum(proba[:, top_classes], axis=1)
        
        proba_values = proba[0][top_classes].tolist()

        # Créer une liste de dictionnaires pour chaque classe et sa probabilité
        result_list = [{'classe': int(class_index), 'probabilite': float(prob)} for class_index, prob in zip(top_classes, proba_values)]

        # Create shap explainer
        explainer = shap.KernelExplainer(neigh.predict_proba, self.independent_variable)

        # Learning on customer's data
        sample = self.customer_features

        # Compute shap values
        shap_values = explainer.shap_values(sample)
        # Chart
        sns.set(style="white")

        # Create a summary plot with enhanced settings
        shap.summary_plot(
            shap_values,
            features=self.df.iloc[:, 1:],
            plot_type="bar",  # Use violin plot for better visualization
            show=False,  # Avoid automatic plt.show() to customize the plot further
            plot_size=(16, 6)
        )

        # Customize the plot
        plt.title('Part de la contribution des variables dans la prédiction de la classe', fontsize=16)
        plt.xlabel('Part de la contribution ', fontsize=14)
        plt.ylabel('Variables', fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()

        plt.savefig("C:/Users/Guillaume Baroin/Documents/M2_sep/DIGITAL_PROJECT3/docs/shape_value.png")
        return result_list,score
