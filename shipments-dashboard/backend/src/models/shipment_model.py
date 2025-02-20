from sqlalchemy import Column, String, Float, Integer, ForeignKey
from src.core.database import Base

class ShipmentModel(Base):
    __tablename__ = "shipments"

    shipment_id = Column(String, primary_key=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    weight = Column(Float)
    cost = Column(Float)
    delivery_time = Column(Integer)
    log_id = Column(String, ForeignKey("vehicle_logs.log_id"), nullable=False)
