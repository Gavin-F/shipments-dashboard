from sqlalchemy.orm import Session
from src.models.vehicle_log_model import VehicleLogModel


def get_vehicle_log(db: Session, log_id: str):
    return db.query(VehicleLogModel).filter(VehicleLogModel.log_id == log_id).first()
