from src.models.train_model import Models
import pandas as pd
import unittest
import pandas.api.types as ptypes

# The goal is to test the function k neighbors in the class model

class TestModels(unittest.TestCase):
    def setUp(self):
        # Training data
        df = pd.DataFrame({'Target': [1, 0, 1],
                                  'Feature1': [1, 4, 3],
                                  'Feature2': [0.1, 0.3, 0.5]})
        # Test data
        individual_data = pd.DataFrame({'Target': [1],
                                        'Feature1': [3], 
                                        'Feature2': [0.4]})
        self.models_instance = Models(df, individual_data)
        
    def test_dfs_type(self):
        # Checking if training and test data are pandas df
        self.assertIsInstance(self.models_instance.df, pd.DataFrame)
        self.assertIsInstance(self.models_instance.df_customer, pd.DataFrame)

    def test_dfs_not_empty(self):
        # Checking if dfs are not empty
        self.assertTrue(len(self.models_instance.df) > 0)
        self.assertTrue(len(self.models_instance.df_customer) > 0)

    def test_dfs_same_columns(self):
        # Checking if dfs have the same number of columns
        self.assertEqual(len(self.models_instance.df.columns), len(self.models_instance.df_customer.columns))

    def test_dfs_columns_types(self):
        #  Checking if columns datatypes are int or float
        self.assertTrue(all(ptypes.is_numeric_dtype(self.models_instance.df[col])for col in self.models_instance.df.columns))
        self.assertTrue(all(ptypes.is_numeric_dtype(self.models_instance.df_customer[col])for col in self.models_instance.df_customer.columns))

    def test_k_neighbors_output_type(self):
        # Checking if the output of the k_neighbors method is a df
        result,proba = self.models_instance.k_neighbors(3)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIsInstance(proba,list)

if __name__ == '__main__':
    unittest.main()
