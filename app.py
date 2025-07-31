import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))
# Streamlit page config
st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="centered")

# 🎨 Custom CSS with background image from the web
st.markdown("""
    <style>
        body {
            margin: 0;
        }
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=1600&q=80");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            color: white;
        }
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #ffffff;
            text-align: center;
            text-shadow: 2px 2px 4px #000000;
            margin-bottom: 30px;
        }
        
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">💻 Laptop Price Predictor</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    company = st.selectbox('Company', df['Company'].unique())
    ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    weight = st.number_input("Weight (in KG)", min_value=0.0, max_value=10.0, step=0.1)
    ips = st.selectbox('IPS', ['No', 'Yes'])
    resolution = st.selectbox('Screen Resolution', [
        '1920x1080','1366x768','1600x900','3840x2160','3200x1800',
        '2880x1800','2560x1600','2560x1440','2304x1440'
    ])
    hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
    gpu = st.selectbox('GPU', df['Gpu Breand'].unique())

with col2:
    type = st.selectbox('Type', df['TypeName'].unique())
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
    screen_size = st.number_input('Screen Size (inches)', min_value=10.0, max_value=20.0, step=0.1)
    cpu = st.selectbox('CPU Brand', df['Cpu brand'].unique())
    ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
    os = st.selectbox('Operating System', df['os'].unique())


if st.button('Predict Price'):
    ppi = None
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0
    if ips == 'Yes':
        ips = 1
    else:
        ips = 0
    
    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    if screen_size != 0:
        ppi = ((X_res)**2 + (Y_res)**2)**0.5 / screen_size
    else:
        ppi = 0  
    query = np.array([company, type, ram, weight, touchscreen, ips,ppi, cpu, hdd, ssd, gpu, os])
    query = query.reshape(1, 12)
    price = pipe.predict(query)[0]
    price = np.exp(price)  
    st.title(f"Predicted Price: {round(price, 2)}")