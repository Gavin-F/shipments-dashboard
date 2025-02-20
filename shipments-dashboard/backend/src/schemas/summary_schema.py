from pydantic import BaseModel
from datetime import date
from typing import List


class DailySummaryResponse(BaseModel):
    date: date
    num_shipments: int
    total_vehicles_used: int
    total_mileage: float
    total_fuel_used: float


class SummaryTimeseriesData(BaseModel):
    date: date
    num_shipments: int
    total_vehicles_used: int
    total_fuel_used: float
    total_mileage: float


class SummaryTimeseriesResponse(BaseModel):
    data: List[SummaryTimeseriesData]
