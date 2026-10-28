from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession

from app.ORM.utils import create_new_wishlist, get_wishlist
from app.keyboard_enums import KeyboardButtons as KB
from app.states import WishlistCreation
from app.utils.keyboard_utils import create_wishlist_list

wishlist_router = Router()


@wishlist_router.callback_query(F.data == KB.create_new_wishlist)
async def request_wishlist_title_handler(
    callback: CallbackQuery, state: FSMContext
) -> None:
    await callback.message.answer("Введи название вишлиста 👇")
    await state.set_state(WishlistCreation.waiting_for_title)
    await callback.answer()


@wishlist_router.message(WishlistCreation.waiting_for_title)
async def wishlist_title_received_handler(
    message: Message, state: FSMContext, session: AsyncSession
):
    wishlist_title = message.text
    fsm_data = await state.get_data()
    await create_new_wishlist(
        id=fsm_data["user_id"], title=wishlist_title, session=session
    )
    await state.set_state(None)
    await message.answer(f"Вишлист '{wishlist_title}' создан.")


@wishlist_router.callback_query(F.data == KB.wishlists_list)
async def show_wishlists_list(callback: CallbackQuery,session: AsyncSession, state: FSMContext) -> None:
    fsm_id = await state.get_data()
    wishlist_list = await get_wishlist(id=fsm_id["user_id"],session=session)
    await callback.message.answer(text="Твои вишлисты",reply_markup=create_wishlist_list(wishlist_list=wishlist_list))
    await callback.answer()

