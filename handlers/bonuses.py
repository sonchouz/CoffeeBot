from aiogram import Router, F
from aiogram.types import Message
from html import escape

from services.mock_client import MockOneCClient


router = Router()
client = MockOneCClient()


@router.message(F.text == "🎁 Бонусы")
async def show_bonuses(message: Message):
    if not message.from_user:
        await message.answer(
            "Не удалось определить пользователя."
        )
        return

    telegram_id = message.from_user.id

    user = await client.get_client(telegram_id)

    if user is None:
        await message.answer(
            "Вы ещё не зарегистрированы в системе."
        )
        return

    await message.answer(
        f"👤 Клиент: {escape(user.name)}\n"
        f"🎁 Бонусный баланс: "
        f"<b>{user.bonus_balance}</b> бонусов"
    )