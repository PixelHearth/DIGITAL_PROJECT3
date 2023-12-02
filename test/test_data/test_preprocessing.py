import unittest
import pandas as pd
import sys
sys.path.append(".")
from src.data.preprocessing import CustomProcessing

class TestCustomProcessing(unittest.TestCase):
    def setUp(self):
        # Create a sample DataFrame for testing
        data = {'Category': ['A', 'B', 'C', 'A', 'B'], 'color': ['blue', 'red', 'red', 'blue', 'grey']}
        self.df = pd.DataFrame(data)
        self.custom_processing = CustomProcessing(self.df)

    def test_label_encoder(self):
        # Test if label_encoder method transforms the first column correctly
        df_transformed = self.custom_processing.label_encoder(self.df.copy())
        self.assertTrue(df_transformed['Category'].dtype == 'int64')
        self.assertTrue(df_transformed['color'].dtype == 'object')    
            
    def test_fit_transform(self):
        # Test if fit_transform method encodes object columns correctly
        self.custom_processing.fit()
        df_transformed = self.custom_processing.fit_transform(self.df.copy())
        self.assertEqual(df_transformed.shape, (5, 4))  # Assuming 3 unique categories in the sample data

    def test_transform(self):
        # Test if transform method encodes object columns correctly
        self.custom_processing.fit()
        df_transformed = self.custom_processing.transform(self.df.copy())
        self.assertEqual(df_transformed.shape, (5, 4))  # Assuming 3 unique categories in the sample data

    def test_inverse_transform(self):
        # Test if inverse_transform method reverses the transformation correctly
        self.custom_processing.fit()
        df_transformed = self.custom_processing.transform(self.df.copy())
        df_inverse = self.custom_processing.inverse_transform(df_transformed.copy())
        self.assertTrue(all(col in df_inverse.columns for col in self.custom_processing.object_columns))

    def test_column_selection(self):
        # Test if column_selection method selects columns correctly
        self.custom_processing.fit()
        df_transformed = self.custom_processing.fit_transform(self.df.copy())
        selected_cols = df_transformed.columns[:3].tolist()  # Select first 3 columns for testing
        selected_cols_after = self.custom_processing.column_selection(selected_cols)
        self.assertTrue(all(col in selected_cols_after for col in self.custom_processing.object_columns))

if __name__ == '__main__':
    unittest.main()

    

if __name__ == '__main__':
    unittest.main()
