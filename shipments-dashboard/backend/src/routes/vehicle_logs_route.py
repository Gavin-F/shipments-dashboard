from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.vehicle_log_schema import VehicleLogResponse
from src.services.vehicle_log_service import fetch_vehicle_log

router = APIRouter()


@router.get("/{log_id}", response_model=VehicleLogResponse)
def get_vehicle_log(log_id: str, db: Session = Depends(get_db)):
    vehicle_log = fetch_vehicle_log(db, log_id)
    if not vehicle_log:
        raise HTTPException(status_code=404, detail="Vehicle log not found")
    return vehicle_log
