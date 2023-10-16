from sklearn.preprocessing import OrdinalEncoder    
import numpy as np
class CustomPreprocessor:
    def __init__(self,dataframe):
        self.encoder = OrdinalEncoder()
        self.dataframe = dataframe
        self.indices = [i for i, column in enumerate(dataframe.columns) if column in dataframe.select_dtypes(include=['object']).columns]
        self.object_columns = dataframe.select_dtypes(include=['object']).columns

    def fit_transform(self):
        self.unique_values = [sorted(list(set(self.dataframe[col])) ) for col in self.object_columns]
        self.encoder.fit(self.dataframe[self.object_columns])

    def transform(self,df_to_transform):
        df_to_transform[self.object_columns] = self.encoder.transform(df_to_transform[self.object_columns])
        return df_to_transform
    
    def inverse_transform(self,df_test):
        indices = [i for i, column in enumerate(self.dataframe.columns) if column in self.object_columns]
        {index: {j: v for j, v in enumerate(values)} for index, values in zip(indices, self.unique_values)}
        self.inverse_encoder = {index: {j: v for j, v in enumerate(values)} for (index, values) in zip(indices, self.unique_values)}
        if self.inverse_encoder is not None:
            for column_index in self.indices:
                df_test[column_index] = df_test[column_index].map(self.inverse_encoder[column_index])
        return df_test
                