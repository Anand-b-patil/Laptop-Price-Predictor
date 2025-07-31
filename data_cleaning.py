
import pandas as pd

def clean_basic_data(df):

    # Remove unnecessary columns
    df = df.drop(columns=['Unnamed: 0'], errors='ignore')

    # Clean Ram column
    df['Ram'] = df['Ram'].str.replace('GB', '')
    df['Ram'] = df['Ram'].astype('Int32')

    # Clean Weight column
    df['Weight'] = df['Weight'].str.replace('kg', '')
    df['Weight'] = df['Weight'].astype('float32')

    # Remove any duplicate ram columns
    df = df.drop(columns=['ram'], errors='ignore')

    return df

if __name__ == "__main__":
    # Example usage
    pass
