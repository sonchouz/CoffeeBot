#Функции бота
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)


def get_main_menu() -> ReplyKeyboardMarkup:
    keyboard = [
        [
            KeyboardButton(text="🎁 Бонусы"),
            KeyboardButton(text="🆕 Новинки"),
        ],
        [
            KeyboardButton(text="🔥 Акции"),
            KeyboardButton(text="🔔 Уведомления"),
        ],
        [
            KeyboardButton(text="👤 Мой профиль"),
        ],
    ]

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
        input_field_placeholder="Выберите раздел",
    )
