import pandas as pd
import sys
sys.path.append(".")
from src.data.fonctions_filtrage import *
import numpy as np
import unittest



class TestDeleteNAFunction(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        self.df = pd.DataFrame({'A': [1, 2, np.nan, 4], 'B': [5, np.nan, 7, 8]})

    def test_delete_na_column_present(self):
        # Test when the specified column is present
        column_name = 'A'
        df_result = delete_na(self.df, column_name)
        expected_result = pd.DataFrame({'A': [1.0, 2.0, 4.0], 'B': [5.0, np.nan, 8.0]})
        pd.testing.assert_frame_equal(df_result, expected_result)

    def test_delete_na_column_not_present(self):
        # Test when the specified column is not present
        column_name = 'C'
        df_result = delete_na(self.df, column_name)
        # The result should be the same as the original DataFrame
        pd.testing.assert_frame_equal(df_result, self.df)


class TestReplaceValueFunction(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        self.df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': ['a', 'b', 'a', 'c']})

    def test_replace_value_column_present(self):
        # Test when the specified column is present
        column_name = 'B'
        value_a = 'a'
        value_b = 'x'
        df_result = replace_value(self.df, column_name, value_a, value_b)
        expected_result = pd.DataFrame({'A': [1, 2, 3, 4], 'B': ['x', 'b', 'x', 'c']})
        pd.testing.assert_frame_equal(df_result, expected_result)

    def test_replace_value_column_not_present(self):
        # Test when the specified column is not present
        column_name = 'C'
        value_a = 'a'
        value_b = 'x'
        df_result = replace_value(self.df, column_name, value_a, value_b)
        # The result should be the same as the original DataFrame
        pd.testing.assert_frame_equal(df_result, self.df)
        
        
class TestConditionalFillNAFunction(unittest.TestCase):

    def test_conditional_fill_na(self):
        # Test the conditional_fill_na function
        data = {'col1': [1, 2, None], 'col2': ['a', 'b', None], 'col3': [4.0, 5.0, None]}
        df = pd.DataFrame(data)
        
        # Expected result after applying conditional_fill_na
        expected_result = pd.DataFrame({
            'col1': [1.0, 2.0, 1.5],
            'col2': ['a', 'b', 'unknown'],
            'col3': [4.0, 5.0, 4.5]
        })
        
        df_result = conditional_fill_na(df)
        
        # Check if the resulting DataFrame is equal to the expected result
        pd.testing.assert_frame_equal(df_result, expected_result)

    def test_conditional_fill_na_empty_dataframe(self):
        # Test the conditional_fill_na function with an empty DataFrame
        empty_df = pd.DataFrame()
        
        # The result should be an empty DataFrame as well
        df_result = conditional_fill_na(empty_df)
        
        # Check if the resulting DataFrame is empty
        self.assertTrue(df_result.empty)

    def test_conditional_fill_na_non_dataframe_input(self):
        # Test the conditional_fill_na function with a non-DataFrame input
        non_df_input = [1, 2, 3]
        
        # The function should raise an AssertionError
        with self.assertRaises(AssertionError):
            conditional_fill_na(non_df_input)



class TestConvertObjectColumnsToIntegersFunction(unittest.TestCase):

    def test_convert_object_columns_to_integers(self):
        # Test the convert_object_columns_to_integers function
        data = {'col1': ['1', 'A', '2'], 'col2': ['a', 'b', 'c']}
        df = pd.DataFrame(data)

        # Expected result after applying convert_object_columns_to_integers
        expected_result = pd.DataFrame({
            'col1': [1.0, None, 2.0],
            'col2': ['a', 'b', 'c']
        })
        
        df_result = convert_object_columns_to_integers(df)
        
        # Check if the resulting DataFrame is equal to the expected result
        pd.testing.assert_frame_equal(df_result, expected_result)

    def test_convert_object_columns_to_integers_empty_dataframe(self):
        # Test the convert_object_columns_to_integers function with an empty DataFrame
        empty_df = pd.DataFrame()

        # The result should be an empty DataFrame as well
        df_result = convert_object_columns_to_integers(empty_df)
        
        # Check if the resulting DataFrame is empty
        self.assertTrue(df_result.empty)

    def test_convert_object_columns_to_integers_non_dataframe_input(self):
        # Test the convert_object_columns_to_integers function with a non-DataFrame input
        non_df_input = [1, 2, 3]

        # The function should raise an AssertionError
        with self.assertRaises(AssertionError):
            convert_object_columns_to_integers(non_df_input)

    def test_convert_object_columns_to_integers_with_strings(self):
        # Test the convert_object_columns_to_integers function with strings that cannot be converted
        data = {'col1': ['A', 'B', 'C'], 'col2': ['a', 'b', 'c']}
        df = pd.DataFrame(data)

        # The result should be the same as the original DataFrame
        df_result = convert_object_columns_to_integers(df)

        # Check if the resulting DataFrame is equal to the original DataFrame
        pd.testing.assert_frame_equal(df_result, df)



class TestSeparateColumnsFunction(unittest.TestCase):

    def test_separate_columns(self):
        # Test the separate_columns function
        data = {'Tags': ['python, data', 'data science', 'java', 'python', np.nan]}
        df = pd.DataFrame(data)

        # Expected result after applying separate_columns
        expected_result = pd.DataFrame({
            'Tags python': [0, 0, 0, 0, None],
            'Tags java': [1, 0, 1, 0, None],
            'Tags data': [1, 0, 0, 1, None]
        })
        
        df_result = separate_columns(df, 'Tags', ['python', 'java', 'data'])
        
        # Check if the resulting DataFrame is equal to the expected result
        pd.testing.assert_frame_equal(df_result, expected_result)

    def test_separate_columns_column_not_present(self):
        # Test the separate_columns function when the specified column is not present
        data = {'Tags': ['python, data', 'data science', 'java', 'python', np.nan]}
        df = pd.DataFrame(data)

        # The result should be the same as the original DataFrame
        df_result = separate_columns(df, 'TagsNotExist', ['python', 'java', 'data'])
        
        # Check if the resulting DataFrame is equal to the original DataFrame
        pd.testing.assert_frame_equal(df_result, df)

    def test_separate_columns_empty_dataframe(self):
        # Test the separate_columns function with an empty DataFrame
        empty_df = pd.DataFrame()

        # The result should be an empty DataFrame as well
        df_result = separate_columns(empty_df, 'Tags', ['python', 'java', 'data'])
        
        # Check if the resulting DataFrame is empty
        self.assertTrue(df_result.empty)

    def test_separate_columns_with_nan_values(self):
        # Test the separate_columns function with NaN values in the original column
        data = {'Tags': [np.nan, 'data science', 'java', 'python', 'python, data']}
        df = pd.DataFrame(data)

        # Expected result after applying separate_columns
        expected_result = pd.DataFrame({
            'Tags python': [None, 0, 0, 0, 1],
            'Tags java': [None, 0, 1, 0, 0],
            'Tags data': [None, 0, 0, 0, 1]
        })

        df_result = separate_columns(df, 'Tags', ['python', 'java', 'data'])

        # Check if the resulting DataFrame is equal to the expected result
        pd.testing.assert_frame_equal(df_result, expected_result)
        
        

class TestCommaCountFunction(unittest.TestCase):

    def test_comma_count(self):
        # Test the comma_count function
        string = "['modality1', 'modality2', 'got it']"
        result = comma_count(string)
        expected_result = 3

        # Check if the result is equal to the expected result
        self.assertEqual(result, expected_result)

    def test_comma_count_empty_string(self):
        # Test the comma_count function with an empty string
        string = ""
        result = comma_count(string)
        expected_result = 0

        # Check if the result is equal to the expected result
        self.assertEqual(result, expected_result)

    def test_comma_count_nan_string(self):
        # Test the comma_count function with a NaN string
        string = pd.NA
        result = comma_count(string)

        # The result should be None for NaN string
        self.assertIsNone(result)

    def test_comma_count_non_string_input(self):
        # Test the comma_count function with a non-string input
        non_string_input = 123
        result = comma_count(non_string_input)
        expected_result = 0

        # Check if the result is equal to the expected result
        self.assertEqual(result, expected_result)
        
        

class TestListToIntAndSelectColumnsFunctions(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        data = {'Modalities': ["['modality1', 'modality2', 'got it']", "['option1', 'option2']", np.nan],
                'A': [1, 2, 3],
                'B': ['a', 'b', 'c'],
                'C': [True, False, True]}
        self.df = pd.DataFrame(data)

    def test_list_to_int(self):
        # Test the list_to_int function
        column_name = 'Modalities'
        df_result = list_to_int(self.df.copy(), column_name)

        # Expected result after applying list_to_int
        expected_result = pd.DataFrame({'Modalities': [3, 2, None],
                                        'A': [1, 2, 3],
                                        'B': ['a', 'b', 'c'],
                                        'C': [True, False, True]})
        
        # Check if the resulting DataFrame is equal to the expected result
        pd.testing.assert_frame_equal(df_result, expected_result)

    def test_list_to_int_column_not_present(self):
        # Test the list_to_int function when the specified column is not present
        column_name = 'NotPresentColumn'
        df_result = list_to_int(self.df.copy(), column_name)

        # The result should be the same as the original DataFrame
        pd.testing.assert_frame_equal(df_result, self.df)

    def test_select_columns(self):
        # Test the select_columns function
        columns_to_keep = ['A', 'C']
        df_result = select_columns(self.df.copy(), columns_to_keep)

        # Expected result after applying select_columns
        expected_result = pd.DataFrame({'A': [1, 2, 3],
                                        'C': [True, False, True]})
        
        # Check if the resulting DataFrame is equal to the expected result
        pd.testing.assert_frame_equal(df_result, expected_result)

    def test_select_columns_some_columns_not_present(self):
        # Test the select_columns function when some specified columns are not present
        columns_to_keep = ['A', 'NotPresentColumn', 'C']
        df_result = select_columns(self.df.copy(), columns_to_keep)

        # Expected result after applying select_columns (excluding 'NotPresentColumn')
        expected_result = pd.DataFrame({'A': [1, 2, 3],
                                        'C': [True, False, True]})
        
        # Check if the resulting DataFrame is equal to the expected result
        pd.testing.assert_frame_equal(df_result, expected_result)



class TestSwitchFirstColumnFunction(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        data = {'A': [1, 2, 3],
                'B': ['a', 'b', 'c'],
                'C': [True, False, True]}
        self.df = pd.DataFrame(data)

    def test_switch_first_column(self):
        # Test the switch_first_column function
        column_name = 'B'
        df_result = switch_first_column(self.df.copy(), column_name)

        # Expected result after applying switch_first_column
        expected_result = pd.DataFrame({'B': ['a', 'b', 'c'],
                                        'A': [1, 2, 3],
                                        'C': [True, False, True]})
        
        # Check if the resulting DataFrame is equal to the expected result
        pd.testing.assert_frame_equal(df_result, expected_result)

    def test_switch_first_column_column_not_present(self):
        # Test the switch_first_column function when the specified column is not present
        column_name = 'NotPresentColumn'
        df_result = switch_first_column(self.df.copy(), column_name)

        # The result should be the same as the original DataFrame
        pd.testing.assert_frame_equal(df_result, self.df)

    def test_switch_first_column_empty_dataframe(self):
        # Test the switch_first_column function with an empty DataFrame
        empty_df = pd.DataFrame()

        # The result should be an empty DataFrame as well
        df_result = switch_first_column(empty_df, 'A')
        
        # Check if the resulting DataFrame is empty
        self.assertTrue(df_result.empty)
        


class TestReplaceNAValueFunction(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        data = {'A': [1, 2, np.nan, 4],
                'B': ['a', 'b', 'c', np.nan]}
        self.df = pd.DataFrame(data)

    def test_replace_na_value(self):
        # Test the replace_na_value function
        column_name = 'A'
        replacement_value = 0
        df_result = replace_na_value(self.df.copy(), column_name, replacement_value)

        # Expected result after applying replace_na_value
        expected_result = pd.DataFrame({'A': [1, 2, 0, 4],
                                        'B': ['a', 'b', 'c', np.nan]})
        
        # Check if the resulting DataFrame is equal to the expected result
        pd.testing.assert_frame_equal(df_result, expected_result)

    def test_replace_na_value_column_not_present(self):
        # Test the replace_na_value function when the specified column is not present
        column_name = 'NotPresentColumn'
        replacement_value = 0
        df_result = replace_na_value(self.df.copy(), column_name, replacement_value)

        # The result should be the same as the original DataFrame
        pd.testing.assert_frame_equal(df_result, self.df)

    def test_replace_na_value_empty_dataframe(self):
        # Test the replace_na_value function with an empty DataFrame
        empty_df = pd.DataFrame()

        # The result should be an empty DataFrame as well
        df_result = replace_na_value(empty_df, 'A', 0)
        
        # Check if the resulting DataFrame is empty
        self.assertTrue(df_result.empty)
        
        

class TestCountNAPerColumnFunction(unittest.TestCase):

    def setUp(self):
        # Create a sample DataFrame for testing
        data = {'A': [1, 2, np.nan, 4],
                'B': ['a', 'b', 'c', np.nan],
                'C': [np.nan, np.nan, 3, 4]}
        self.df = pd.DataFrame(data)

    def test_count_na_per_column(self):
        # Test the count_na_per_column function
        df_result = count_na_per_column(self.df.copy())

        # Expected result after applying count_na_per_column
        expected_result = pd.DataFrame({'Column': ['A', 'B', 'C'],
                                        'NA_Count': [1, 1, 2]})
        
        # Check if the resulting DataFrame is equal to the expected result
        pd.testing.assert_frame_equal(df_result, expected_result)

    def test_count_na_per_column_empty_dataframe(self):
        # Test the count_na_per_column function with an empty DataFrame
        empty_df = pd.DataFrame()

        # The result should be an empty DataFrame as well
        df_result = count_na_per_column(empty_df)
        
        # Check if the resulting DataFrame is empty
        self.assertTrue(df_result.empty)

class TestConvertObjectColumnsToIntegers(unittest.TestCase):

    def test_conversion(self):
        # Create a DataFrame of test
        data = {
            'Column1': [1, '2', '3', '4'],
            'Column2': ['a', None, 'c', 'd'],
            'Column3': [1.1, 2.2, 3.3, 4.4],
        }
        df = pd.DataFrame(data)

        # Calling the function to test
        result_df = convert_object_columns_to_integers(df)
        print(result_df)
        # Checking if columns were converted correctly
        self.assertTrue(result_df['Column1'].dtype == 'float64')
        self.assertTrue(result_df['Column2'].dtype == 'object')  # Not converted
        self.assertTrue(result_df['Column3'].dtype == 'float64')  # Not converted

if __name__ == '__main__':
    unittest.main()
