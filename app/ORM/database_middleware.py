from aiogram import BaseMiddleware

from app.core.db_helper import db


class DatabaseMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        async with db.session_factory() as session:
            data["session"] = session
            await handler(event, data)
