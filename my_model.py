import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

# defining a function to get metrics for a set of predictions vs a train series
def get_tree_metrics(y_train, y_pred):
    """
    This functiion will
    - take in a y_train series and a y_pred (result from a classifier.predict)
    - returns nothing
    - prints out confusion matrix with row/column labeled with actual/predicted and the unique values in y_train
    -- (could add in a labels variable to make that prettier (NOT THERE NOW))
    """
    print("CONFUSION MATRIX")
    print(pd.DataFrame(
          confusion_matrix(y_train, y_pred),
          index=[label.astype(str) + '_actual' for label in sorted(y_train.unique())],
          columns=[label.astype(str) + '_predicted' for label in sorted(y_train.unique())])
        )
    print()
    print("Classification Report:")
    print(classification_report(y_train, y_pred))