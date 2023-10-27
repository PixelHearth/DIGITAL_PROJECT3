from sklearn.preprocessing import OrdinalEncoder   
class CustomPreprocessor:
    """ 
    fait un encodage des variables string en variables ordinales
    """
    def __init__(self,dataframe):
        """
        Initialise un objet CustomPreprocessor.

        Parameters:
        dataframe (pandas.DataFrame): Le DataFrame contenant les données à prétraiter.

        Attributes:
        encoder (OrdinalEncoder): L'encodeur qui transforme les valeurs de type chaîne en valeurs ordinales.
        dataframe (pandas.DataFrame): Le DataFrame utilisé pour entraîner l'encodeur.
        indices (list): Une liste des indices des colonnes qui seront transformées en valeurs ordinales.
        object_columns (Index): Un index répertoriant les noms des colonnes considérées comme des objets (chaînes).

        """
        self.encoder = OrdinalEncoder()
        self.dataframe = dataframe
        self.object_columns = dataframe.select_dtypes(include=['object']).columns
        self.indices = [column for column in (dataframe.columns) if column in self.object_columns]
        self.unique_values = [sorted(list(set(self.dataframe[col])) ) for col in self.object_columns]
        self.inverse_encoder = {index: {j: v for j, v in enumerate(values)}
                                 for (index, values) in zip(self.indices, self.unique_values)}


    def fit(self):
        """
        permet d'entrainer l'encodeur sur le dataframe de la classe
        """
                
        self.encoder.fit(self.dataframe[self.object_columns])

    def transform(self,df_to_transform):
        """
        Transforme un DataFrame en utilisant l'entraînement effectué sur la base de données de la classe.

        Parameters:
        df_to_transform (pandas.DataFrame): Le DataFrame à transformer.
        """

        df_to_transform[self.object_columns] = self.encoder.transform(df_to_transform[self.object_columns])
        return df_to_transform
    
    def inverse_transform(self,df_test):
        """
        Effectue la transformation inverse en utilisant l'encodeur.

        Parameters:
        df_test (pandas.DataFrame): Le DataFrame à transformer inversement.

        Returns:
        pandas.DataFrame: Le DataFrame avec la transformation inverse appliquée.

        # """
        # if self.inverse_encoder is not None:
        #     common_columns = set(df_test.columns).intersection(set(self.object_columns))

        #     for column_name in common_columns:
        #         column_index = self.dataframe.columns.get_loc(column_name)  # Obtenez l'index de la colonne par le nom
        #         df_test[column_name] = df_test[column_name].map(self.inverse_encoder[column_index])

        # return df_test
        if self.inverse_encoder is not None:
            for index, col_name in enumerate(self.indices):
                for index in self.inverse_encoder:
                    print(index)
                    encoded_column_name = self.inverse_encoder[index]
                    print(encoded_column_name)
                    df_test[encoded_column_name] = df_test[col_name].map(self.inverse_encoder[index])

        return df_test
    