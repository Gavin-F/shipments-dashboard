from sqlalchemy.orm import Session
from src.models.shipment_model import ShipmentModel
from sqlalchemy import func


def get_shipment(db: Session, shipment_id: str):
    return db.query(ShipmentModel).filter(ShipmentModel.shipment_id == shipment_id).first()


def get_route_summary(db: Session, origin: str, destination: str):
    return db.query(
        func.avg(ShipmentModel.delivery_time).label("avg_delivery_time"),
        func.sum(ShipmentModel.cost).label("total_cost"),
        func.count(ShipmentModel.shipment_id).label("num_deliveries")
    ).filter(
        func.lower(ShipmentModel.origin) == origin.lower(),
        func.lower(ShipmentModel.destination) == destination.lower()
    ).first()


def get_top_expensive_routes(db: Session, limit: int = 5):
    return (
        db.query(
            ShipmentModel.origin,
            ShipmentModel.destination,
            func.sum(ShipmentModel.cost).label("total_cost"),
            func.count(ShipmentModel.shipment_id).label("num_deliveries")
        )
        .group_by(ShipmentModel.origin, ShipmentModel.destination)
        .order_by(func.sum(ShipmentModel.cost).desc())
        .limit(limit)
        .all()
    )
