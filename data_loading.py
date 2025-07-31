"""
Data Loading & Initial Exploration Module
"""
import numpy as np 
import pandas as pd

def load_and_explore_data(file_path='laptop_data.csv'):
    """
    Load the laptop dataset and perform initial exploration

    Parameters:
    file_path (str): Path to the CSV file

    Returns:
    pandas.DataFrame: Loaded dataset
    """
    # Load data
    df = pd.read_csv(file_path)

    # Display basic information
    print("Dataset shape:", df.shape)
    print("\nDataset info:")
    print(df.info())
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nFirst 5 rows:")
    print(df.head())
    print("\nRandom sample:")
    print(df.sample(10))

    return df

if __name__ == "__main__":
    df = load_and_explore_data()
