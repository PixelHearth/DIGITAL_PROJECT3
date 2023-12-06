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
        # Test des exceptions
        with self.assertRaises(AssertionError):
            select_features(self.df, self.features)  # nb_feature doit être supérieur à zéro

        with self.assertRaises(AssertionError):
            select_features(self.df, len(self.df.columns))  # nb_feature ne doit pas dépasser le nombre de colonnes - 1

        with self.assertRaises(AssertionError):
            select_features(pd.DataFrame(), self.features)  # Le DataFrame ne peut pas être vide

        # Test du type de données pour les paramètres
        with self.assertRaises(AssertionError):
            select_features("invalid_df", self.features)  # dataframe doit être un objet DataFrame

        with self.assertRaises(AssertionError):
            select_features(self.df, "invalid_nb_feature")  # nb_feature doit être un entier

if __name__ == '__main__':
    unittest.main()