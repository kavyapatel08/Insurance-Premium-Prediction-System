import pickle

def load_model():
    with open("Model/GB_regressor.pkl", "rb") as f:
        model = pickle.load(f)
    return model
