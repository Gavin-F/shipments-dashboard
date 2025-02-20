from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.vehicle_schema import VehicleResponse
from src.services.vehicle_service import fetch_vehicle
from src.services.vehicle_service import fetch_vehicle_efficiency
from src.schemas.vehicle_schema import VehicleEfficiencyListResponse

router = APIRouter()


@router.get("/{vehicle_id}", response_model=VehicleResponse)
def get_vehicle(vehicle_id: str, db: Session = Depends(get_db)):
    vehicle = fetch_vehicle(db, vehicle_id)
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle


@router.get("/analysis/efficiency", response_model=VehicleEfficiencyListResponse)
def vehicle_efficiency(
    db: Session = Depends(get_db),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0)
):
    return fetch_vehicle_efficiency(db, limit, offset)
