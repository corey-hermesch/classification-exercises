### IMPORTS 

from env import host, user, password
import os
import numpy as np
import pandas as pd
# from scipy import stats
# import matplotlib.pyplot as plt
# import seaborn as sns
np.random.seed(42)
### FUNCTIONS 

def get_db_url(db_name, user=user, host=host, password=password):
    '''
    get_db_url accepts a database name, username, hostname, password 
    and returns a url connection string formatted to work with codeup's 
    sql database.
    Default values from env.py are provided for user, host, and password.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'

# generic function to get a sql pull into a dataframe
def get_mysql_data(sql_query, database):
    """
    This function will:
    - take in a sql query and a database (both strings)
    - create a connection url to mySQL database
    - return a df of the given query, connection_url combo
    """
    url = get_db_url(database)
    return pd.read_sql(sql_query, url)    

def get_csv_export_url(g_sheet_url):
    '''
    This function will
    - take in a string that is a url of a google sheet
      of the form "https://docs.google.com ... /edit#gid=12345..."
    - return a string that can be used with pd.read_csv
    '''
    csv_url = g_sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    return csv_url

def get_titanic_data(sql_query="SELECT * FROM passengers"
                     , filename="titanic.csv"):
    """
    This function will:
    -input 2 strings: sql_query, filename 
        default query "SELECT * FROM passengers"
        default filename "titanic.csv"
    - check the current working directory for filename (csv) existence
      - return df from that filename if it exists
    - If csv doesn't exist:
      - create a df of the sql_query
      - write df to csv
      - return that df
    """
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
        print("csv file found and read")
        return df
    else:
        url = get_db_url('titanic_db')
        df = pd.read_sql(sql_query, url)
        df.to_csv(filename, index=False)
        print ("csv file not found, data read from sql query, csv created")
        return df
    
        
def get_iris_data(sql_query="SELECT * FROM species JOIN measurements USING (species_id)"
                 , filename="iris.csv"):
    """
    This function will:
    -input 2 strings: sql_query, filename 
        default query "SELECT * FROM passengers"
        default filename "iris.csv"
    - check the current directory for filename (csv) existence
      - return df from that filename if it exists
    - If csv doesn't exist:
      - create a df of the sql_query
      - write df to csv
      - return that df
    """
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
        print ("csv file found and read")
        return df
    else:
        url = get_db_url('iris_db')
        df = pd.read_sql(sql_query, url)
        df.to_csv(filename, index=False)
        print ("csv file not found, data read from sql query, csv created")
        return df
    
def get_telco_data(sql_query= """
                        SELECT  customer_id, gender, senior_citizen
                            , partner, dependents, tenure, phone_service
                            , multiple_lines, customers.internet_service_type_id
                            , internet_service_types.internet_service_type
                            , online_security, online_backup
                            , device_protection, tech_support
                            , streaming_tv, streaming_movies
                            , customers.contract_type_id
                            , contract_types.contract_type
                            , paperless_billing, customers.payment_type_id
                            , payment_types.payment_type
                            , monthly_charges, total_charges
                            , churn
                        FROM customers
                        JOIN contract_types USING (contract_type_id)
                        JOIN internet_service_types USING (internet_service_type_id)
                        JOIN payment_types USING (payment_type_id)
                    """
                    , filename="telco.csv"):
    
    """
    This function will:
    -input 2 strings: sql_query, filename 
        default query "SELECT * FROM passengers"
        default filename "telco.csv"
    - check the current directory for filename (csv) existence
      - return df from that filename if it exists
    - If csv doesn't exist:
      - create a df of the sql_query
      - write df to csv
      - return that df
    """
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
        print ("csv file found and read")
        return df
    else:
        url = get_db_url('telco_churn')
        df = pd.read_sql(sql_query, url)
        df.to_csv(filename, index=False)
        print ("csv file not found, data read from sql query, csv created")
        return df
          