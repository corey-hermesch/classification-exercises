## IMPORTS

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

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
    - clean it up 
        -- remove useless columns passenger_id, class, embark_town, deck, age
        -- tack on dummies columns for 'pclass', 'sex', 'embarked'
    - returns cleaned up dataframe
    """
    df = df.drop(columns=['passenger_id', 'class', 'embark_town', 'deck', 'age'])
    df.embarked = df.embarked.fillna('S') #filling with most common value
    dummies_df = pd.get_dummies(df[['sex','embarked']], drop_first=True)
    new_df = pd.concat([df, dummies_df], axis=1)
    return new_df

# defining a second prepare function to keep age
def prep_titanic_2(df):
    """
    This function will
    - take in the titanic dataframe
    - clean it up 
        -- remove useless columns passenger_id, class, embark_town, deck
        -- NOTE: keeping the age column; fixing age nulls NOT done here (must use impute_feature)
        -- tack on dummies columns for 'pclass', 'sex', 'embarked'
    - returns cleaned up dataframe
    """
    df = df.drop(columns=['passenger_id', 'class', 'embark_town', 'deck'])
    df.embarked = df.embarked.fillna('S') # filling with most common value
    dummies_df = pd.get_dummies(df[['sex','embarked']], drop_first=True)
    new_df = pd.concat([df, dummies_df], axis=1)
    return new_df

def prep_titanic_for_model(df):
    """
    - take in titanic dataframe from prep_titanic function
    - remove non-encoded columns
    - return df with only numeric columns ready for modeling
    """
    drop_cols = ['sex', 'embarked']
    df = df.drop(columns=drop_cols)
    return df

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

def prep_telco_for_model(df):
    """
    This function will
    - take in telco dataframe from prep_telco function
    - remove non-encoded columns
    - remove unneccessary columns (repeated columns)
    - return df with only numeric columns ready for modeling
    """
    # getting rid of non-numeric columns to start the modeling phase
    drop_cols = ['gender', 'partner', 'dependents', 'phone_service', 'multiple_lines', 'internet_service_type',
                'online_security', 'online_backup', 'device_protection', 'tech_support', 'streaming_tv', 
                'streaming_movies', 'contract_type', 'paperless_billing', 'payment_type', 'churn']
    # make "encoded" df without only the encoded columns for machine learning
    e_df = df.drop(columns=drop_cols)
    
    # phone_service was included in multiple_lines, so drop that phone_service_encoded, too
    e_df = e_df.drop(columns=['phone_service_encoded'])
    
    # Since internet_service_type_None is repeated in several columns, I can delete them. 
    # A possibly better way is to encode them differently so the column names make more sense. maybe later
    repeated_cols = ['online_security_No internet service', 'online_backup_No internet service',
                    'device_protection_No internet service', 'tech_support_No internet service',
                    'streaming_tv_No internet service', 'streaming_movies_No internet service']
    e_df = e_df.drop(columns=repeated_cols)
    
    return e_df

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

def impute_feature(train, validate, test, feature='age', strat='median'):
    """
    This function will
    - take in train, validate, test dfs
    - take in a string which is the column name that has nan values
        -- default is 'age' (built off titanic df)
    - take in a string which is the strategy to impute values
        -- default is 'median'
    - impute nan values in the feature(age) column and fill with new values
    - return train, validate, test with imputed values
    """
    imputer = SimpleImputer(missing_values=np.nan, strategy=strat)
    imputer = imputer.fit(train[[feature]])
    train[[feature]] = imputer.transform(train[[feature]])
    validate[[feature]] = imputer.transform(validate[[feature]])
    test[[feature]] = imputer.transform(test[[feature]])
    
    return train, validate, test