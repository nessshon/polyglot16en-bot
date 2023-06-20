from aiogram import Dispatcher

from app.bot.filters import IsPrivate
from app.bot.states import MainState, LessonState


def register(dp: Dispatcher) -> None:
    from .main import MainCallbackHandler
    dp.register_callback_query_handler(
        MainCallbackHandler.menu, IsPrivate(),
        state=MainState.menu
    )
    dp.register_callback_query_handler(
        MainCallbackHandler.about_the_author, IsPrivate(),
        state=MainState.about_the_author
    )
    dp.register_callback_query_handler(
        MainCallbackHandler.connect_with_us, IsPrivate(),
        state=MainState.connect_with_us
    )
    dp.register_callback_query_handler(
        MainCallbackHandler.copyright_holders, IsPrivate(),
        state=MainState.copyright_holders
    )

    from .lesson import LessonCallbackHandler
    dp.register_callback_query_handler(
        LessonCallbackHandler.list, IsPrivate(),
        state=LessonState.list
    )
    dp.register_callback_query_handler(
        LessonCallbackHandler.learning, IsPrivate(),
        state=LessonState.learning
    )
