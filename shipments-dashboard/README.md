# Setup DB
cd shipments-dashboard/
docker-compose up -d
docker exec -i logistics_db psql -U admin -d logistics < scripts/initial_schema.sql
docker exec -i logistics_db psql -U admin -d logistics < scripts/seed_vehicles.sql
docker exec -i logistics_db psql -U admin -d logistics < scripts/seed_vehicle_logs.sql
docker exec -i logistics_db psql -U admin -d logistics < scripts/seed_shipments.sql
# Run backend
cd backend
pip3 install -r requirements.txt 
# Run frontend
cd ../frontend
npm install
npm run dev

http://localhost:5173/ React App
http://localhost:8000/docs for openapi spec