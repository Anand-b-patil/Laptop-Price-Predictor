# 💻 Laptop Price Predictor

A machine learning-powered web application that predicts the price of a laptop based on its specifications such as CPU, GPU, RAM, storage, and display features.

![GitHub](https://img.shields.io/github/license/Anand-b-patil/Laptop-Price-Predictor)
![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-red.svg)
![ML](https://img.shields.io/badge/Machine%20Learning-RandomForest-green.svg)


 🚀 Demo
 ---

🔗 [Live Demo Coming Soon](#)

Or run it locally:


streamlit run app.py



🧠 Features
---

Predict laptop prices based on key specs

Trained using Random Forest Regressor

Clean, interactive Streamlit web interface

Real-time prediction and result visualization

Handles preprocessing, feature engineering, and model serialization



📊 Model Overview
---
Algorithm Used: Random Forest Regressor

Preprocessing: OneHotEncoding, ColumnTransformer

Metrics: Mean Absolute Error (MAE), Root Mean Squared Error (RMSE)

Trained On: Cleaned and processed version of a public dataset with ~1300+ laptop records



🧾 Input Features
---
💼 Brand (e.g., Dell, HP, Lenovo)

💻 Type (e.g., Ultrabook, Gaming, Netbook)

🔳 Screen Size & Resolution

👆 Touchscreen & IPS Panel

🧠 CPU Brand

🎮 GPU Brand

💾 RAM & Storage (HDD/SSD)

🧑‍💻 Operating System



📁 Project Structure
---
bash
Copy
Edit
Laptop-Price-Predictor/
│
├── app.py                  # Streamlit web app
├── predictor.pkl           # Trained Random Forest model
├── laptop_df.csv           # Cleaned dataset
├── requirements.txt        # Dependencies
├── README.md               # Project overview
├── EDA and Modeling.ipynb  # Exploratory analysis and training notebook



🛠️ Installation & Usage
---
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Anand-b-patil/Laptop-Price-Predictor.git
cd Laptop-Price-Predictor
Create virtual environment (optional):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the app:

bash
Copy
Edit
streamlit run app.py


📈 Example Prediction
---
Input:

Brand: Lenovo

Type: Ultrabook

RAM: 8 GB

CPU: Intel Core i5

GPU: Intel UHD

Storage: 256GB SSD

OS: Windows 10

Screen: 14", Full HD, Touchscreen

Predicted Price: ₹55,372.01

📷 Screenshots
---
<img src="https://raw.githubusercontent.com/Anand-b-patil/Laptop-Price-Predictor/main/assets/ui_demo.png" width="600" />


