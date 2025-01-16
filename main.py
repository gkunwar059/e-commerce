import redis
from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, Session, mapped_column, sessionmaker

# SQLAlchemy setup
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/test-redis-database"
Base = declarative_base()
engine = create_engine(url=DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Redis setup
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)


# FastAPI app
app = FastAPI()


# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = "users"  # TODO: REMOVE THIS TABLE_NAME
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True, index=True)
    phone_number: Mapped[str] = mapped_column(unique=True, index=True)


Base.metadata.create_all(bind=engine)


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    phone_number: str


@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.post("/users", status_code=201)
def create_user(body: UserSchema, db: Session = Depends(get_db)):
    user = User(body.model_dump(exclude_unset=True))
    db.add(user)
    db.commit()
    return {"msg": "User created successfully"}


@app.patch("/users/{user_id}")
def update_user(user_id: int, body: UserSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = body.model_dump(exclude_unset=True)
    db.query(User).filter_by(id=user_id).update(update_data)
    db.commit()
    return {"msg": "User updated successfully"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db.query(User).filter_by(id=user_id).delete()
    db.commit()
    return {"msg": "User deleted successfully"}
