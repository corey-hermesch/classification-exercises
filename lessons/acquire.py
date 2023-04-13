### IMPORTS 

from env import host, user, password

### FUNCTIONS 

def get_db_url(db_name, user=user, host=host, password=password):
    '''
    get_db_url accepts a database name, username, hostname, password 
    and returns a url connection string formatted to work with codeup's 
    sql database.
    Default values from env.py are provided for user, host, and password.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db_name}'

def new_titanic_data(sql_query="SELECT * FROM passengers"):
    """
    This function will:
    - take in a sql query
    - create a connection url to mySQL database
    -- default query is select * from passengers
    - return a df of the given query
    """
    url = get_db_url('titanic_db')
    return pd.read_sql(sql_query, url)