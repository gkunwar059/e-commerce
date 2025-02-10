from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property


from db import engine


class Base(DeclarativeBase):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    phone_number: Mapped[str] = mapped_column(unique=True, index=True)
    orders: Mapped[list["Order"]] = relationship(
        back_populates="user", cascade="all , delete-orphan"
    )
    cart: Mapped["Cart"] = relationship(
        back_populates="user", cascade="all , delete-orphan", uselist=False
    )


class Category(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True, unique=True)
    products: Mapped[list["Product"]] = relationship(
        back_populates="category", cascade="all , delete-orphan"
    )


class Product(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(index=True)
    price: Mapped[float]
    quantity: Mapped[int]
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id"))
    orders: Mapped[list["Order"]] = relationship(
        secondary="productorder", back_populates="products"
    )

    category: Mapped["Category"] = relationship(back_populates="products")

    cart_items: Mapped[list["CartItem"]] = relationship(
        back_populates="product", cascade="all , delete-orphan"
    )


class Order(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    quantity: Mapped[int]

    user: Mapped["User"] = relationship(back_populates="orders")
    products: Mapped[list["Product"]] = relationship(
        back_populates="orders", secondary="productorder"
    )

    @hybrid_property
    def total_price(self):
        return sum(product.price for product in self.product)

    # EXPRESSION WILL HANDLE LATER ON IN THE CODE


class ProductOrder(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"), primary_key=True)
    order_id: Mapped[int] = mapped_column(ForeignKey("order.id"), primary_key=True)


class Cart(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), index=True)
    user: Mapped["User"] = relationship(back_populates="cart")
    cart_items: Mapped[list["CartItem"]] = relationship(
        back_populates="cart", cascade="all , delete-orphan"
    )


class CartItem(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    cart_id: Mapped[int] = mapped_column(ForeignKey("cart.id"))
    product_id: Mapped[int] = mapped_column(ForeignKey("product.id"))
    quantity: Mapped[int]
    cart: Mapped["Cart"] = relationship(back_populates="cart_items")
    product: Mapped["Product"] = relationship(back_populates="cart_items")


Base.metadata.create_all(bind=engine)
