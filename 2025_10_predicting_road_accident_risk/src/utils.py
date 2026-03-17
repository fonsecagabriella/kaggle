import numpy as np
import pandas as pd


### TRANSFORMATION UTILITIES ###
def vectorize_ready(X, num_cols, cat_cols):
    # convert all categorical-like features to string
    for col in cat_cols:
        X[col] = X[col].astype(str)

    # drop target variable if present
    if 'accident_risk' in X.columns:
        X = X.drop(columns=['accident_risk'])

    # drop index if present
    if 'index' in X.columns:
        X = X.drop(columns=['index'])


    X_train_dict = X[num_cols + cat_cols].to_dict(orient='records')

    return X_train_dict

def make_matrices(df, dv=None, fit=False):
    """
    Build X matrix from df using your existing vectorize_ready().
    If fit=True, fit a new DictVectorizer and return it; otherwise reuse dv.
    """
    num_cols = ['curvature']
    cat_cols = ['speed_limit', 'lighting', 'num_reported_accidents', 'weather']

    X_dict = vectorize_ready(df, num_cols=num_cols, cat_cols=cat_cols)

    if fit:
        dv = DictVectorizer(sparse=False)
        X = dv.fit_transform(X_dict)
        return X, dv
    else:
        X = dv.transform(X_dict)
        return X


#### EVALUATION METRICS ####




#### KAGGLE SUBMISSION FUNCTIONALITY ####

# define function to create file to submit to kaggle
def create_submission_file(test_data, y_pred, filename='submission.csv'):
    submission = pd.DataFrame({
        'id': test_data['id'],
        'accident_risk': np.round(y_pred, 3)
    })
    submission.to_csv(filename, index=False)
    print(f"Submission file '{filename}' created.")

def predict_and_create_submission(num_cols, cat_cols, model, dv, filename='submission.csv'):
    #X_test = test_data.drop(columns=['accident_risk'])
    X_test = pd.read_csv('data/test.csv')
    test_data = X_test.copy()
    
    X_test_dict = vectorize_ready(X_test, num_cols, cat_cols)
    X_test = dv.transform(X_test_dict)
    y_test_pred = model.predict(X_test)
    create_submission_file(test_data, y_test_pred, filename)
