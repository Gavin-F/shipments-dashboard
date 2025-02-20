from sqlalchemy import Column, String, Float
from src.core.database import Base

class VehicleModel(Base):
    __tablename__ = "vehicles"

    vehicle_id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    total_mileage = Column(Float, default=0)
