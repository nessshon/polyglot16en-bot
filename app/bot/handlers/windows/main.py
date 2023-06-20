from contextlib import suppress
from dataclasses import dataclass

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageToEditNotFound, MessageCantBeEdited, MessageNotModified

from app.bot import keyboards
from app.bot.states import MainState
from app.bot.texts import MessageText


@dataclass
class MainWindow:
    EditTextErrors = MessageToEditNotFound, MessageCantBeEdited, MessageNotModified

    @classmethod
    async def menu(cls, call: CallbackQuery, state: FSMContext) -> None:
        data = await state.get_data()
        lesson_id = data["lesson_id"] if "lesson_id" in data else None

        text = MessageText.get("main_menu")
        markup = keyboards.main_menu(lesson_id)

        with suppress(*cls.EditTextErrors):
            await call.message.edit_text(text, reply_markup=markup)
        await MainState.menu.set()

    @classmethod
    async def about_the_author(cls, call: CallbackQuery) -> None:
        text = MessageText.get("about_the_author")
        markup = keyboards.back()

        with suppress(*cls.EditTextErrors):
            await call.message.edit_text(text, reply_markup=markup)
        await MainState.about_the_author.set()

    @classmethod
    async def connect_with_us(cls, call: CallbackQuery) -> None:
        text = MessageText.get("connect_with_us")
        markup = keyboards.connect_with_us()

        with suppress(*cls.EditTextErrors):
            await call.message.edit_text(text, reply_markup=markup)
        await MainState.connect_with_us.set()

    @classmethod
    async def copyright_holders(cls, call: CallbackQuery) -> None:
        text = MessageText.get("copyright_holders")
        markup = keyboards.back()

        with suppress(*cls.EditTextErrors):
            await call.message.edit_text(text, reply_markup=markup)
        await MainState.copyright_holders.set()
