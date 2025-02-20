from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from datetime import date
from src.core.database import get_db
from src.services.summary_service import fetch_daily_summary, fetch_summary_timeseries_service
from src.schemas.summary_schema import DailySummaryResponse, SummaryTimeseriesResponse

router = APIRouter()


@router.get("/analysis/daily-summary", response_model=DailySummaryResponse)
def daily_summary(
    summary_date: date = Query(..., description="Date in YYYY-MM-DD format"),
    db: Session = Depends(get_db)
):
    return fetch_daily_summary(db, summary_date)


@router.get("/analysis/timeseries", response_model=SummaryTimeseriesResponse)
def get_summary_timeseries(
    db: Session = Depends(get_db),
    range: int = Query(7, description="Number of days to retrieve (7 or 30)")
):
    return fetch_summary_timeseries_service(db, range)
