from aiogram import Router, F
from aiogram.types import Message
from html import escape

from services.mock_client import MockOneCClient


router = Router()
client = MockOneCClient()


@router.message(F.text == "🔥 Акции")
async def show_promotions(message: Message):
    promotions = await client.get_promotions()

    if not promotions:
        await message.answer("Сейчас активных акций нет.")
        return

    text = "🔥 <b>Актуальные акции</b>\n\n"

    for promotion in promotions:
        text += (
            f"🎉 <b>{escape(promotion.title)}</b>\n"
            f"{escape(promotion.description)}\n"
            f"Скидка: {promotion.discount_percent}%\n\n"
        )

    await message.answer(text)