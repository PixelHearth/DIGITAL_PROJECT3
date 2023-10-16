from sklearn.preprocessing import OrdinalEncoder    
import numpy as np
class CustomPreprocessor:
    def __init__(self,dataframe):
        """initialisation des variables :
        self.encoder : c'est le programme qui transforme les valeurs string en valeur ordinale
        self.dataframe : dataframe utilisé pour l'entrainement de l'encoder
        self.indices : liste qui permet d'encapsuler les valeurs des colonnes qui se transforme en valeur ordinale
        self.object_columns : un index qui répertorie les colonnes considérées comme objet"""
        self.encoder = OrdinalEncoder()
        self.dataframe = dataframe
        self.indices = [i for i, column in enumerate(dataframe.columns) if column in dataframe.select_dtypes(include=['object']).columns]
        self.object_columns = dataframe.select_dtypes(include=['object']).columns

    def fit(self):
        """permet d'entrainer l'encodeur sur le dataframe de la classe"""
        self.unique_values = [sorted(list(set(self.dataframe[col])) ) for col in self.object_columns]
        self.encoder.fit(self.dataframe[self.object_columns])

    def transform(self,df_to_transform):
        """permet de transformer un dataframe avec l'entrainement de la base de données de la classe """
        df_to_transform[self.object_columns] = self.encoder.transform(df_to_transform[self.object_columns])
        return df_to_transform
    
    def inverse_transform(self,df_test):
        """permet de faire la transformation inverse à l'encodeur
        self.inverse_encoder : créer un dictionnaire qui permet de d'encapsuler la transformation faites au préalable
        """
        self.inverse_encoder = {index: {j: v for j, v in enumerate(values)} for (index, values) in zip(self.indices, self.unique_values)}
        if self.inverse_encoder is not None:
            for column_index in self.indices:
                df_test[column_index] = df_test[column_index].map(self.inverse_encoder[column_index])
        return df_test
                