from sqlalchemy.orm import Session
from functools import lru_cache
from datetime import date, timedelta, datetime
from src.repositories.summary_repo import get_daily_summary
from src.repositories.summary_repo import get_summary_timeseries_data
from src.schemas.summary_schema import SummaryTimeseriesResponse, SummaryTimeseriesData, DailySummaryResponse


def fetch_daily_summary(db: Session, summary_date: date) -> DailySummaryResponse:
    raw_data = get_daily_summary(db, summary_date)

    return DailySummaryResponse(
        date=summary_date,
        num_shipments=raw_data.num_shipments or 0,
        total_vehicles_used=raw_data.total_vehicles_used or 0,
        total_mileage=round(float(raw_data.total_mileage),
                            2) if raw_data.total_mileage else 0,
        total_fuel_used=round(float(raw_data.total_fuel_used),
                              2) if raw_data.total_fuel_used else 0
    )


@lru_cache(maxsize=1)
def fetch_summary_timeseries_service(db: Session, days: int) -> SummaryTimeseriesResponse:
    if days not in [7, 30]:
        raise ValueError("Invalid range. Only 7 or 30 days are supported.")

    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=days - 1)

    raw_data = get_summary_timeseries_data(db, start_date, end_date)

    formatted_data = [
        SummaryTimeseriesData(
            date=row.date,
            num_shipments=row.num_shipments or 0,
            total_vehicles_used=row.total_vehicles_used or 0,
            total_fuel_used=round(row.total_fuel_used or 0, 2),
            total_mileage=round(row.total_mileage or 0, 2),
        )
        for row in raw_data
    ]

    return SummaryTimeseriesResponse(data=formatted_data)
