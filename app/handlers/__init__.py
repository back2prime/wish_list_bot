from aiogram import Router

from app.handlers.help_handlers import help_router
from app.handlers.start_handlers import start_router
from app.handlers.wishlist_handlers import wishlist_router

main_router = Router(name="main_router")
main_router.include_routers(start_router, help_router, wishlist_router)
