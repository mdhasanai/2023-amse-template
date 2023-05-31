import os
import sys
import unittest
import pandas as pd
import sqlite3 as db
# Appending path
print(os.path.dirname(__file__))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('../data')
from data.pipeline import pull_data

print(os.path.dirname(__file__))

class TestDataPull(unittest.TestCase):
    def test_pull_data(self):
        
        # Defining Data Sources
        source_1 = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-ladesaulen-in-deutschland/exports/csv"
        source_2 = "https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/E_Mobilitaet/Ladesaeulenregister.xlsx?__blob=publicationFile&v=21"

        # Test data sources
        conn = db.connect('../data/database/data.db')
        
        # Define expected results
        expected_df  = pd.read_sql_query(f"SELECT * FROM table1", conn)
        expected_dff = pd.read_sql_query(f"SELECT * FROM table2", conn)
        
        # Call the function to pull the data
        df, dff = pull_data(source_1, source_2, False)
        
        # Perform assertions to check if the actual results match the expected results
        self.assertTrue(df.equals(expected_df), "DataFrame from source 1 'df' does not match the expected result.")
        self.assertTrue( len(df)==len(expected_df), "Data is not same size from source 1")
        
        #self.assertTrue(dff.equals(expected_dff), "DataFrame from source 2 ('dff') does not match the expected result.")
        #self.assertTrue(len(dff)==len(expected_dff), "Data is not same size from source 1")
        
        conn.close()
        
if __name__ == '__main__':
    unittest.main()