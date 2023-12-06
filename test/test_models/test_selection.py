from src.models.selection import select_features
import pandas as pd
import unittest
class TestModels(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({'Target': [1, 0, 1],
                                  'Feature1': [1, 4, 3],
                                  'Feature2': [0.1, 0.3, 0.5],
                                  'Feature3': [3, 4, 5]})
        self.features = 2
        
    def test_select_features_output_types(self):
        selected, importances = select_features(self.df, self.features)
        self.assertIsInstance(selected, pd.Index, "Le résultat 'selected' doit être un objet DataFrame.")
        self.assertIsInstance(importances, pd.DataFrame, "Le résultat 'importances' doit être un objet DataFrame.")

    def test_select_features(self):
        select_features(self.df, self.features)

    def test_select_features_exceptions(self):
        # Test of the exceptions
        with self.assertRaises(AssertionError):
            select_features(self.df, self.features)  # nb_feature must be greater than 0

        with self.assertRaises(AssertionError):
            select_features(self.df, len(self.df.columns))  # nb_feature must not exceed the number of columns - 1

        with self.assertRaises(AssertionError):
            select_features(pd.DataFrame(), self.features)  # The DataFrame must not be empty

        # Test of the datatypes for parameters
        with self.assertRaises(AssertionError):
            select_features("invalid_df", self.features)  # dataframe must be a DataFrame object

        with self.assertRaises(AssertionError):
            select_features(self.df, "invalid_nb_feature")  # nb_feature must be an integer

if __name__ == '__main__':
    unittest.main()
