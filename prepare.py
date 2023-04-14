## IMPORTS

import numpy as np
import pandas as pd


## FUNCTIONS

def prep_iris(df):
    """
    This function will
    - take in the iris_df
    - clean it up (remove useless columns, rename a column, and tack on some dummies columns for 'species')
    - returns cleaned up dataframe
    """
    df = df.drop(columns=['species_id', 'measurement_id'])
    df = df.rename(columns={'species_name': 'species'})
    dummy_df = pd.get_dummies(df[['species']], drop_first=True)
    new_df = pd.concat([df, dummy_df], axis=1)
    return new_df

def prep_titanic(df):
    """
    This function will
    - take in the titanic dataframe
    - clean it up (remove useless columns and tack on some dummies columns for 'pclass', 'sex', 'embarked')
    - returns cleaned up dataframe
    """
    df = df.drop(columns=['passenger_id', 'class', 'embark_town', 'deck', 'age'])
    dummies_df = pd.get_dummies(df[['pclass', 'sex','embarked']], drop_first=True)
    new_df = pd.concat([df, dummies_df], axis=1)
    return new_df