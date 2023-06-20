from contextlib import suppress
from dataclasses import dataclass

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageToEditNotFound, MessageCantBeEdited, MessageNotModified
from aiogram.utils.markdown import hide_link

from app.bot import keyboards
from app.bot.states import LessonState
from app.bot.texts import MessageText
from app.db.manage import Database


@dataclass
class LessonWindow:
    EditTextErrors = MessageToEditNotFound, MessageCantBeEdited, MessageNotModified

    @staticmethod
    async def list(call: CallbackQuery, state: FSMContext) -> None:
        data = await state.get_data()
        lesson_id = data["lesson_id"] if "lesson_id" in data else None

        db: Database = call.bot.get("db")
        lessons = await db.lesson.get_all()

        text = MessageText.get("list_of_lessons")
        markup = keyboards.lesson_list(lessons, lesson_id)

        with suppress(*LessonWindow.EditTextErrors):
            await call.message.edit_text(text, reply_markup=markup)
        await LessonState.list.set()

    @classmethod
    async def learning(cls, call: CallbackQuery, state: FSMContext) -> None:
        data = await state.get_data()
        lesson_id = data["lesson_id"] if "lesson_id" in data else 1
        lesson_variant = data["lesson_variant"] if "lesson_variant" in data else "video_variant"

        db: Database = call.bot.get("db")
        lesson = await db.lesson.get(lesson_id)

        match lesson_variant:
            case "text_variant":
                content_url = lesson.text_url
            case "audio_variant":
                content_url = lesson.audio_url
            case _:
                content_url = lesson.video_url

        text = (
            f"<b>{lesson.title}</b>\n\n"
            f"{lesson.description}"
            f"{hide_link(content_url)}"
        )
        markup = keyboards.learning(lesson_variant)

        with suppress(*LessonWindow.EditTextErrors):
            await call.message.edit_text(text, reply_markup=markup)
        await LessonState.learning.set()
