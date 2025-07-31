"""
Model Saving & Loading Module
"""
import pickle

def save_model_and_data(df, pipe, df_filename='df.pkl', model_filename='pipe.pkl'):
    """
    Save preprocessed data and trained model

    Parameters:
    df: Preprocessed dataframe
    pipe: Trained pipeline
    df_filename (str): Filename for dataframe
    model_filename (str): Filename for model
    """
    # Save preprocessed data
    with open(df_filename, 'wb') as f:
        pickle.dump(df, f)

    # Save trained model
    with open(model_filename, 'wb') as f:
        pickle.dump(pipe, f)

    print(f"Model saved as {model_filename}")
    print(f"Data saved as {df_filename}")

def load_model_and_data(df_filename='df.pkl', model_filename='pipe.pkl'):
    """
    Load preprocessed data and trained model

    Parameters:
    df_filename (str): Filename for dataframe
    model_filename (str): Filename for model

    Returns:
    tuple: (dataframe, pipeline)
    """
    # Load preprocessed data
    with open(df_filename, 'rb') as f:
        df = pickle.load(f)

    # Load trained model
    with open(model_filename, 'rb') as f:
        pipe = pickle.load(f)

    print(f"Model loaded from {model_filename}")
    print(f"Data loaded from {df_filename}")

    return df, pipe

if __name__ == "__main__":
    # Example usage
    pass
