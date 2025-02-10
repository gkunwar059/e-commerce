from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models import User
from schemas import UserSchema

from fastapi import FastAPI

app = FastAPI()


@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@app.post("/users", status_code=201, response_model=UserSchema)
def create_user(body: UserSchema, db: Session = Depends(get_db)):
    new_user = body.model_dump(exclude_unset=True)

    user = User(**new_user)
    if user.email in [user.email for user in db.query(User).all()]:
        raise HTTPException(status_code=400, detail="Email already exists")
    db.add(user)
    db.commit()

    return user


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
