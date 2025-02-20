from fastapi import FastAPI
from src.core.database import engine
from src.models import Base
from src.routes import shipments_route, vehicle_logs_route, vehicles_route, summary_route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Logistics API")

Base.metadata.create_all(bind=engine)

app.include_router(shipments_route.router,
                   prefix="/shipments", tags=["Shipments"])
app.include_router(vehicles_route.router,
                   prefix="/vehicles", tags=["Vehicles"])
app.include_router(vehicle_logs_route.router,
                   prefix="/vehicle-logs", tags=["Vehicle Logs"])
app.include_router(summary_route.router, tags=["Summary Analytics"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Root
@app.get("/")
def home():
    return {"message": "Welcome to the Logistics API"}
