import os
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer


def get_config():
    """Returns the configuaration

    Returns:
        conf: a python dictionary that contains the paramaeters for the ETL pipeline
    """
    # Defining Data Sources
    source = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
    
    # Setting up the configuaration
    conf = {
        "source1": source,
        "database_dir": "./database",
        "database_name": "sqlite:///airports.sqlite",
        "table_name" : "airports",
        "transformation": {
            "drop_missing_value": False,
            "drop_duplicate": False
        }
    }
    return conf


class ETL:
    
    def __init__(self, conf):
        self.config = conf

    def load_data(self):
        """Pulling the data from the data sources

        Returns:
            df: returns the data from source as pandas dataframe
        """
        
        print("LOading the data from the data source")
        # Load the data from the sources as pandas DataFrame
        df = pd.read_csv(self.config['source1'], delimiter=';')
        return df
    
    
    def transform_data(self, df):
        """ Perform any necessary data transformations, cleaning, or manipulation on the DataFrame
        Returns:
            df: return data as pandas dataframe
        """
        
        print("Transforming data")
        if self.config['transformation']['drop_missing_value']==True:
            # Cheacking there is Nan value exists or Not
            if sum(df.isnull().sum().tolist())>0:
                # Dropping rows or columns with missing values
                df.dropna()
        elif self.config['transformation']['drop_duplicate']==True:
            # Removing duplicates
            df.drop_duplicates()
            
        return df
    
    
    def push_to_databse(self, engine, df, table_name):
        """ Insert the data into the database
        Returns:
            response: return the response
        """
        # Define the metadata and table schema
        metadata = MetaData()
        
        # Generate the column types from the DataFrame
        column_types = {column: String(length=255) if dtype == 'object' else Integer() for column, dtype in df.dtypes.items()}

        # Define the table using the column types
        data_table = Table(
            table_name,
            metadata,
            Column('id', Integer, primary_key=True),
            *(Column(column, column_type) for column, column_type in column_types.items())
        )


        print("Pushing the data into databse")
        status = 440
        message = ''
        try:
            # Create the table in the database
            metadata.create_all(engine)
            
            # Convert the DataFrame to a list of dictionaries
            data_to_insert = df.to_dict(orient='records')
            
            # Open a connection and insert the data into the table
            with engine.begin() as connection:
                connection.execute(data_table.insert(), data_to_insert)


            # Write the data from the DataFrame into the table
            # df.to_sql(table_name, engine, if_exists="replace", index=False)
            status = 500
            message = "data intertion success!"
        except Exception as e:
            status = 440
            message = f"data couln't able to push into the databse due to following error: \n {str(e)}"
        return {"message": message, "status": status}
       
       
    def pull_data_from_databse(self, engine=None, table_name=None):
        """ Pull the data from the database
        Returns:
            response: return data as dataframe
        """
        
        # Setting default table name to load
        if table_name is None:
            table_name = self.config['table_name']
            
        status = 440
        message = ''
        loaded_df = None
        if engine is None:
            try:
                #databse_path = os.path.join(self.config["database_dir"], self.config["database_name"])
                database_path = self.config["database_name"]
                engine = create_engine(f"{database_path}")
                
                # Load the database from the folder
                loaded_df = pd.read_sql_table(table_name, engine)
                status = 500
                message = "data extraction success!"
            except Exception as e:
                status = 440
                message = f"data couln't able to pull due to following error: \n {str(e)}"

        return {"data":loaded_df ,"message": message, "status": status}
      
        
    def process_data(self):
        """Process the data

        Returns:
            df: returns the data from source as pandas dataframe
        """
        # Making a folder to store the database
        os.makedirs("./database", exist_ok=True)
        
        # Defining SQLAlchemy connection
        # databse_path = os.path.join(self.config["database_dir"], self.config["database_name"])
        databse_path = self.config["database_name"]
        print(databse_path)
        engine = create_engine(f"{databse_path}")
        
        # Loading
        df = self.load_data()
        
        # Transform data
        df = self.transform_data(df)
        
        # Push data into database
        response = self.push_to_databse(engine, df, self.config["table_name"])
        
        # closing the engine
        engine.dispose()
        return response


def main():
    
    print("*"*20, "ETL PIPELINE STARTED", "*"*20)
    # Getting the configuaration
    config = get_config()
    
    # Define the ETL pipeline
    etl_pipeline = ETL(config)
    process_response = etl_pipeline.process_data()
    print(process_response)
    
    pull_response = etl_pipeline.pull_data_from_databse()
    print(pull_response)
    
    print("#"*20, "ETL PIPELINE ENDED", "#"*20)
    

if __name__ == '__main__':
	main()      
        
        
        

        

        
        
    
