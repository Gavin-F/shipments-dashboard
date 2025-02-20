from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
import os
import time
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy database setup
for attempt in range(5):
    try:
        engine = create_engine(DATABASE_URL)
        SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=engine)
        print("Successfully connected to the database.")
        break
    except OperationalError:
        print(f" Database not ready, retrying ({attempt+1}/5)...")
        time.sleep(3)
else:
    raise Exception("Database connection failed after 5 retries.")


Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
