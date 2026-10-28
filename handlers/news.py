from aiogram import Router, F
from aiogram.types import Message
from html import escape

from services.mock_client import MockOneCClient


router = Router()
client = MockOneCClient()


@router.message(F.text == "🆕 Новинки")
async def show_news(message: Message):
    products = await client.get_new_products()

    if not products:
        await message.answer("Пока новинок нет.")
        return

    text = "🆕 <b>Новинки кофейни</b>\n\n"

    for product in products:
        text += (
            f"☕ <b>{escape(product.name)}</b>\n"
            f"{escape(product.description)}\n"
            f"Цена: {product.price:.2f} ₽\n\n"
        )

    await message.answer(text)