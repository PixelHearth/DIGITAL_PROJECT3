import os
import unittest
import pandas as pd
from openpyxl import Workbook
import sys
sys.path.append(".")
from src.data.make_dataset import importation_excel

class TestImportationExcel(unittest.TestCase):

    def setUp(self):
        # Create a sample Excel file for testing
        self.test_excel_file = 'test_file.xlsx'
        self.test_sheet_name = 'Feuil1'
        workbook = Workbook()
        sheet = workbook.active
        sheet.append(['Name', 'Age', 'City'])
        sheet.append(['John Doe', 25, 'New York'])
        workbook.save(self.test_excel_file)

    def tearDown(self):
        # Clean up the test Excel file
        if os.path.exists(self.test_excel_file):
            os.remove(self.test_excel_file)

    def test_importation_excel_success(self):
        # Test the function with a valid Excel file and sheet
        df = importation_excel(self.test_excel_file, self.test_sheet_name)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertListEqual(list(df.columns), ['Name', 'Age', 'City'])

    def test_importation_excel_file_not_found(self):
        # Test the function with a non-existing Excel file
        with self.assertRaises(FileNotFoundError):
            importation_excel('non_existing_file.xlsx', self.test_sheet_name)

    def test_importation_excel_sheet_not_found(self):
        # Test the function with a non-existing sheet in the Excel file
        with self.assertRaises(ValueError):
            importation_excel(self.test_excel_file, 'NonExistingSheet')

    def test_importation_excel_empty_column_names(self):
        # Test the function with an Excel file containing empty column names
        workbook = Workbook()
        sheet = workbook.active
        sheet.append([None, None, None])
        workbook.save(self.test_excel_file)

        with self.assertRaises(ValueError):
            importation_excel(self.test_excel_file, self.test_sheet_name)

if __name__ == '__main__':
    unittest.main()
