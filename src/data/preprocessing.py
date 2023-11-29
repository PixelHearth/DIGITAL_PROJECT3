from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import pandas as pd

class CustomProcessing:
    """ 
    Performs one-hot encoding of string variables.
    
    Initializes a CustomPreprocessor object.

    Parameters:
        dataframe (pandas.DataFrame): The DataFrame containing the data to preprocess.

    Attributes:
        encoder (OneHotEncoder): The encoder that transforms string values into one-hot encoded vectors.
        dataframe (pandas.DataFrame): The DataFrame used to train the encoder.
        object_columns (Index): An index listing the names of columns considered as objects (strings).
    """
    def __init__(self, dataframe):
        # asserts
        assert isinstance(dataframe, pd.DataFrame)

        # Loading the encoding model
        self.encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)

        # DataFrame to convert, train, or transform
        self.dataframe = dataframe.iloc[:,1:]
        self.dataframe_var = dataframe.iloc[:, 0]
        # Keep columns that are object types
        self.object_columns = self.dataframe.select_dtypes(include=['object']).columns
    
    def ordinal_var(self,dataframe):
        self.dataframe_var = dataframe.iloc[:, 0]
        label_encoder = LabelEncoder()
        self.dataframe_var = label_encoder.fit_transform(self.dataframe_var)
        dataframe.iloc[:, 0] = self.dataframe_var
        dataframe = pd.concat([dataframe.iloc[:, 0],dataframe.iloc[:,1:]],axis= 1).astype(int)
        return dataframe
    
    def fit(self):
        # Fit the encoder on the entire dataset
        self.encoder.fit(self.dataframe[self.object_columns])
        
    def fit_transform(self,dataframe):
        # Transform the object columns and create new one-hot encoded columns
        self.encoder.fit(self.dataframe[self.object_columns])
        encoded_data = self.encoder.transform(dataframe[self.object_columns])
        # Create a DataFrame with the encoded data
        encoded_df = pd.DataFrame(encoded_data, columns=self.encoder.get_feature_names_out(self.object_columns)).reset_index(drop=True)
        
        df = dataframe.drop(self.object_columns,axis=1)
        df = df.reset_index(drop=True)
        # Concatenate the encoded DataFrame with the original DataFrame
        result_df = pd.concat([self.ordinal_var(df), encoded_df], axis=1)
        return result_df

    def transform(self, dataframe):
        """
        Transforms the specified DataFrame using the trained OneHotEncoder.
        """
        assert isinstance(dataframe, pd.DataFrame)

        # Create a DataFrame with the transformed data
        encoded_data = self.encoder.transform(dataframe[self.object_columns]).toarray()
        # Create a DataFrame with the encoded data
        encoded_df = pd.DataFrame(encoded_data, columns=self.encoder.get_feature_names_out(self.object_columns)).reset_index(drop=True)
        
        df = dataframe.drop(self.object_columns,axis=1)
        df = df.reset_index(drop=True)
        # Concatenate the encoded DataFrame with the original DataFrame
        result_df = pd.concat([self.ordinal_var(df), encoded_df], axis=1)
        
        return result_df

    def inverse_transform(self, encoded_dataframe):
        """
        Performs the inverse transformation using the encoder.

        Parameters:
            df_test (pandas.DataFrame): The DataFrame to inverse transform.

        Returns:
            pandas.DataFrame: The DataFrame with the inverse transformation applied.
        """

        # Check that our inverse_encoder dictionary is not empty
        
        assert isinstance(encoded_dataframe, pd.DataFrame)

        # Extract the relevant object columns used during training
        col = self.encoder.get_feature_names_out(self.object_columns)
        print(col)
        # Inverse transform the encoded data
        for col in col:
            if col in encoded_dataframe.columns:
                encoded_dataframe[col] = self.encoder.inverse_transform(encoded_dataframe)
        
        return encoded_dataframe
