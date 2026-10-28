from sqlalchemy import select, Sequence
from sqlalchemy.ext.asyncio import AsyncSession

from app.ORM.models import User, Wishlist


async def get_or_create_user(user_id: int, session: AsyncSession) -> User:
    stmt = select(User).where(User.telegram_id == user_id)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    if user:
        return user
    new_user = User(telegram_id=user_id)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user


async def create_new_wishlist(user_id: int, title: str, session: AsyncSession) -> Wishlist:
    new_wishlist = Wishlist(title=title, user_id=user_id)
    session.add(new_wishlist)
    await session.commit()
    await session.refresh(new_wishlist)
    return new_wishlist

async def get_wishlist(user_id: int,session: AsyncSession) -> Sequence[Wishlist]:
    stmt = select(Wishlist).where(Wishlist.user_id == user_id)
    result = await session.execute(stmt)
    wishlist_list = result.scalars().all()
    return wishlist_list
