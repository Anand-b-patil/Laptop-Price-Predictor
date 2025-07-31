"""
Feature Engineering Module
"""
import pandas as pd
import numpy as np

def extract_screen_features(df):
    """
    Extract features from ScreenResolution column

    Parameters:
    df (pandas.DataFrame): Input dataframe

    Returns:
    pandas.DataFrame: Dataframe with new screen features
    """
    # Extract Touchscreen feature
    df['Touchscreen'] = df['ScreenResolution'].apply(lambda x: 1 if 'Touchscreen' in x else 0)

    # Extract IPS feature
    df['IPS'] = df['ScreenResolution'].apply(lambda x: 1 if 'IPS' in x else 0)

    # Extract resolution
    new = df['ScreenResolution'].str.split('x', n=1, expand=True)
    df['X_res'] = new[0]
    df['Y_res'] = new[1]

    # Clean resolution data
    df['X_res'] = df['X_res'].str.replace(',','').str.findall(r'(\d+\.?\d+)').apply(lambda x: x[0] if x else '0')
    df['X_res'] = df['X_res'].astype('Int32')
    df['Y_res'] = df['Y_res'].astype('Int32')

    return df

def calculate_ppi(df):
    """
    Calculate pixels per inch (PPI)

    Parameters:
    df (pandas.DataFrame): Input dataframe with X_res, Y_res, and Inches columns

    Returns:
    pandas.DataFrame: Dataframe with PPI column
    """
    df['ppi'] = ((((df['X_res']**2) + (df['Y_res']**2))**0.5) / df['Inches']).astype('float')

    # Drop intermediate columns
    df = df.drop(columns=['ScreenResolution', 'X_res', 'Y_res', 'Inches'], errors='ignore')

    return df

def process_cpu_features(df):
    """
    Process CPU information and extract CPU brand

    Parameters:
    df (pandas.DataFrame): Input dataframe

    Returns:
    pandas.DataFrame: Dataframe with processed CPU features
    """
    # Extract CPU name
    df['Cpu Name'] = df['Cpu'].apply(lambda x: " ".join(x.split()[0:3]))

    def fetch_processor(text):
        if text == 'Intel Core i7' or text == 'Intel Core i5' or text == 'Intel Core i3':
            return text 
        else:
            if text.startswith('Intel'):
                return 'Other Intel Processor'
            else:
                return 'AMD Processor'

    # Extract CPU brand
    df['Cpu brand'] = df['Cpu Name'].apply(fetch_processor)

    # Drop original CPU columns
    df = df.drop(columns=['Cpu', 'Cpu Name'], errors='ignore')

    return df

def process_memory_features(df):
    """
    Process Memory column and extract storage features

    Parameters:
    df (pandas.DataFrame): Input dataframe

    Returns:
    pandas.DataFrame: Dataframe with processed memory features
    """
    # Clean memory data
    df['Memory'] = df['Memory'].astype(str).replace(r'\.0', '', regex=True)
    df["Memory"] = df["Memory"].str.replace('GB', '')
    df["Memory"] = df["Memory"].str.replace('TB', '000')
    new = df["Memory"].str.split("+", n=1, expand=True)

    df["first"] = new[0]
    df["first"] = df["first"].str.strip()
    df["second"] = new[1]

    # Extract storage types for layer 1
    df["Layer1HDD"] = df["first"].apply(lambda x: 1 if "HDD" in x else 0)
    df["Layer1SSD"] = df["first"].apply(lambda x: 1 if "SSD" in x else 0)
    df["Layer1Hybrid"] = df["first"].apply(lambda x: 1 if "Hybrid" in x else 0)
    df["Layer1Flash_Storage"] = df["first"].apply(lambda x: 1 if "Flash Storage" in x else 0)

    df['first'] = df['first'].str.replace(r'\D', '', regex=True)
    df["second"] = df["second"].fillna("0")

    # Extract storage types for layer 2
    df["Layer2HDD"] = df["second"].apply(lambda x: 1 if "HDD" in x else 0)
    df["Layer2SSD"] = df["second"].apply(lambda x: 1 if "SSD" in x else 0)
    df["Layer2Hybrid"] = df["second"].apply(lambda x: 1 if "Hybrid" in x else 0)
    df["Layer2Flash_Storage"] = df["second"].apply(lambda x: 1 if "Flash Storage" in x else 0)

    df['second'] = df['second'].str.replace(r'\D', '', regex=True)

    df["first"] = df["first"].astype(int)
    df["second"] = df["second"].astype(int)

    # Calculate total storage by type
    df["HDD"] = (df["first"] * df["Layer1HDD"] + df["second"] * df["Layer2HDD"])
    df["SSD"] = (df["first"] * df["Layer1SSD"] + df["second"] * df["Layer2SSD"])
    df["Hybrid"] = (df["first"] * df["Layer1Hybrid"] + df["second"] * df["Layer2Hybrid"])
    df["Flash_Storage"] = (df["first"] * df["Layer1Flash_Storage"] + df["second"] * df["Layer2Flash_Storage"])

    # Clean up intermediate columns
    df = df.drop(columns=['first', 'second', 'Layer1HDD', 'Layer1SSD', 'Layer1Hybrid',
                         'Layer1Flash_Storage', 'Layer2HDD', 'Layer2SSD', 'Layer2Hybrid',
                         'Layer2Flash_Storage', 'Memory'], errors='ignore')

    # Remove less correlated features
    df = df.drop(columns=['Hybrid', 'Flash_Storage'], errors='ignore')

    return df

def process_gpu_features(df):
    """
    Process GPU information

    Parameters:
    df (pandas.DataFrame): Input dataframe

    Returns:
    pandas.DataFrame: Dataframe with processed GPU features
    """
    # Extract GPU brand
    df['Gpu Breand'] = df['Gpu'].apply(lambda x: x.split()[0])

    # Remove ARM GPU entries (rare cases)
    df = df[df['Gpu Breand'] != 'ARM']

    # Drop original GPU column
    df = df.drop(columns=['Gpu'], errors='ignore')

    return df

def process_os_features(df):
    """
    Process Operating System information

    Parameters:
    df (pandas.DataFrame): Input dataframe

    Returns:
    pandas.DataFrame: Dataframe with processed OS features
    """
    def cat_os(inp):
        if inp == 'Windows 10' or inp == 'Windows 7' or inp == 'Windows 10 S':
            return 'Windows'
        elif inp == 'macOS' or inp == 'Mac OS X':
            return 'MacOS'
        else:
            return 'Other OS/No OS/Linux'

    # Categorize OS
    df['os'] = df['OpSys'].apply(cat_os)

    # Drop original OS column
    df = df.drop(columns=['OpSys'], errors='ignore')

    return df

if __name__ == "__main__":
    # Example usage
    pass
