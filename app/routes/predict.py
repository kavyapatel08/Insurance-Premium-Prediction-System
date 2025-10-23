from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas.user_input_schema import UserInput
from app.services.prediction_service import predict_premium_service

router = APIRouter()

@router.post("/predict")
def predict_premium(data: UserInput):
    try:
        result = predict_premium_service(data)
        return JSONResponse(status_code=200, content=result)
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
