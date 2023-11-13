import unittest
import pandas as pd
import sys
sys.path.append(".")
from src.data.preprocessing import CustomPreprocessor

# class TestCustomPreprocessor(unittest.TestCase):
#     def setUp(self):
#         try:
#             data = {
#                 'Category': ['A', 'B', 'A', 'C'],
#                 'Color': [3, 5, 4, 5]
#             }
#             self.df = pd.DataFrame(data)
#             self.preprocessor = CustomPreprocessor(self.df)
#             self.preprocessor.fit()
#             self.encoded_df = self.preprocessor.transform(self.df.copy())
#             print("test1 passed")
#         except:
#             print("test1 failed")

#     def test_transform(self):
#         # Vérifiez que la transformation a été effectuée correctement
#         try:
#             expected_encoded_data = {
#                 'Category': [0.0, 1.0, 0.0, 2.0],
#                 'Color': [3, 5, 4, 5]
#             }
#             expected_encoded_df = pd.DataFrame(expected_encoded_data)
#             pd.testing.assert_frame_equal(self.encoded_df, expected_encoded_df)
#             print("test2 Passed")
#         except:
#             print("test2 failed")
#     def test_inverse_transform(self):
#         try:
#             # Vérifiez que la transformation inverse fonctionne correctement
#             decoded_df = self.preprocessor.inverse_transform(self.encoded_df.copy())
#             pd.testing.assert_frame_equal(decoded_df, self.df)
#             print("test3 Passed")
#         except:
#             print("test3 failed")

class TestCustomPreprocessor(unittest.TestCase):
    def setUp(self):
        data = {
            'Category': ['A', 'A', 'B', 'C'],
            'Color': [3, 5, 4, 5]
        }
        
        self.df = pd.DataFrame(data)
        self.preprocessor = CustomPreprocessor(self.df)
        self.preprocessor.fit()
        self.encoded_df = self.preprocessor.transform(self.df.copy())

    def test_transform(self):
        expected_encoded_data = {
            'Category': [0.0, 0.0, 1.0, 2.0],
            'Color': [3, 5, 4, 5]
        }
        expected_encoded_df = pd.DataFrame(expected_encoded_data)
        pd.testing.assert_frame_equal(self.encoded_df, expected_encoded_df)

    def test_inverse_transform(self):
        decoded_df = self.preprocessor.inverse_transform(self.encoded_df.copy())
        pd.testing.assert_frame_equal(decoded_df, self.df)

if __name__ == '__main__':
    unittest.main()
