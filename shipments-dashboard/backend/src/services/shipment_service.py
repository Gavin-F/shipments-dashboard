from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.repositories.shipment_repo import get_shipment
from src.repositories.shipment_repo import get_route_summary
from src.repositories.shipment_repo import get_top_expensive_routes
from src.schemas.shipment_schema import RouteSummaryResponse
from src.schemas.shipment_schema import TopExpensiveRoutesResponse


def fetch_shipment(db: Session, shipment_id: str):
    return get_shipment(db, shipment_id)


def fetch_route_summary(db: Session, origin: str, destination: str) -> RouteSummaryResponse:
    raw_results = get_route_summary(db, origin, destination)

    if raw_results.num_deliveries == 0:
        raise HTTPException(
            status_code=404, detail="No shipments found for this route")

    return RouteSummaryResponse(
        origin=origin,
        destination=destination,
        average_delivery_time=round(
            raw_results.avg_delivery_time, 2) if raw_results.avg_delivery_time else 0,
        total_cost=round(raw_results.total_cost,
                         2) if raw_results.total_cost else 0,
        num_deliveries=raw_results.num_deliveries or 0
    )


def fetch_top_expensive_routes(db: Session, limit: int = 5) -> TopExpensiveRoutesResponse:
    raw_results = get_top_expensive_routes(db, limit)

    formatted_data = [
        {
            "origin": row.origin,
            "destination": row.destination,
            "total_cost": round(float(row.total_cost), 2),
            "num_deliveries": row.num_deliveries
        }
        for row in raw_results
    ]

    return TopExpensiveRoutesResponse(data=formatted_data)
