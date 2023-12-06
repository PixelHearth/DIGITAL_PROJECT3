from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np

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
    def __init__(self, df):
        # asserts
        if not isinstance(df,pd.DataFrame):
            raise TypeError("input must be a dataframe")

        # Loading the encoding model
        self.encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
        
        # get columns to train
        self.df = df.iloc[:,1:]
        
        # Keep distinct object and numerous columns
        self.object_columns = self.df.select_dtypes(include=['object']).columns
        self.numeric_columns = self.df.select_dtypes(include=['number']).columns
        

    def label_encoder(self,df):
        """Transform the first column, must be categorical values, in a value

        Args:
            dataframe (pd.DataFrame): Dataframe to encode in ordinal

        Returns:
            dataframe (pd.DataFrame): Dataframe with first column encoded
            
        Exemple:
        >>> df = pd.DataFrame({'Category': ['A', 'B', 'C', 'A', 'B'],'color': ['blue','red','red','blue','grey']})
        >>> encoded_df = label_encoder(df)
        >>> print(encoded_df)
           Category Color
        0         0 blue    
        1         1 red
        2         2 red
        3         0 blue
        4         1 grey
        
        """
        # Return error type if not a dataframe
        if not isinstance(df,pd.DataFrame):
            raise TypeError("input must be a dataframe")
        
        # Instance LabelEncoder to transform label in number
        label_encoder = LabelEncoder()
        
        # Fit and transform the first column
        df.iloc[:, 0 ] = label_encoder.fit_transform(df.iloc[:, 0 ])
        print(label_encoder.classes_)
        # Get Int type for first columns
        df = pd.concat([df.iloc[:, 0].astype(int),df.iloc[:,1:]],axis= 1)

        return df
    
    def fit(self):
        """DataFrame to fit the OneHotEncoder instanced in the class"""
        
        # Fit the encoder on the object dataset
        self.encoder.fit(self.df[self.object_columns])
        
    def fit_transform(self,df):
        """Fit and transform with the OneHotEncoder object columns in the dataframe 

        Args:
            dataframe (pd.DataFrame): dataframe to encode

        Returns:
            dataframe (pd.DataFrame): dataframe encoded
        """
        if not isinstance(df,pd.DataFrame):
            raise TypeError("input must be a dataframe")
        
        #fit and transform object columns
        encoded_data = self.encoder.fit_transform(df[self.object_columns])
        
        # Create a DataFrame with the encoded data
        encoded_df = pd.DataFrame(encoded_data, columns=self.encoder.get_feature_names_out(self.object_columns)).reset_index(drop=True)
        
        df = df.drop(self.object_columns,axis=1).reset_index(drop=True)

        # Concatenate the encoded DataFrame with the original DataFrame
        result_df = pd.concat([self.label_encoder(df), encoded_df], axis=1)

        return result_df

    def transform(self, df):
        """Function to transform a dataframe with the fit made previously with the dataframe instancied in the class

        Args:
            dataframe (pd.DataFrame): DataFrame to encode

        Returns:
            dataframe (pd.DataFrame): DataFrame encoded
        """
        if not isinstance(df,pd.DataFrame):
            raise TypeError("input must be a dataframe")

        # Create a DataFrame with the transformed data
        encoded_data = self.encoder.transform(df[self.object_columns])
        
        # Create a DataFrame with the encoded data
        encoded_df = pd.DataFrame(encoded_data, columns=self.encoder.get_feature_names_out(self.object_columns))
        
        #drop columns transformed
        df = df.drop(self.object_columns,axis=1).reset_index(drop=True)

        # Concatenate the encoded DataFrame with the original DataFrame
        result_df = pd.concat([df, encoded_df], axis=1)
        
        return result_df

    def inverse_transform(self, df):
        """
        Performs the inverse transformation using the encoder.

        Parameters:
            df_test (pandas.DataFrame): The DataFrame to inverse transform.

        Returns:
            pandas.DataFrame: The DataFrame with the inverse transformation applied.
        """

        # Check that our inverse_encoder dictionary is not empty
        
        if not isinstance(df,pd.DataFrame):
            raise TypeError("input must be a dataframe")

        # Get origin name of columns
        cols_transformed = self.encoder.get_feature_names_out(self.object_columns)

        # Inverse the transformation with their original name
        if len(cols_transformed) == 0 : 
            raise ValueError("no object columns in dataframe")
        inverse_encoded = self.encoder.inverse_transform(df[cols_transformed])

        # Replace columns transformed by the inverse_encoded
        df[self.object_columns] = inverse_encoded
        
        # Drop binarized columns
        df.drop(cols_transformed,axis = 1,inplace= True)

        return df
    
    def column_selection(self,cols):
        """Get cols transformed by the transformer, split columns modified then drop duplicate, useful after a selection of variables

        Args:
            cols (list): list of selected variable by the RandomForest

        Returns:
            cols (list): list of columns selected to reduce dimension
        """
        #transform cols
        cols_transformed = self.encoder.get_feature_names_out(self.object_columns).tolist() 

        #variable selected
        col_selected = cols 
        
        #loop to get columns 
        list_cols = []
        for cols in col_selected:
            if cols in cols_transformed:
                list_cols.append(cols.rsplit('_', 1)[0])
            else:
                list_cols.append(cols)
                
        # frop duplicate
        list_cols = list(set(list_cols))
        return list_cols

