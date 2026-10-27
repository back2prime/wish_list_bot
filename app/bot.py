import asyncio

from aiogram import Dispatcher, Bot
from os import getenv

from dotenv import load_dotenv

from app.ORM.database_middleware import DatabaseMiddleware

from app.core.db_helper import db
from app.ORM.models import Item, User, Wishlist  # noqa
from app.handlers import main_router

load_dotenv()

bot_token = getenv("BOT_TOKEN")

dp = Dispatcher()


if bot_token:
    bot = Bot(token=bot_token)
else:
    raise ValueError("Не удалось найти BOT_TOKEN")


async def main():
    dp.update.middleware(DatabaseMiddleware())
    await db.create_tables()
    dp.include_router(main_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
