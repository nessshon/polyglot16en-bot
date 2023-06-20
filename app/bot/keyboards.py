from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.bot.texts import ButtonText
from app.db.models import Lesson


def learning(lesson_variant: str) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=3)

    video_variant = ButtonText.get("video_variant")
    text_variant = ButtonText.get("text_variant")
    audio_variant = ButtonText.get("audio_variant")

    markup.add(
        InlineKeyboardButton(
            text=f"· {video_variant} ·" if lesson_variant == "video_variant" else video_variant,
            callback_data=f"video_variant",
        ),
        InlineKeyboardButton(
            text=f"· {text_variant} ·" if lesson_variant == "text_variant" else text_variant,
            callback_data=f"text_variant",
        ),
        InlineKeyboardButton(
            text=f"· {audio_variant} ·" if lesson_variant == "audio_variant" else audio_variant,
            callback_data=f"audio_variant",
        ),
    )
    markup.add(
        InlineKeyboardButton(
            text=ButtonText.get("prev"),
            callback_data="prev",
        ),
        InlineKeyboardButton(
            text=ButtonText.get("list"),
            callback_data="list",
        ),
        InlineKeyboardButton(
            text=ButtonText.get("next"),
            callback_data=f"next",
        )
    )
    markup.row(
        InlineKeyboardButton(
            text=ButtonText.get("back"),
            callback_data="back",
        )
    )
    return markup


def lesson_list(lessons: list[Lesson], lesson_id: int | None) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=4)

    markup.add(*[
        InlineKeyboardButton(
            text=f"· {lesson.title} ·" if lesson_id == lesson.id else lesson.title,
            callback_data=str(lesson.id)
        ) for lesson in lessons
    ])
    markup.row(
        InlineKeyboardButton(
            text=ButtonText.get("back"),
            callback_data="back",
        )
    )
    return markup


def connect_with_us() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)

    markup.add(
        InlineKeyboardButton(
            text=ButtonText.get("write_a_message"),
            url="https://t.me/NessFeedbackBot",
        ),
        InlineKeyboardButton(
            text=ButtonText.get("back"),
            callback_data="back",
        ),
    )
    return markup


def main_menu(lesson_id: int | None) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()

    markup.row(
        InlineKeyboardButton(
            text=ButtonText.get("continue_learning") if lesson_id else ButtonText.get("start_learning"),
            callback_data="continue_learning" if lesson_id else "start_learning",
        ),
    )
    markup.row(
        InlineKeyboardButton(
            text=ButtonText.get("list_of_lessons"),
            callback_data="list_of_lessons",
        ),
        InlineKeyboardButton(
            text=ButtonText.get("connect_with_us"),
            callback_data="connect_with_us",
        ),
    )
    markup.row(
        InlineKeyboardButton(
            text=ButtonText.get("about_the_author"),
            callback_data="about_the_author",
        ),
        InlineKeyboardButton(
            text=ButtonText.get("copyright_holders"),
            callback_data="copyright_holders",
        ),
    )
    return markup


def back() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)

    markup.add(
        InlineKeyboardButton(
            text=ButtonText.get("back"),
            callback_data="back",
        ),
    )
    return markup
