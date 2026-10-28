#Начало работы бота
from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboards.main_menu import get_main_menu


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "☕ Добро пожаловать в кофейню!\n\n"
        "Здесь вы сможете:\n"
        "🎁 Проверять бонусный баланс\n"
        "🆕 Узнавать о новинках\n"
        "🔥 Просматривать акции\n"
        "🔔 Управлять уведомлениями\n"
        "👤 Просматривать свой профиль",
        reply_markup=get_main_menu(),
    )


@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer(
        "Используйте кнопки главного меню "
        "для выбора нужного раздела.",
        reply_markup=get_main_menu(),
    )


@router.message(F.text == "🎁 Бонусы")
async def bonuses_handler(message: Message):
    await message.answer(
        "🎁 Просмотр бонусного баланса "
        "появится в следующем модуле."
    )


@router.message(F.text == "🆕 Новинки")
async def news_handler(message: Message):
    await message.answer(
        "🆕 Здесь будут отображаться новинки кофейни."
    )


@router.message(F.text == "🔥 Акции")
async def promotions_handler(message: Message):
    await message.answer(
        "🔥 Здесь будут отображаться актуальные акции."
    )


@router.message(F.text == "🔔 Уведомления")
async def notifications_handler(message: Message):
    await message.answer(
        "🔔 Здесь можно будет управлять подписками."
    )


@router.message(F.text == "👤 Мой профиль")
async def profile_handler(message: Message):
    await message.answer(
        "👤 Здесь будет информация о вашем профиле."
    )
