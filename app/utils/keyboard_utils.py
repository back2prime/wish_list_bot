from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def create_keyboard() -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text="Создать новый вишлист", callback_data="create_new_wishlist"
    )
    keyboard_builder.button(text="Список вишлистов", callback_data="wishlists_list")
    keyboard_builder.button(text="Как все устроено", callback_data="wishlists_help")
    return keyboard_builder.adjust(1).as_markup()
