from sqlalchemy import Column, String, Date, Float, ForeignKey
from src.core.database import Base

class VehicleLogModel(Base):
    __tablename__ = "vehicle_logs"

    log_id = Column(String, primary_key=True)
    trip_date = Column(Date, nullable=False)
    mileage = Column(Float)
    fuel_used = Column(Float)
    vehicle_id = Column(String, ForeignKey("vehicles.vehicle_id"), nullable=False)
