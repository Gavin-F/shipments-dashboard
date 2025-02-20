from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date
from src.models.shipment_model import ShipmentModel
from src.models.vehicle_log_model import VehicleLogModel


def get_daily_summary(db: Session, summary_date: date):
    result = (
        db.query(
            func.count(ShipmentModel.shipment_id).label("num_shipments"),
            func.count(func.distinct(VehicleLogModel.vehicle_id)).label("total_vehicles_used"),
            func.sum(func.distinct(VehicleLogModel.mileage)).label("total_mileage"),
            func.sum(func.distinct(VehicleLogModel.fuel_used)).label("total_fuel_used")
        )
        .join(
            ShipmentModel, ShipmentModel.log_id == VehicleLogModel.log_id, isouter=True
        )
        .filter(
            VehicleLogModel.trip_date == summary_date,
            VehicleLogModel.mileage.isnot(None),
            VehicleLogModel.fuel_used.isnot(None)
        )
        .first()
    )

    return result


def get_summary_timeseries_data(db: Session, start_date: date, end_date: date):
    return db.query(
        func.date(VehicleLogModel.trip_date).label("date"),
        func.count(ShipmentModel.shipment_id).label("num_shipments"),
        func.count(func.distinct(VehicleLogModel.vehicle_id)).label("total_vehicles_used"),
        func.sum(func.distinct(VehicleLogModel.mileage)).label("total_mileage"),
        func.sum(func.distinct(VehicleLogModel.fuel_used)).label("total_fuel_used")
    ).join(
        ShipmentModel, ShipmentModel.log_id == VehicleLogModel.log_id, isouter=True
    ).filter(
        VehicleLogModel.mileage.isnot(None),
        VehicleLogModel.fuel_used.isnot(None),
        func.date(VehicleLogModel.trip_date).between(start_date, end_date)
    ).group_by(
        func.date(VehicleLogModel.trip_date)
    ).order_by(
        func.date(VehicleLogModel.trip_date)
    ).all()
