from src.models.train_model import Models
import pandas as pd
import unittest
import pandas.api.types as ptypes

# l'objectif est de tester la fonction k neighbors dans la class model

class TestModels(unittest.TestCase):
    def setUp(self):
        # Données d'entraînement
        df = pd.DataFrame({'Target': [1, 0, 1],
                                  'Feature1': [1, 4, 3],
                                  'Feature2': [0.1, 0.3, 0.5]})
        # Données de test
        individual_data = pd.DataFrame({'Target': [1],
                                        'Feature1': [3], 
                                        'Feature2': [0.4]})
        self.models_instance = Models(df, individual_data)
        
    def test_dfs_type(self):
        # Vérifie que les données d'entraînement et de test sont des dfs pandas
        self.assertIsInstance(self.models_instance.df, pd.DataFrame)
        self.assertIsInstance(self.models_instance.df_customer, pd.DataFrame)

    def test_dfs_not_empty(self):
        # Vérifie que les dfs ne sont pas vides
        self.assertTrue(len(self.models_instance.df) > 0)
        self.assertTrue(len(self.models_instance.df_customer) > 0)

    def test_dfs_same_columns(self):
        # Vérifie que les dfs ont le même nombre de colonnes
        self.assertEqual(len(self.models_instance.df.columns), len(self.models_instance.df_customer.columns))

    def test_dfs_columns_types(self):
        # Vérifie que les types de données des colonnes sont int ou float
        self.assertTrue(all(ptypes.is_numeric_dtype(self.models_instance.df[col])for col in self.models_instance.df.columns))
        self.assertTrue(all(ptypes.is_numeric_dtype(self.models_instance.df_customer[col])for col in self.models_instance.df_customer.columns))

    def test_k_neighbors_output_type(self):
        # Vérifie que la sortie de la méthode k_neighbors est un df
        result,proba = self.models_instance.k_neighbors(3)
        self.assertIsInstance(result, pd.DataFrame)
        self.assertIsInstance(proba,list)

if __name__ == '__main__':
    unittest.main()