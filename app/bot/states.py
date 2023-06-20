from aiogram.dispatcher.filters.state import StatesGroup, State


class MainState(StatesGroup):
    menu = State()

    about_the_author = State()
    connect_with_us = State()
    copyright_holders = State()


class LessonState(StatesGroup):
    list = State()
    learning = State()
