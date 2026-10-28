#Точка запуска бота
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramNetworkError

from config import BOT_TOKEN
from handlers.start import router as start_router


async def main():
    logging.basicConfig(level=logging.INFO)


    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        ),
    )

    dp = Dispatcher()
    dp.include_router(start_router)

    try:
        print("Проверка подключения к Telegram...")

        me = await bot.get_me()
        print(f"Подключение успешно: @{me.username}")

        await bot.delete_webhook(
            drop_pending_updates=True
        )

        print("Бот запущен!")
        await dp.start_polling(bot)

    except TelegramNetworkError as e:
        print("Ошибка подключения к Telegram API:")
        print(e)

    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
