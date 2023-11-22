from sklearn.preprocessing import OrdinalEncoder   
import pandas as pd
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

class CustomPreprocessor:
    """ 
    Performs ordinal encoding of string variables.
    
    Initializes a CustomPreprocessor object.

    Parameters:
        dataframe (pandas.DataFrame): The DataFrame containing the data to preprocess.

    Attributes:
        encoder (OrdinalEncoder): The encoder that transforms string values into ordinal values.
        dataframe (pandas.DataFrame): The DataFrame used to train the encoder.
        indices (list): A list of column indices that will be transformed into ordinal values.
        object_columns (Index): An index listing the names of columns considered as objects (strings).
    """
    def __init__(self, dataframe):
        #asserts
        assert isinstance(dataframe, pd.DataFrame)
        # Loading the encoding model
        self.encoder = OrdinalEncoder()

        # DataFrame to convert, train, or transform
        self.dataframe = dataframe

        # Keep columns that are object types
        self.object_columns = dataframe.select_dtypes(include=['object']).columns

        # List of names of object columns
        self.indices = [column for column in dataframe.columns if column in self.object_columns]
        if len(self.indices) == 0:
            raise ValueError("There are no string-type columns; applying the function is unnecessary")

        # Ordered list of values within the columns
        self.unique_values = [sorted(list(set(self.dataframe[col]))) for col in self.object_columns]

        # Dictionaries with column title, unique values within the column ordered with their corresponding indices
        self.inverse_encoder = {index: {j: v for j, v in enumerate(values)}
                                for (index, values) in zip(self.indices, self.unique_values)}
        assert self.inverse_encoder is not None, 'The transformation dictionary is empty'

    def fit(self):
        """
        Trains the encoder on the class's DataFrame.
        """
        self.encoder.fit(self.dataframe[self.object_columns])

    def transform(self, df_to_transform):
        """
        Transforms the specified DataFrame using the encoder.

        Parameters:
            df_to_transform (pandas.DataFrame): The DataFrame to transform.

        Returns:
            pandas.DataFrame: The DataFrame with the transformation applied.
        """
        assert isinstance(df_to_transform, pd.DataFrame)

        # Create a copy of the DataFrame to avoid modifying the original
        df_to_transform[self.object_columns] = self.encoder.transform(df_to_transform[self.object_columns])
        return df_to_transform

    def inverse_transform(self, df_test):
        """
        Performs the inverse transformation using the encoder.

        Parameters:
            df_test (pandas.DataFrame): The DataFrame to inverse transform.

        Returns:
            pandas.DataFrame: The DataFrame with the inverse transformation applied.
        """

        # Check that our inverse_encoder dictionary is not empty
        assert isinstance(df_test, pd.DataFrame)
        if self.inverse_encoder is not None:
            for col_name in self.indices:
                if col_name in df_test.columns:
                    df_test[col_name] = df_test[col_name].map(self.inverse_encoder[col_name])

        return df_test
