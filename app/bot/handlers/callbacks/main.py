from dataclasses import dataclass

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from app.bot.handlers.windows.lesson import LessonWindow
from app.bot.handlers.windows.main import MainWindow


@dataclass
class MainCallbackHandler:

    @staticmethod
    async def menu(call: CallbackQuery, state: FSMContext) -> None:
        match call.data:
            case "start_learning":
                await state.update_data(lesson_id=1)
                await LessonWindow.learning(call, state)
            case "continue_learning":
                await LessonWindow.learning(call, state)
            case "list_of_lessons":
                await LessonWindow.list(call, state)
            case "connect_with_us":
                await MainWindow.connect_with_us(call)
            case "about_the_author":
                await MainWindow.about_the_author(call)
            case "copyright_holders":
                await MainWindow.copyright_holders(call)
        await call.answer()

    @staticmethod
    async def about_the_author(call: CallbackQuery, state: FSMContext) -> None:
        match call.data:
            case "back":
                await MainWindow.menu(call, state)
        await call.answer()

    @staticmethod
    async def connect_with_us(call: CallbackQuery, state: FSMContext) -> None:
        match call.data:
            case "back":
                await MainWindow.menu(call, state)
        await call.answer()

    @staticmethod
    async def copyright_holders(call: CallbackQuery, state: FSMContext) -> None:
        match call.data:
            case "back":
                await MainWindow.menu(call, state)
        await call.answer()
