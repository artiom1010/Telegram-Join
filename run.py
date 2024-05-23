# Рабочий скрипт для бота админа, который отправляет оператору имя пользователя, который обратился к боту
import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TOKEN, YOUR_CHAT_ID

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def send_notification(chat_id, user):
    await bot.send_message(chat_id, f'Пользователь {user.full_name} приглашен')


@dp.message(CommandStart())
async def cmd_start(message: Message):
    # await message.reply(f"Привет!\nID нашего клуба: {'778899'}\nID приглашения: {'123456'}\nCcылка приглашения: {'ссылка на приложение'}\nХотите ли выигрывать деньги в покер?")

    await send_notification(YOUR_CHAT_ID, message.from_user)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # asyncio.run(main())
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')










# import asyncio
# import logging

# from aiogram import Bot, Dispatcher
# from aiogram.filters import CommandStart
# from aiogram.types import Message

# from config import TOKEN, YOUR_CHAT_ID

# bot = Bot(token=TOKEN)
# dp = Dispatcher()

# @dp.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.reply(f"Привет!\nID нашего клуба: {'778899'}\nID приглашения: {'123456'}\nCcылка приглашения: {'ссылка на приложение'}\nХотите ли выигрывать деньги в покер?")



# async def main():
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     # asyncio.run(main())
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print('Exit')