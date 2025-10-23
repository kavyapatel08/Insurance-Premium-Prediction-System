# 🖥️ Frontend - Insurance Premium Prediction App

This folder contains the **Streamlit frontend** for the Insurance Premium Prediction System.

## 📂 Folder Structure
frontend/
├─ app_ui.py # Main Streamlit app
├─ assets/
│ └─ frontend.png # App screenshot
└─ Dockerfile # Frontend Dockerfile

bash
Copy code

## 🚀 How to Run
- Install dependencies:  
- pip install -r ../requirements.txt
- Run the app:

Copy code
- streamlit run app_ui.py
📌 Notes
- The app communicates with the FastAPI backend (if used).

assets/ contains screenshots or static files for the frontend.

- Dockerfile can be used to containerize the frontend separately.
