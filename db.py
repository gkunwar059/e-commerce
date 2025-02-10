from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLAlchemy setup
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test-redis-database"
engine = create_engine(url=DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
