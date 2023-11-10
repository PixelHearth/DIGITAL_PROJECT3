# Pour tester le K_neighbors algorithmes on doit s'assurer que la variable entrée est bien un dataframe, qu'il est ne contient pas de none, date, ou autre
import sys 
sys.path.append(".")
from src.models.train_model import Models
import pandas as pd
import unittest
import pandas.api.types as ptypes

# l'objectif est de tester la fonction k neighbors dans la class model

class TestModels(unittest.TestCase):

    def test_kneighbors_int_float(self):
        # Données d'entraînement
        dataframe = pd.DataFrame({'Target': [1, 0, 1],
                                  'Feature1': [1, 4, 3],
                                  'Feature2': [0.1, 0.3, 0.5],
                                  "string":["A","B","C"],
                                  "mixte":["str",1,0.5]})
        # Données de test
        individual_data = pd.DataFrame({'Feature1': [3], 
                                        'Feature2': [0.4],
                                        "string":["B"],
                                        "mixte":["str"]})
        self.models_instance = Models(dataframe, individual_data)

    def test_dataframes_type(self):
        # Vérifie que les données d'entraînement et de test sont des dataframes pandas
        self.assertIsInstance(self.models_instance.dataframe, pd.DataFrame)
        self.assertIsInstance(self.models_instance.individual_features, pd.DataFrame)

    def test_dataframes_not_empty(self):
        # Vérifie que les dataframes ne sont pas vides
        self.assertTrue(len(self.models_instance.dataframe) > 0)
        self.assertTrue(len(self.models_instance.individual_features) > 0)

    def test_dataframes_same_columns(self):
        # Vérifie que les dataframes ont le même nombre de colonnes
        self.assertEqual(len(self.models_instance.dataframe.columns), len(self.models_instance.individual_features.columns)+1)

    def test_dataframes_columns_types(self):
        # Vérifie que les types de données des colonnes sont int ou float
        self.assertTrue(all(ptypes.is_numeric_dtype(self.models_instance.dataframe[col])for col in self.models_instance.dataframe.columns))
        self.assertTrue(all(ptypes.is_numeric_dtype(self.models_instance.individual_features[col])for col in self.models_instance.individual_features.columns))

    def test_k_neighbors_output_type(self):
        # Vérifie que la sortie de la méthode k_neighbors est un DataFrame
        result = self.models_instance.k_neighbors()
        self.assertIsInstance(result, pd.DataFrame)

if __name__ == '__main__':
    unittest.main()