import sys
sys.path.append(".")

from src.models.selection import select_variables
import pandas as pd
import unittest
class TestModels(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({'Target': [1, 0, 1],
                                  'Feature1': [1, 4, 3],
                                  'Feature2': [0.1, 0.3, 0.5],
                                  "string":["A","B","C"],
                                  "mixte":["str",1,0.5]})
        self.features = 10
    def test_select_variables_output_types(self):
        selected, importances = select_variables(self.df, 2)
        self.assertIsInstance(selected, pd.DataFrame, "Le résultat 'selected' doit être un objet DataFrame.")
        self.assertIsInstance(importances, pd.DataFrame, "Le résultat 'importances' doit être un objet DataFrame.")

    def test_select_variables(self):
        select_variables(self.df, 2)

    def test_select_variables_exceptions(self):
        # Test des exceptions
        with self.assertRaises(AssertionError):
            select_variables(self.df, 0)  # nb_feature doit être supérieur à zéro

        with self.assertRaises(AssertionError):
            select_variables(self.df, len(self.df.columns))  # nb_feature ne doit pas dépasser le nombre de colonnes - 1

        with self.assertRaises(AssertionError):
            select_variables(pd.DataFrame(), 2)  # Le DataFrame ne peut pas être vide

        # Test du type de données pour les paramètres
        with self.assertRaises(AssertionError):
            select_variables("invalid_df", 2)  # dataframe doit être un objet DataFrame

        with self.assertRaises(AssertionError):
            select_variables(self.df, "invalid_nb_feature")  # nb_feature doit être un entier

if __name__ == '__main__':
    unittest.main()