# Laptop Price Prediction - Modular Code Structure

## Overview
The original Jupyter notebook has been split into 8 modular Python files for better organization, maintainability, and reusability. Each module handles a specific aspect of the machine learning pipeline.

## File Structure

### 1. **data_loading.py**
**Purpose**: Data loading and initial exploration
- `load_and_explore_data()`: Loads CSV file and displays basic dataset information
- Shows dataset shape, info, missing values, and sample data

### 2. **data_cleaning.py** 
**Purpose**: Basic data cleaning and preprocessing
- `clean_basic_data()`: Removes unnecessary columns, cleans Ram and Weight columns
- Converts data types to appropriate formats

### 3. **eda.py**
**Purpose**: Exploratory Data Analysis and visualization
- `perform_eda()`: Creates comprehensive visualizations for price distribution, company analysis, laptop types
- `plot_feature_analysis()`: Generic function to analyze any feature vs price

### 4. **feature_engineering.py**
**Purpose**: Advanced feature creation and transformation
- `extract_screen_features()`: Extracts Touchscreen, IPS, and resolution features
- `calculate_ppi()`: Calculates pixels per inch from screen resolution
- `process_cpu_features()`: Processes CPU information and creates CPU brand categories
- `process_memory_features()`: Complex memory processing to extract HDD/SSD storage info
- `process_gpu_features()`: Extracts GPU brand information
- `process_os_features()`: Categorizes operating systems

### 5. **outlier_processing.py**
**Purpose**: Outlier removal and target variable preparation
- `remove_outliers()`: Uses Z-score method to remove price outliers
- `prepare_features_target()`: Separates features and applies log transformation to target

### 6. **model_building.py**
**Purpose**: Machine learning model creation and training
- `split_data()`: Splits data into train/test sets
- `create_pipeline()`: Creates sklearn pipeline with OneHotEncoder and RandomForest
- `train_and_evaluate()`: Trains model and calculates performance metrics

### 7. **model_saving.py**
**Purpose**: Model persistence functionality
- `save_model_and_data()`: Saves trained model and preprocessed data using pickle
- `load_model_and_data()`: Loads saved model and data for future use

### 8. **main.py**
**Purpose**: Main execution script that orchestrates the entire pipeline
- Imports all modules and executes the complete workflow
- Provides progress updates and final performance metrics

## Usage Instructions

### Option 1: Run Complete Pipeline
```bash
python main.py
```
This executes the entire pipeline from data loading to model saving.

### Option 2: Use Individual Modules
```python
from data_loading import load_and_explore_data
from feature_engineering import extract_screen_features

# Load data
df = load_and_explore_data('laptop_data.csv')

# Apply specific feature engineering
df = extract_screen_features(df)
```

### Option 3: Custom Pipeline
```python
# Import required modules
from data_loading import load_and_explore_data
from data_cleaning import clean_basic_data
from feature_engineering import *
from model_building import *

# Create custom workflow
df = load_and_explore_data('laptop_data.csv')
df = clean_basic_data(df)
df = extract_screen_features(df)
# ... continue with other steps
```

## Key Improvements from Original Code

1. **Modularity**: Each function has a single responsibility
2. **Reusability**: Functions can be imported and used independently
3. **Documentation**: Each function includes docstrings explaining parameters and returns
4. **Error Handling**: Proper error handling with `errors='ignore'` where appropriate
5. **Maintainability**: Easy to modify individual components without affecting others
6. **Testing**: Individual functions can be tested separately

## Pipeline Flow

```
Data Loading → Data Cleaning → EDA → Feature Engineering → 
Outlier Removal → Model Building → Model Training → Model Saving
```

## Current Model Performance
- **R2 Score**: 0.89
- **MAE**: 0.161
- **Algorithm**: Random Forest Regressor
- **Features**: 12 engineered features after preprocessing

## Next Steps for Improvement
Based on the previous analysis, consider implementing:
1. Hyperparameter tuning (GridSearchCV/RandomizedSearchCV)
2. Advanced algorithms (XGBoost, LightGBM)
3. Ensemble methods (Stacking)
4. Additional feature engineering
5. Advanced outlier detection methods

## Dependencies
- pandas
- numpy
- scikit-learn
- seaborn
- matplotlib
- scipy

## File Requirements
- Input: `laptop_data.csv` (original dataset)
- Output: `df.pkl` (preprocessed data), `pipe.pkl` (trained model)