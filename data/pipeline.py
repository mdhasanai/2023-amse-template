import os
import pandas as pd
import sqlite3 as db


# Defining Data Sources
source_1 = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-ladesaulen-in-deutschland/exports/csv"
source_2 = "https://www.bundesnetzagentur.de/SharedDocs/Downloads/DE/Sachgebiete/Energie/Unternehmen_Institutionen/E_Mobilitaet/Ladesaeulenregister.xlsx?__blob=publicationFile&v=21"

table_name_1 = "table1"
table_name_2 = "table2"
save_in_local = False


def main():
    
    # Make a folder
    os.makedirs("./database", exist_ok=True)


    # Connect to the SQLite database
    conn = db.connect('./database/data.db')
    print("Database connection success!!!")

    # Load data from the database into a DataFrame
    df_1, df_2 = pull_data(source_1, source_2, save_in_local)
    print("Pulled data from the data sources")

    # Perform data analysis or manipulations on the DataFrame
    processed_df1 = process_data(df_1)
    processed_df2 = process_data(df_2)
    print("Processed dataset")

    # Save the processed data to a new table in the database
    store_data(processed_df1, conn, table_name_1)
    store_data(processed_df2, conn, table_name_2)
    print("data stored in the database")

    # Closing the database connection
    conn.close()
    print("Completed!!!")
  
    
def pull_data(data_source1, data_source2, save_in_local):
    """ Pulling the data from the data sources

    Returns:
        df: return data as pandas dataframe
    """
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(data_source1, delimiter=';', encoding='latin-1')
    dff = pd.read_excel(data_source2, skiprows=10)
    
    if save_in_local:
        df.to_csv("./database/source1.csv", sep='\t', encoding='utf-8')
        dff.to_csv("./database/source2.csv", sep='\t', encoding='utf-8')
    return df, dff


def process_data(df):
    """ Perform any necessary data transformations, cleaning, or manipulation on the DataFrame
    Returns:
        df: return data as pandas dataframe
    """
    
    # Step1: Handle missing values
    # Cheacking there is Nan value exists or Not
    if sum(df.isnull().sum().tolist())>0:
        # Dropping rows or columns with missing values
        df.dropna()
    
        # Step2: Clean and transform the data
        # Removing duplicates
        df.drop_duplicates()
    return df


def store_data(df, conn, table_name):    
    # Store the DataFrame in the database table
    #df.to_sql(table_name, conn, if_exists="replace", index=False)
    df.to_sql(table_name, conn, if_exists="replace", index=False)


def load_data_from_database(conn, table_name):
    # Write a SQL query to retrieve data from the database table
    query = f"SELECT * FROM {table_name}"
    
    # Execute the SQL query and load the data into a DataFrame
    df = pd.read_sql_query(query, conn)
    return df

if __name__ == '__main__':
    main()
