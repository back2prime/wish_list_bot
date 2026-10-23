from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
    AsyncEngine,
)

from app.core.config import settings


class DatabaseHelper:

    def __init__(self, url: str, echo: bool, pool_pre_ping: bool):
        self.engine: AsyncEngine = create_async_engine(
            url=url, echo=echo, pool_pre_ping=pool_pre_ping
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine, autoflush=False, expire_on_commit=False
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, Any]:
        async with self.session_factory() as session:
            yield session


db = DatabaseHelper(
    url=settings.db.async_url,
    echo=settings.db.echo,
    pool_pre_ping=settings.db.pool_pre_ping,
)
