import json
import os

# Configuration
DATA_DIR = "backend/data/"
OUTPUT_DIR = "scripts/"
BATCH_SIZE = 10000


def load_json(filename):
    with open(os.path.join(DATA_DIR, filename), "r") as f:
        return json.load(f)


def format_value(value):
    if value is None:
        return "NULL"
    elif isinstance(value, str):
        return f"'{value.replace("'", "''")}'"
    else:
        return str(value)


# Vehicles
def generate_vehicles_sql():
    vehicles = load_json("vehicles.json")
    sql = "INSERT INTO vehicles (vehicle_id, name, total_mileage) VALUES\n"
    sql += ",\n".join(
        [f"({format_value(v['vehicle_id'])}, {format_value(v['name'])}, {format_value(v['total_mileage'])})" for v in vehicles]
    )
    sql += ";\n"
    with open(os.path.join(OUTPUT_DIR, "seed_vehicles.sql"), "w") as f:
        f.write(sql)


# Vehicle Logs
def generate_vehicle_logs_sql():
    logs = load_json("vehicle_logs.json")
    with open(os.path.join(OUTPUT_DIR, "seed_vehicle_logs.sql"), "w") as f:
        for i in range(0, len(logs), BATCH_SIZE):
            batch = logs[i: i + BATCH_SIZE]
            sql = "INSERT INTO vehicle_logs (log_id, vehicle_id, trip_date, mileage, fuel_used) VALUES\n"
            sql += ",\n".join(
                [
                    f"({format_value(l['log_id'])}, {format_value(l['vehicle_id'])}, {format_value(l['trip_date'])}, {format_value(l['mileage'])}, {format_value(l['fuel_used'])})"
                    for l in batch
                ]
            )
            sql += ";\n\n"
            f.write(sql)


# Shipments
def generate_shipments_sql():
    shipments = load_json("shipments.json")
    with open(os.path.join(OUTPUT_DIR, "seed_shipments.sql"), "w") as f:
        for i in range(0, len(shipments), BATCH_SIZE):
            batch = shipments[i: i + BATCH_SIZE]
            sql = "INSERT INTO shipments (shipment_id, origin, destination, weight, cost, delivery_time, log_id) VALUES\n"
            sql += ",\n".join(
                [
                    f"({format_value(s['shipment_id'])}, {format_value(s['origin'])}, {format_value(s['destination'])}, {format_value(s['weight'])}, {format_value(s['cost'])}, {format_value(s['delivery_time'])}, {format_value(s['log_id'])})"
                    for s in batch
                ]
            )
            sql += ";\n\n"
            f.write(sql)


def main():
    generate_vehicles_sql()
    generate_vehicle_logs_sql()
    generate_shipments_sql()
    print("SQL seed files generated")


if __name__ == "__main__":
    main()
