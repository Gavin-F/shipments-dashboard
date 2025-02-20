from pydantic import BaseModel
from typing import List


class VehicleBase(BaseModel):
    vehicle_id: str
    name: str
    total_mileage: float


class VehicleResponse(VehicleBase):
    class Config:
        from_attributes = True


class VehicleEfficiencyResponse(BaseModel):
    vehicle_id: str
    total_mileage: float
    total_fuel_used: float
    fuel_efficiency: float


class VehicleEfficiencyListResponse(BaseModel):
    data: List[VehicleEfficiencyResponse]
