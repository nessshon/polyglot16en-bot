import asyncio
from contextlib import suppress

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from app.bot import keyboards
from app.bot.handlers.windows.main import MainWindow
from app.bot.misc.messages import delete_previous_message, delete_message
from app.bot.misc.throttling import rate_limit
from app.bot.states import MainState
from app.bot.texts import MessageText
from app.db.manage import Database


@rate_limit(1)
async def start_command(message: Message, state: FSMContext) -> None:
    await delete_previous_message(message.bot, state)
    msg = await message.answer("👋")
    await delete_message(message)
    await asyncio.sleep(1.5)

    db: Database = message.bot.get("db")
    if not await db.user.is_exists(message.from_user.id):
        await db.user.add(
            id=message.from_user.id,
            first_name=message.from_user.first_name,
        )

    data = await state.get_data()
    lesson_id = data["lesson_id"] if "lesson_id" in data else None

    text = MessageText.get("main_menu")
    markup = keyboards.main_menu(lesson_id)

    with suppress(MainWindow.EditTextErrors):
        await msg.edit_text(text, reply_markup=markup)
        await state.update_data(message_id=msg.message_id)
    await MainState.menu.set()
