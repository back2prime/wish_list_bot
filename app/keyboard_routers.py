from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from sqlalchemy.ext.asyncio import AsyncSession

from app.ORM.utils import get_or_create_user
from app.utils.keyboard_utils import create_keyboard

from app.keyboard_enums import KeyboardButtons as KB

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, session: AsyncSession) -> None:
    await message.answer(text="Hi!", reply_markup=create_keyboard())
    await get_or_create_user(user_id=message.from_user.id, session=session)


@router.callback_query(F.data == KB.wishlists_help)
async def callback_handler(callback: CallbackQuery) -> None:
    await callback.message.answer(
        "Тут должен быть какой-то текст по справке. Поменять потом!"
    )
    await callback.answer()
