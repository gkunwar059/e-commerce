from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    phone_number: str


class ProductSchema(BaseModel):
    name: str
    price: float
    quantity: int
    category_id: int


class CategorySchema(BaseModel):
    name: str
