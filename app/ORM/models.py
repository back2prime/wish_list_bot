from decimal import Decimal

from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from app.core.base import Base
from sqlalchemy.orm import Mapped

from app.ORM.enums import Priority


class User(Base):

    telegram_id: Mapped[int] = mapped_column(unique=True)

    wishlists: Mapped[list["Wishlist"]] = relationship(back_populates="user")


class Wishlist(Base):

    title: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship("User", back_populates="wishlists")
    item: Mapped[list["Item"]] = relationship(back_populates="wishlist")


class Item(Base):

    wishlist_id: Mapped[int] = mapped_column(ForeignKey("wishlist.id"))
    title: Mapped[str]
    photo_file_id: Mapped[str]
    url: Mapped[str]
    price: Mapped[Decimal]
    priority: Mapped[Priority]

    wishlist: Mapped["Wishlist"] = relationship(back_populates="item")
