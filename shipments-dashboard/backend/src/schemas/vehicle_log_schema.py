from pydantic import BaseModel
from datetime import date


class VehicleLogBase(BaseModel):
    log_id: str
    vehicle_id: str
    trip_date: date
    mileage: float | None
    fuel_used: float | None


class VehicleLogResponse(VehicleLogBase):
    class Config:
        from_attributes = True
