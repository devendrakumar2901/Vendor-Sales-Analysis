import pandas as pd
import os 
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename ="logs/ingestion_db.log",
    level = logging.DEBUG,
    format ="%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)

engine = create_engine('sqlite:///inventory.db')

print(os.getcwd())  # Current working directory
print(os.listdir()) # Files and folders here


def ingest_db(df, table_name, engine):
    ''' This function will ingest dataframe into database table. '''
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)

def load_raw_data():
    """this function will load  CSVs as dataframe and ingest into db"""
    start = time.time()
    for file in os.listdir('data'):
        if file.endswith('.csv'):
           df = pd.read_csv('data/' + file)
           logging.info(f'ingesting {file} in db')
           ingest_db(df, file[:-4], engine)

    end = time.time()
    total_time = (end - start)/60
    logging.info('--------ingestion complete---------')

    logging.info(f'\nTotal time taken: {total_time}minutes')

if __name__ == "__main__":
    load_raw_data()
