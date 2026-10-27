from aiogram.fsm.state import StatesGroup, State


class WishlistCreation(StatesGroup):
    waiting_for_title = State()
