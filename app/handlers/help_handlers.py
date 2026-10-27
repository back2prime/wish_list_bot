from aiogram import F, Router
from aiogram.types import CallbackQuery

from app.keyboard_enums import KeyboardButtons as KB

help_router = Router()


@help_router.callback_query(F.data == KB.wishlists_help)
async def callback_handler(callback: CallbackQuery) -> None:
    await callback.message.answer(
        "Тут должен быть какой-то текст по справке. Поменять потом!"
    )
    await callback.answer()
