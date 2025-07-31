"""
Model Building & Training Module
"""
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split data into training and testing sets

    Parameters:
    X: Features
    y: Target
    test_size (float): Proportion of test data
    random_state (int): Random seed

    Returns:
    tuple: (x_train, x_test, y_train, y_test)
    """
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    print(f"Training data shape: {x_train.shape}, {y_train.shape}")
    print(f"Testing data shape: {x_test.shape}, {y_test.shape}")
    return x_train, x_test, y_train, y_test

def create_pipeline():
    """
    Create machine learning pipeline

    Returns:
    sklearn.pipeline.Pipeline: ML pipeline
    """
    # OneHotEncoder for categorical features
    # Columns: Company(0), TypeName(1), Cpu brand(7), Gpu Brand(10), os(11)
    step1 = ColumnTransformer(transformers=[
        ('col_tnf', OneHotEncoder(sparse_output=False, drop='first'), [0, 1, 7, 10, 11])
    ], remainder='passthrough')

    # Random Forest Regressor
    step2 = RandomForestRegressor(n_estimators=100,
                                  random_state=3,
                                  max_samples=0.5,
                                  max_features=0.75,
                                  max_depth=15)

    # Create pipeline
    pipe = Pipeline([
        ('step1', step1),
        ('step2', step2)
    ])

    return pipe

def train_and_evaluate(pipe, x_train, x_test, y_train, y_test):
    """
    Train the model and evaluate performance

    Parameters:
    pipe: ML pipeline
    x_train, x_test, y_train, y_test: Train/test data

    Returns:
    tuple: (trained_pipeline, r2_score, mae)
    """
    # Train the model
    pipe.fit(x_train, y_train)

    # Make predictions
    y_pred = pipe.predict(x_test)

    # Calculate metrics
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f'R2 score: {r2:.4f}')
    print(f'MAE: {mae:.4f}')

    return pipe, r2, mae

if __name__ == "__main__":
    # Example usage
    pass
