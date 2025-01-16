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


# SQLalchemy User Model
class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True, index=True)
    phone_number: Mapped[str] = mapped_column(unique=True, index=True)


Base.metadata.create_all(bind=engine)


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    phone_number: str


# FastAPI routes
@app.get("/", status_code=200)  # status code can be used here
async def root():
    return {"message": "Hello World!"}


@app.post("/users")
def create_user(body: UserSchema, db: Session = Depends(get_db)):
    new_user = body.model_dump(
        exclude_unset=True
    )  # body.dict() and body.model_dump is similar ?
    user = User(**new_user)
    # user=User(**body.model_dump(exclude_unset=True))      #clean code in a single line no need to assign the variable
    # user = User(name=body.name, email=body.email, phone_number=body.phone_number)
    db.add(user)
    db.commit()
    return {"message": "User created successfully"}

@app.patch("/users/{user_id}")
def update_user(user_id: int, body: UserSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    update_data = body.model_dump(exclude_unset=True)

    """
    
    this one the better approach for this and update the user using the built in function too 
    """

    user = db.query(User).filter_by(id=user_id).update(update_data)

    """
    this below approach is of using the loop
    it will iterate over the loop and update the user attributes
    # """
    # update_data=body.model_dump(exclude_unset=True)
    # for key, value in update_data.items():               #Dict Approach
    #     setattr(user, key, value)

    """
    last one approach of the update
    
    """
    # if user:
    #     user.name = body.name
    #     user.email = body.email
    #     user.phone_number = body.phone_number

    db.commit()
    return {"message": "User updated successfully"}


@app.put("/users/{user_id}")
def update_users(user_id: int, body: UserSchema, db: Session = Depends(get_db)):
    """
    to update the entire resource
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    update_data = body.model_dump(exclude_unset=True)
    user = db.query(User).filter_by(id=user_id).update(update_data)
    db.commit()
    return {"message": "User updated successfully-Put"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    filter_by and filter
    """
    db.query(User).filter(
        User.id == user_id
    ).first()  # filter left side will be of the model side and another will be query a=b
    # a is already present and b is given to find the a , generally it works both are for the same value

    """
    Direct the delete request to the DB  #filter_by is used here too 
    """
    # db.query(User).filter_by(id=user_id).delete()
    """'
    this approach is not optimized fetch the user and delete the user
    """
    # user = db.query(User).filter(User.id == user_id).first()
    # if not user:
    #     raise HTTPException(status_code=404, detail="User not found")

    # db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}


"""
To update this automatically right / 
"""
# if __name__ == "__main__":
#     uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
