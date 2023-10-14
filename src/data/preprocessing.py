from sklearn.preprocessing import OrdinalEncoder    
import numpy as np
class CustomPreprocessor:
    def __init__(self):
        self.encoder = OrdinalEncoder()

    def fit(self, dataframe):
        object_columns = dataframe.select_dtypes(include=['object']).columns
        self.encoder.fit(dataframe[object_columns])
        unique_values = [sorted(list(set(dataframe[col])) ) for col in object_columns]
        # à modifier pour que les clés du dictionnaires soit les valeurs des colonnes "objet"
        self.inverse_encoder = {i: {j: v for j, v in enumerate(values)} for i, (col, values) in enumerate(zip(dataframe.columns, unique_values))}
        print(self.inverse_encoder)

    def transform(self, dataframe):
        object_columns = dataframe.select_dtypes(include=['object']).columns
        dataframe[object_columns] = self.encoder.transform(dataframe[object_columns])
        return dataframe
    
    def inverse_transform(self, data):
        if self.inverse_encoder is not None:
            for col in self.inverse_encoder:
                data[:, col] = np.vectorize(lambda val: self.inverse_encoder[col][int(val)])
        return data