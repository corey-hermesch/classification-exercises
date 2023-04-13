### IMPORTS 

from env import host, user, password
import os

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
    
def get_titanic_data(sql_query="SELECT * FROM passengers"
                     , directory='/Users/slick/codeup-data-science/classification-exercises/'
                     , filename="titanic.csv"):
    """
    This function will:
    -input 3 strings: sql_query, directory, filename 
      - default query "SELECT * FROM passengers"
      - default directory is "Users/slick/codeup-data-science/classification-exercises/""
      - default filename "titanic.csv"
    - check the directory for filename (csv) existence
      - return df from that filename if it exists
    - If csv doesn't exist:
      - create a df of the sql_query
      - write df to csv
      - return that df
    """
    if os.path.exists(directory + filename):
        df = pd.read_csv(filename)
        df = df.drop(columns=['Unnamed: 0'])
        return df
    else:
        url = get_db_url('titanic_db')
        df = pd.read_sql(sql_query, url)
        df.to_csv(filename)
        return df
    
def get_iris_data(sql_query="SELECT * FROM species JOIN measurements USING (species_id)"
                 , directory='/Users/slick/codeup-data-science/classification-exercises/'
                 , filename="iris.csv"):
    """
    This function will:
    -input 3 strings: sql_query, directory, filename 
      - default query "SELECT * FROM species JOIN measurements USING (species_id)"
      - default directory is "Users/slick/codeup-data-science/classification-exercises/""
      - default filename "iris.csv"
    - check the directory for filename (csv) existence
      - return df from that filename if it exists
    - If csv doesn't exist:
      - create a df of the sql_query
      - write df to csv
      - return that df
    """
    if os.path.exists(directory + filename):
        df = pd.read_csv(filename)
        df = df.drop(columns=['Unnamed: 0'])
        return df
    else:
        url = get_db_url('iris_db')
        df = pd.read_sql(sql_query, url)
        df.to_csv(filename)
        return df
    
def get_telco_data(sql_query= """
                        SELECT  customer_id, gender, senior_citizen
                            , partner, dependents, tenure, phone_service
                            , multiple_lines, customers.internet_service_type_id
                            , internet_service_types.internet_service_type
                            , online_security, online_backup
                            , device_protection, tech_support
                            , streaming_tv, customers.contract_type_id
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
                    , directory='/Users/slick/codeup-data-science/classification-exercises/'
                    , filename="telco.csv"):
    
    """
    This function will:
    -input 3 strings: sql_query, directory, filename 
      - default query "SELECT * FROM customers JOIN'd with contract_types, internet_service_types, payment_types"
      - default directory is "Users/slick/codeup-data-science/classification-exercises/""
      - default filename "telco.csv"
    - check the directory for filename (csv) existence
      - return df from that filename if it exists
    - If csv doesn't exist:
      - create a df of the sql_query
      - write df to csv
      - return that df
    """
    if os.path.exists(directory + filename):
        df = pd.read_csv(filename)
        df = df.drop(columns=['Unnamed: 0'])
        return df
    else:
        url = get_db_url('telco_churn')
        df = pd.read_sql(sql_query, url)
        df.to_csv(filename)
        return df
