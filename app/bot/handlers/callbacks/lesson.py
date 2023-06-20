from dataclasses import dataclass

from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from app.bot.handlers.windows.lesson import LessonWindow
from app.bot.handlers.windows.main import MainWindow


@dataclass
class LessonCallbackHandler:

    @staticmethod
    async def list(call: CallbackQuery, state: FSMContext) -> None:
        match call.data:
            case "back":
                await MainWindow.menu(call, state)
            case lesson_id if lesson_id.isdigit():
                await state.update_data(lesson_id=int(lesson_id))
                await LessonWindow.learning(call, state)
        await call.answer()

    @staticmethod
    async def learning(call: CallbackQuery, state: FSMContext) -> None:
        data = await state.get_data()

        match call.data:
            case "back":
                await MainWindow.menu(call, state)
            case "list":
                await LessonWindow.list(call, state)
            case "prev":
                current_lesson = data["lesson_id"]
                prev_lesson = current_lesson - 1 if current_lesson != 1 else 16
                await state.update_data(lesson_id=prev_lesson)
                await LessonWindow.learning(call, state)
            case "next":
                current_lesson = data["lesson_id"]
                next_lesson = current_lesson + 1 if current_lesson != 16 else 1
                await state.update_data(lesson_id=next_lesson)
                await LessonWindow.learning(call, state)
            case "video_variant":
                await state.update_data(lesson_variant="video_variant")
                await LessonWindow.learning(call, state)
            case "text_variant":
                await state.update_data(lesson_variant="text_variant")
                await LessonWindow.learning(call, state)
            case "audio_variant":
                await state.update_data(lesson_variant="audio_variant")
                await LessonWindow.learning(call, state)
        await call.answer()
