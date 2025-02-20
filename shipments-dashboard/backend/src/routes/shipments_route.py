from fastapi import APIRouter, Depends, HTTPException
from src.services.shipment_service import fetch_route_summary
from sqlalchemy.orm import Session
from src.core.database import get_db
from src.schemas.shipment_schema import ShipmentResponse
from src.services.shipment_service import fetch_shipment
from src.schemas.shipment_schema import RouteSummaryResponse
from src.services.shipment_service import fetch_top_expensive_routes
from src.schemas.shipment_schema import TopExpensiveRoutesResponse

router = APIRouter()


@router.get("/{shipment_id}", response_model=ShipmentResponse)
def get_shipment(shipment_id: str, db: Session = Depends(get_db)):
    shipment = fetch_shipment(db, shipment_id)
    if not shipment:
        raise HTTPException(status_code=404, detail="Shipment not found")
    return shipment


@router.get("/analysis/route-summary", response_model=RouteSummaryResponse)
def get_route_summary(origin: str, destination: str, db: Session = Depends(get_db)):
    return fetch_route_summary(db, origin, destination)


@router.get("/analysis/top-expensive-routes", response_model=TopExpensiveRoutesResponse)
def get_top_expensive_routes(limit: int = 5, db: Session = Depends(get_db)):
    return fetch_top_expensive_routes(db, limit)
