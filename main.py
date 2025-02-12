from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from db import get_db
from models import Category, Product, User
from schemas import CategorySchema, ProductSchema, UserSchema

app = FastAPI()

"""
CRUD OPERATION OF USER
"""


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


@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter_by(id=user_id).first()
    return user


"""
CRUD OPERATION OF PRODUCT & CATEGORY
"""

@app.get("/categories/")
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(Category).all()
    return categories


@app.get("/categories/{category_id}")
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = db.query(Category).filter_by(id=category_id).first()
    return category


@app.patch("/categories/{category_id}")
def update_category(
    category_id: int, body: CategorySchema, db: Session = Depends(get_db)
):
    category = db.query(Category).filter_by(id=category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    update_category = body.model_dump(exclude_unset=True)
    db.query(Category).filter_by(id=category_id).update(update_category)
    db.commit()
    return {"msg": "Category updated successfully"}


@app.delete("/categories/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db.query(Category).filter_by(id=category_id).delete()
    db.commit()
    return {"msg": "Category deleted successfully"}


@app.post("/categories", status_code=201, response_model=CategorySchema)
def create_category(body: CategorySchema, db: Session = Depends(get_db)):
    new_category = body.model_dump(exclude_unset=True)

    category = Category(**new_category)
    db.add(category)
    db.commit()
    return category


@app.get("/products/")
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter_by(id=product_id).first()
    return product


@app.post("/products", status_code=201, response_model=ProductSchema)
def create_product(body: ProductSchema, db: Session = Depends(get_db)):
    new_product = body.model_dump(exclude_unset=True)

    product = Product(**new_product)
    db.add(product)
    db.commit()
    return product


@app.patch("/products/{product_id}")
def update_product(product_id: int, body: ProductSchema, db: Session = Depends(get_db)):
    product = db.query(Product).filter_by(id=product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    update_product = body.model_dump(exclude_unset=True)
    db.query(Product).filter_by(id=product_id).update(update_product)
    db.commit()
    return {"msg": "Product updated successfully"}


@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db.query(Product).filter_by(id=product_id).delete()
    db.commit()
    return {"msg": "Product deleted successfully"}


