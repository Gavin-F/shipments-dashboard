from sqlalchemy.orm import Session
from src.repositories.vehicle_log_repo import get_vehicle_log

def fetch_vehicle_log(db: Session, log_id: str):
    return get_vehicle_log(db, log_id)
