from fastapi import APIRouter
from src.controllers.predictions_controller import router as predictions_router

router = APIRouter()

router.include_router(predictions_router)