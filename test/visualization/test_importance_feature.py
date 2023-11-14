import unittest
import pandas as pd
import sys
from unittest.mock import patch
from io import StringIO
sys.path.append(".")
from src.visualization.importance_feature_graph import plot_feature_importance
class TestImportanceFeature(unittest.TestCase):
    def setUp(self):

        # Exemple de données
        self.data = pd.DataFrame({'Feature': ['Texte 1', 'Texte 2', 'Texte 3', 'Texte 4'],
                'Importance': [25, 30, 20, 25]})
        
        self.nb_feature = 4

    def test_plot_feature_importance(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            plot_feature_importance(self.data,self.nb_feature)
            self.assertEqual(mock_stdout.getvalue(), '')  # Vérifier qu'il n'y a pas de sortie stdout
        
if __name__ == "__main__":
    unittest.main()

