from pydantic import BaseModel
from typing import List


class ShipmentBase(BaseModel):
    shipment_id: str
    origin: str
    destination: str
    weight: float
    cost: float
    delivery_time: int
    log_id: str


class ShipmentResponse(ShipmentBase):
    class Config:
        from_attributes = True


class RouteSummaryResponse(BaseModel):
    origin: str
    destination: str
    average_delivery_time: float
    total_cost: float
    num_deliveries: int


class ExpensiveRouteResponse(BaseModel):
    origin: str
    destination: str
    total_cost: float
    num_deliveries: int


class TopExpensiveRoutesResponse(BaseModel):
    data: List[ExpensiveRouteResponse]
