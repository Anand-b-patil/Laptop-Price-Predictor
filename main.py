"""
Main Execution Script - Laptop Price Prediction
"""
from data_loading import load_and_explore_data
from data_cleaning import clean_basic_data
from eda import perform_eda, plot_feature_analysis
from feature_engineering import (extract_screen_features, calculate_ppi, 
                                process_cpu_features, process_memory_features,
                                process_gpu_features, process_os_features)
from outlier_processing import remove_outliers, prepare_features_target
from model_building import split_data, create_pipeline, train_and_evaluate
from model_saving import save_model_and_data

def main():
    """
    Main execution function
    """
    print("=== Laptop Price Prediction Pipeline ===")

    # 1. Data Loading & Exploration
    print("\n1. Loading and exploring data...")
    df = load_and_explore_data('laptop_data.csv')

    # 2. Basic Data Cleaning
    print("\n2. Performing basic data cleaning...")
    df = clean_basic_data(df)

    # 3. Exploratory Data Analysis
    print("\n3. Performing EDA...")
    perform_eda(df)

    # 4. Feature Engineering
    print("\n4. Engineering features...")
    df = extract_screen_features(df)
    df = calculate_ppi(df)
    df = process_cpu_features(df)
    df = process_memory_features(df)
    df = process_gpu_features(df)
    df = process_os_features(df)

    # Plot feature analysis for engineered features
    plot_feature_analysis(df, 'Touchscreen', 'Touchscreen')
    plot_feature_analysis(df, 'IPS', 'IPS Display')
    plot_feature_analysis(df, 'Cpu brand', 'CPU Brand')
    plot_feature_analysis(df, 'Gpu Breand', 'GPU Brand')
    plot_feature_analysis(df, 'os', 'Operating System')

    # 5. Outlier Removal & Target Processing
    print("\n5. Removing outliers and preparing target...")
    df = remove_outliers(df)
    X, y = prepare_features_target(df)

    # 6. Model Building & Training
    print("\n6. Building and training model...")
    x_train, x_test, y_train, y_test = split_data(X, y)
    pipe = create_pipeline()
    pipe, r2, mae = train_and_evaluate(pipe, x_train, x_test, y_train, y_test)

    # 7. Save Model
    print("\n7. Saving model and data...")
    save_model_and_data(df, pipe)

    print("\n=== Pipeline completed successfully! ===")
    print(f"Final R2 Score: {r2:.4f}")
    print(f"Final MAE: {mae:.4f}")

if __name__ == "__main__":
    main()
