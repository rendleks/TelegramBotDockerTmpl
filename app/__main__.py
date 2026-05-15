import asyncio
import logging
from datetime import datetime
from pathlib import Path

from aiogram import Bot, Dispatcher
from aiogram import types

from app import TOKEN

dp = Dispatcher()

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(
        f'Я бот. Приятно познакомиться, {message.from_user.first_name}'
    )


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def text_reply(message: types.Message):
    if message.text.lower() == 'привет':
        await message.answer('Привет!')
    else:
        await message.answer('Не понимаю, что это значит...')


async def main():
    log_name = f'logs/{datetime.now().strftime("%Y-%m-%d")}.log'
    Path(log_name).parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        filename=log_name,
        filemode="a"
    )
    
    bot = Bot(token=TOKEN)
    
    print("Starting bot...")
    try:
        await dp.start_polling(bot)
    finally:
        print("Bot stopped")


if __name__ == '__main__':
    asyncio.run(main())
