from aiogram import Dispatcher, Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats

from app.bot.filters import IsPrivate
from app.bot.handlers.commands.start import start_command


async def setup(bot: Bot) -> None:
    commands = [
        BotCommand("start", "Перезапустить"),
    ]

    await bot.set_my_commands(
        commands=commands,
        scope=BotCommandScopeAllPrivateChats(),
    )


def register(dp: Dispatcher) -> None:
    dp.register_message_handler(
        start_command, IsPrivate(),
        commands="start", state="*"
    )
