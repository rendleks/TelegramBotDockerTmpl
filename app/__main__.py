import asyncio
import logging
from datetime import datetime
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram import types

from app import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()



async def main():
    log_name = f'logs/{datetime.now().strftime("%Y-%m-%d")}.log'
    Path(log_name).parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        filename=log_name,
        filemode="a"
    )

    token = getenv("BOT_TOKEN")
    if not token:      
        error = "No token provided"
        raise ValueError(error)    
    bot = Bot(token=token)
    
    print("Starting bot...")
    try:
        await dp.start_polling(bot)
    finally:
        print("Bot stopped")


if __name__ == '__main__':
    asyncio.run(main())
