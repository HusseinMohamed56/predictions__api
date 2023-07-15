from fastapi import APIRouter
from typing import Union
from src.services.linear_model_service import predict_value

router = APIRouter()

@router.get("/predict_value")
async def get_predict(x0: float, x1: float, x2: float):
    predicted_value = predict_value(x0, x1, x2)
    return {"predicted_value": predicted_value}
