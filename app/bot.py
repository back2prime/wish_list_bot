import asyncio

from aiogram import Dispatcher, Bot
from os import getenv

from dotenv import load_dotenv

from keyboard_routers import router

load_dotenv()

bot_token = getenv("BOT_TOKEN")

dp = Dispatcher()

if bot_token:
    bot = Bot(token=bot_token)
else:
    raise ValueError("Не удалось найти BOT_TOKEN")


async def main():

    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
