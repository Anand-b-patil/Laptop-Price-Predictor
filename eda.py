"""
Exploratory Data Analysis Module
"""
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def perform_eda(df):
    """
    Perform comprehensive exploratory data analysis

    Parameters:
    df (pandas.DataFrame): Input dataframe
    """
    # Price distribution
    plt.figure(figsize=(10, 6))
    sns.displot(df['Price'], kde=True)
    plt.title('Price Distribution')
    plt.show()

    # Company analysis
    plt.figure(figsize=(12, 6))
    df['Company'].value_counts().plot(kind='bar')
    plt.title('Laptop Count by Company')
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.barplot(x=df['Company'], y=df['Price'])
    plt.title('Average Price by Company')
    plt.xticks(rotation=90)
    plt.show()

    # TypeName analysis
    plt.figure(figsize=(10, 6))
    df['TypeName'].value_counts().plot(kind='bar')
    plt.title('Laptop Count by Type')
    plt.xticks(rotation=45)
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.barplot(x=df['TypeName'], y=df['Price'])
    plt.title('Average Price by Type')
    plt.xticks(rotation=90)
    plt.show()

def plot_feature_analysis(df, feature_col, title_prefix=""):
    """
    Plot analysis for a specific feature

    Parameters:
    df (pandas.DataFrame): Input dataframe
    feature_col (str): Column name to analyze
    title_prefix (str): Prefix for plot titles
    """
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    df[feature_col].value_counts().plot(kind='bar')
    plt.title(f'{title_prefix} Count')
    plt.xticks(rotation=45)

    plt.subplot(1, 2, 2)
    sns.barplot(x=df[feature_col], y=df['Price'])
    plt.title(f'{title_prefix} vs Price')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Example usage
    pass
