"""
Outlier Removal & Target Processing Module
"""
import numpy as np
from scipy import stats

def remove_outliers(df, z_threshold=3):
    """
    Remove outliers using Z-score method

    Parameters:
    df (pandas.DataFrame): Input dataframe
    z_threshold (float): Z-score threshold for outlier detection

    Returns:
    pandas.DataFrame: Dataframe with outliers removed
    """
    z = np.abs(stats.zscore(df['Price']))
    df_clean = df[(z < z_threshold)]
    print(f"Removed {len(df) - len(df_clean)} outliers")
    return df_clean

def prepare_features_target(df):
    """
    Prepare features and target variables

    Parameters:
    df (pandas.DataFrame): Input dataframe

    Returns:
    tuple: (X, y) features and target
    """
    X = df.drop(columns=['Price'], errors='ignore')
    y = np.log(df['Price'])  # Log transformation for better model performance

    print(f"Features shape: {X.shape}")
    print(f"Target shape: {y.shape}")

    return X, y

if __name__ == "__main__":
    # Example usage
    pass
