## IMPORTS

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

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
    dummies_df = pd.get_dummies(df[['sex','embarked']], drop_first=True)
    new_df = pd.concat([df, dummies_df], axis=1)
    return new_df

def prep_telco(df):
    """
    This function will
    - take in the telco_churn dataframe
    - clean it up (remove useless columns, rename some columns, and
      add encoded columns for categorical variables (columns) 
    - returns cleaned up (prepared) dataframe
    """
    df = df.drop(columns=['customer_id', 'internet_service_type_id', 'contract_type_id', 'payment_type_id'])
    df.total_charges = df.total_charges.str.replace(' ', '0').astype(float)
    df['gender_encoded'] = df.gender.map({'Male': 0, 'Female': 1})
    df['partner_encoded'] = df.partner.map({'No': 0, 'Yes': 1})
    df['dependendents_encoded'] = df.dependents.map({'No': 0, 'Yes': 1})
    df['phone_service_encoded'] = df.phone_service.map({'No': 0, 'Yes': 1})
    df['paperless_billing_encoded'] = df.paperless_billing.map({'No': 0, 'Yes': 1})
    df['churn_encoded'] = df.churn.map({'No': 0, 'Yes': 1})
    dummy_df = pd.get_dummies(df[['multiple_lines', 'internet_service_type', 'online_security', 'online_backup'
                               ,'device_protection', 'tech_support', 'streaming_tv', 'streaming_movies'
                               ,'contract_type', 'payment_type']], drop_first=True)
    df = pd.concat([df, dummy_df], axis=1)
    return df

def split_function(df, target_var):
    """
    This function will
    - take in a dataframe (df) and a string (target_var)
    - split the dataframe into 3 data frames: train (60%), validate (20%), test (20%)
    -   while stratifying on the target_var
    - And finally return the three dataframes in order: train, validate, test
    """
    train, test = train_test_split(df, random_state=42, test_size=.2, stratify=df[target_var])
    
    train, validate = train_test_split(train, random_state=42, test_size=.25, stratify=train[target_var])

    print(f'Prepared df: {df.shape}')
    print()
    print(f'Train: {train.shape}')
    print(f'Validate: {validate.shape}')
    print(f'Test: {test.shape}')
    
    return train, validate, test