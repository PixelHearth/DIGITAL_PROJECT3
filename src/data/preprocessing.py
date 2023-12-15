from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
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
    def __init__(self, df):
        # asserts
        if not isinstance(df,pd.DataFrame):
            raise TypeError("input must be a dataframe")

        # Loading the encoding model
        self.encoder = OneHotEncoder(handle_unknown='ignore',sparse_output=False)

        # Get columns to train
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
        # Get Int type for first columns
        df = pd.concat([df.iloc[:, 0].astype(int),df.iloc[:,1:]],axis= 1)

        return df
    
    def fit(self):
        """DataFrame to fit the OneHotEncoder instanced in the class"""
        
        # Fit the encoder on the object dataset
        self.encoder.fit(self.df[self.object_columns])
        
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
        result_df = pd.concat([self.label_encoder(df), encoded_df], axis=1)
        
        return result_df
        
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
    
    def column_selection(self,rf_cols):
        """Get cols transformed by the transformer, split columns modified then drop duplicate, useful after a selection of variables

        Args:
            rf_cols (list): list of selected variable by the RandomForest

        Returns:
            rf_cols (list): list of columns selected to reduce dimension
        """
        #transform cols
        cols_transformed = self.encoder.get_feature_names_out(self.object_columns).tolist() 

        #variable selected
        col_selected = rf_cols 
        
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
    

class ScalerProcessor:
    """
    A class for scaling properties data and processing customer data using StandardScaler.

    Args:
    - properties (pd.DataFrame): The properties data to be scaled.
    - customer (pd.DataFrame): The customer data to be processed.

    Attributes:
    - properties (pd.DataFrame): The scaled properties data.
    - customer (pd.DataFrame): The processed customer data.
    - properties_scaler (StandardScaler): The scaler used for scaling properties data.
    """
    def __init__(self, properties, customer):
        self.properties = properties
        self.customer = customer
        self.properties_scaler = None

    def scale_properties(self):
        """
        Scale the numeric columns of the properties DataFrame.

        Exemple:
        >>> properties_data = pd.DataFrame({'Feature1': [10, 20, 30, 40], 'Feature2': [0.1, 0.2, 0.3, 0.4]})
        >>> customer_data = pd.DataFrame({'Feature1': [15, 25, 35], 'Feature2': [0.15, 0.25, 0.35]})
        >>> data_processor = ScalerProcessor(properties_data, customer_data)

        >>> data_processor.scale_properties()
        >>> scaled_properties = data_processor.properties
        >>> print(scaled_properties)
           Feature1  Feature2
        0  -1.341641 -1.341641
        1  -0.447214 -0.447214
        2   0.447214  0.447214
        3   1.341641  1.341641
        """
        # Identify numeric columns
        numeric_columns = self.properties.select_dtypes(include=['number']).columns

        # Create a new StandardScaler
        self.properties_scaler = StandardScaler()

        # Apply scaler to numeric columns
        self.properties[numeric_columns] = self.properties_scaler.fit_transform(self.properties[numeric_columns])

    def process_customer_data(self):
        """
        Process customer data using the mean and scale values from the properties scaler.

        Raises:
        - ValueError: If properties scaler has not been initialized.

        Exemple:
        >>> properties_data = pd.DataFrame({'Feature1': [10, 20, 30, 40], 'Feature2': [0.1, 0.2, 0.3, 0.4]})
        >>> customer_data = pd.DataFrame({'Feature1': [15, 25, 35], 'Feature2': [0.15, 0.25, 0.35]})
        >>> data_processor = ScalerProcessor(properties_data, customer_data)

        >>> data_processor.scale_properties()
        >>> data_processor.process_customer_data()
        >>> processed_customer = data_processor.customer
        >>> print(processed_customer)
           Feature1  Feature2
        0  -0.447214 -0.447214
        1   0.447214  0.447214
        2   1.341641  1.341641
        """
        if self.properties_scaler is None:
            raise ValueError("Properties scaler has not been initialized. Please scale properties first.")

        # Get the mean and scale from the properties scaler
        mean_values = self.properties_scaler.mean_
        scale_values = self.properties_scaler.scale_

        # Apply the mean and scale to the customer DataFrame
        for col, mean, scale in zip(self.customer.select_dtypes(include=['number']).columns, mean_values, scale_values):
            self.customer[col] = (self.customer[col] - mean) / scale

    def run_processing_pipeline(self):
        """
        Run the entire data processing pipeline.

        Exemple:
        >>> properties_data = pd.DataFrame({'Feature1': [10, 20, 30, 40], 'Feature2': [0.1, 0.2, 0.3, 0.4]})
        >>> customer_data = pd.DataFrame({'Feature1': [15, 25, 35], 'Feature2': [0.15, 0.25, 0.35]})
        >>> data_processor = ScalerProcessor(properties_data, customer_data)

        >>> data_processor.run_processing_pipeline()
        >>> scaled_properties = data_processor.properties
        >>> processed_customer = data_processor.customer
        >>> print(scaled_properties)
           Feature1  Feature2
        0  -1.341641 -1.341641
        1  -0.447214 -0.447214
        2   0.447214  0.447214
        3   1.341641  1.341641
        >>> print(processed_customer)
           Feature1  Feature2
        0  -0.447214 -0.447214
        1   0.447214  0.447214
        2   1.341641  1.341641
        """
        self.scale_properties()
        self.process_customer_data()

