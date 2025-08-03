import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.utils.exceptions import TelegramAPIError

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

async def send_eth_update():
    try:
        # Здесь логика для получения цены ETH, упрощенно:
        price = 3450  # Пример, замените на актуальную логику
        await bot.send_message(CHAT_ID, f"Текущая цена ETH: ${price}")
    except TelegramAPIError as e:
        print(f"Ошибка Telegram API: {e}")

async def scheduler():
    while True:
        await send_eth_update()
        await asyncio.sleep(3 * 60 * 60)  # Каждые 3 часа

async def main():
    await scheduler()

if __name__ == "__main__":
    asyncio.run(main())
 
