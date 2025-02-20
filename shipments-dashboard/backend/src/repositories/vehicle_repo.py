from sqlalchemy.orm import Session
from sqlalchemy import func
from src.models.vehicle_model import VehicleModel
from src.models.vehicle_log_model import VehicleLogModel


def get_vehicle(db: Session, vehicle_id: str):
    return db.query(VehicleModel).filter(VehicleModel.vehicle_id == vehicle_id).first()


def get_vehicle_efficiency(db: Session, limit: int, offset: int):
    results = (
        db.query(
            VehicleLogModel.vehicle_id,
            func.sum(VehicleLogModel.mileage).label("total_mileage"),
            func.sum(VehicleLogModel.fuel_used).label("total_fuel_used")
        )
        .filter(
            VehicleLogModel.mileage.isnot(None),
            VehicleLogModel.fuel_used.isnot(None)
        )
        .group_by(VehicleLogModel.vehicle_id)
        .order_by(func.sum(VehicleLogModel.mileage).desc())
        .limit(limit)
        .offset(offset)
        .all()
    )

    return results
