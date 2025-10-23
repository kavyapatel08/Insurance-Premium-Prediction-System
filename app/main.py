from fastapi import FastAPI
from app.routes import predict

app = FastAPI(title="Insurance Premium Prediction API")

# Include routes
app.include_router(predict.router)

@app.get("/")
def home():
    return {"message": "Insurance premium prediction API"}

@app.get("/health")
def health_check():
    return {"status": "OK"}
