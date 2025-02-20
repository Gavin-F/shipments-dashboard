CREATE TABLE vehicles (
    vehicle_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    total_mileage FLOAT DEFAULT 0 CHECK (total_mileage >= 0)
);

CREATE TABLE vehicle_logs (
    log_id TEXT PRIMARY KEY,
    vehicle_id TEXT NOT NULL,
    trip_date DATE NOT NULL,
    mileage FLOAT CHECK (mileage >= 0),
    fuel_used FLOAT CHECK (fuel_used >= 0),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id) ON DELETE CASCADE
);

CREATE TABLE shipments (
    shipment_id TEXT PRIMARY KEY,
    origin TEXT NOT NULL,
    destination TEXT NOT NULL,
    weight FLOAT CHECK (weight >= 0),
    cost FLOAT CHECK (cost >= 0),
    delivery_time INT CHECK (delivery_time >= 0),
    log_id TEXT NOT NULL,
    FOREIGN KEY (log_id) REFERENCES vehicle_logs(log_id) ON DELETE CASCADE
);

CREATE INDEX idx_vehicle_logs_vehicle ON vehicle_logs(vehicle_id);
CREATE INDEX idx_vehicle_logs_trip_date ON vehicle_logs (trip_date);
CREATE INDEX idx_shipments_log ON shipments(log_id);

-- docker exec -i logistics_db psql -U admin -d logistics < initial_schema.sql