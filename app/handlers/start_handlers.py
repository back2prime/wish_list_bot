from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from app.ORM.utils import get_or_create_user
from app.utils.keyboard_utils import create_keyboard

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(
    message: Message, session: AsyncSession, state: FSMContext
) -> None:
    await message.answer(text="Hi!", reply_markup=create_keyboard())
    current_user = await get_or_create_user(
        user_id=message.from_user.id, session=session
    )
    await state.update_data(user_id=current_user.id)
