from sqlalchemy.orm import Session
from src.repositories.vehicle_repo import get_vehicle
from src.repositories.vehicle_repo import get_vehicle_efficiency
from src.schemas.vehicle_schema import VehicleEfficiencyListResponse, VehicleEfficiencyResponse


def fetch_vehicle(db: Session, vehicle_id: str):
    return get_vehicle(db, vehicle_id)


def fetch_vehicle_efficiency(db: Session, limit: int, offset: int) -> VehicleEfficiencyListResponse:
    raw_results = get_vehicle_efficiency(db, limit, offset)

    formatted_data = [
        VehicleEfficiencyResponse(
            vehicle_id=row.vehicle_id,
            total_mileage=round(float(row.total_mileage),
                                2) if row.total_mileage else 0,
            total_fuel_used=round(float(row.total_fuel_used),
                                  2) if row.total_fuel_used else 0,
            fuel_efficiency=round(
                float(row.total_mileage / row.total_fuel_used), 2) if row.total_fuel_used else 0
        )
        for row in raw_results
    ]

    return VehicleEfficiencyListResponse(data=formatted_data)
