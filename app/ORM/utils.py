from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.ORM.models import User


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
