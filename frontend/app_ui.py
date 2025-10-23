import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

# ------------------- PAGE CONFIG -------------------
st.set_page_config(
    page_title="💰 Insurance Premium Predictor",
    page_icon="💵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ------------------- CUSTOM CSS -------------------
st.markdown("""
    <style>
        body {
            background-color: #F5F7FA;
            color: #333333;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            padding: 10px 25px;
            font-size: 18px;
            font-weight: 600;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
        .result-card {
            background-color: #E8F5E9;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
            margin-top: 20px;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------- SIDEBAR -------------------
st.sidebar.title("📂 Navigation")
menu = st.sidebar.radio("Go to:", ["🏠 Prediction", "ℹ️ About App", "🧠 Model Info"])

# ------------------- API CALL FUNCTION -------------------
@st.cache_data(ttl=300)  # Cache results for 5 minutes to reduce requests
def get_premium_prediction(api_url, input_data):
    """Send input data to backend API and return prediction"""
    try:
        response = requests.post(api_url, json=input_data, timeout=40)
        if response.status_code == 200:
            return response.json(), None
        else:
            return None, f"⚠️ Error {response.status_code}: {response.text}"
    except requests.exceptions.Timeout:
        return None, "⏰ The request timed out. Please try again."
    except requests.exceptions.ConnectionError:
        return None, "❌ Could not connect to backend API. Please check the server URL."
    except Exception as e:
        return None, f"Unexpected error: {e}"

# ------------------- PREDICTION PAGE -------------------
if menu == "🏠 Prediction":
    st.title("💰 Insurance Premium Prediction App")
    st.markdown("### Fill in your details below to predict your insurance premium.")
    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("🎂 Age", min_value=1, max_value=119, value=30)
        sex = st.selectbox("👫 Gender", options=["Male", "Female"])
        children = st.number_input("👶 Number of Children", min_value=0, max_value=10, value=0)

    with col2:
        height = st.number_input("📏 Height (m)", min_value=0.5, max_value=2.5, value=1.70)
        weight = st.number_input("⚖️ Weight (kg)", min_value=1.0, value=65.0)
        smoker = st.radio("🚬 Are you a smoker?", options=["Yes", "No"])
        region = st.selectbox("🌍 Region", options=["southwest", "southeast", "northwest", "northeast"])

    bmi = round(weight / (height ** 2), 2)

    if st.button("🔮 Predict Premium"):
        API_URL = "https://insurance-premium-prediction-api-2.onrender.com/predict"

        input_data = {
            "age": age,
            "sex": sex.lower(),
            "height": height,
            "weight": weight,
            "children": children,
            "smoker": smoker.lower(),
            "region": region
        }

        with st.spinner("🔎 Predicting your premium... Please wait."):
            result, error = get_premium_prediction(API_URL, input_data)

        if error:
            st.error(error)
        else:
            predicted_premium = result.get("predicted_premium")
            calculated_bmi = result.get("calculated_bmi")

            st.markdown(f"""
                <div class="result-card">
                    <h3>✅ Prediction Successful!</h3>
                    <h3>Predicted Insurance Premium: 
                        <span style="color:#2E8B57;">{predicted_premium}</span>
                    </h3>
                    <p>BMI Used in Prediction: <b>{calculated_bmi}</b></p>
                </div>
            """, unsafe_allow_html=True)

# ------------------- ABOUT APP -------------------
elif menu == "ℹ️ About App":
    st.title("ℹ️ About This App")
    st.markdown("""
        This app predicts **insurance premiums** based on user details such as age, BMI, 
        smoking habits, and region.  
        It’s powered by a **FastAPI backend** and an **ML model** trained on the 
        [Insurance Premium Prediction dataset](https://www.kaggle.com/datasets/noordeen/insurance-premium-prediction).

        **Tech Stack:**
        - 🧠 Machine Learning (Scikit-learn, Gradient Boosting)
        - ⚡ FastAPI for backend API
        - 🖥️ Streamlit for frontend UI
        - 🐳 Docker for containerization
        - ☁️ Render for deployment
    """)

# ------------------- MODEL INFO -------------------
elif menu == "🧠 Model Info":
    st.title("🧠 Model Information")
    st.markdown("""
        The ML model was trained on:
        - Age  
        - Sex  
        - BMI (calculated from height & weight)  
        - Children  
        - Smoker  
        - Region  

        **Preprocessing steps:**
        - Standard Scaling for numeric features  
        - One-Hot Encoding for categorical features  

        **Algorithms tested:**
        - Linear Regression  
        - Decision Tree Regressor  
        - Random Forest Regressor  
        - XGBoost Regressor  
        - Gradient Boosting (best model with ~87% accuracy)

        📦 Full code: [GitHub Repo](https://github.com/kavyapatel08/Insurance-Premium-Prediction-System)
    """)
