import os
import sys
import unittest
import pandas as pd
from pipeline import pull_data
# Appending path
sys.path.append(os.path.dirname(os.path.abspath('')))


class TestDataPull(unittest.TestCase):
    def test_pull_data(self):
        
        # Defining Data Sources
        source_1 = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-ladesaulen-in-deutschland/exports/csv"
        source_2 = "https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/E_Mobilitaet/Ladesaeulenregister.xlsx?__blob=publicationFile&v=21"

        # Test data sources
        data_source1 = './database/source1.csv'
        data_source2 = "./database/source2.csv"
        
        # Define expected results
        expected_df = pd.read_csv(data_source1, sep='\t', encoding='utf-8', index_col = [0])
        expected_dff = pd.read_csv(data_source2, sep='\t', encoding='utf-8', index_col = [0])
        
        # Call the function to pull the data
        df, dff = pull_data(source_1, source_2, False)
        
        # Perform assertions to check if the actual results match the expected results
        self.assertTrue(df.equals(expected_df), "DataFrame from source 1 'df' does not match the expected result.")
        self.assertTrue( len(df)==len(expected_df), "Data is not same size from source 1")
        
        # self.assertTrue(dff.equals(expected_dff), "DataFrame from source 2 ('dff') does not match the expected result.")
        
if __name__ == '__main__':
    unittest.main()