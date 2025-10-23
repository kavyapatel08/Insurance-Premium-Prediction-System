import pandas as pd
from app.core.model_loader import load_model

model = load_model()

def predict_premium_service(data):
    input_df = pd.DataFrame([{
        "age": data.age,
        "sex": data.sex,
        "bmi": data.bmi,
        "children": data.children,
        "smoker": data.smoker,
        "region": data.region
    }])

    prediction = model.predict(input_df)[0]
    return {
        "predicted_premium": round(float(prediction), 2),
        "calculated_bmi": data.bmi
    }
