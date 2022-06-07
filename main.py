from aiogram import Bot, Dispatcher, executor
from config.personal_data import BOT_TOKEN
import asyncio
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from db.create_tables import create_tables
from config.crypto_rsa import create_rsa_keys
from trading.get_securities import get_security_list
from trading.place_order import buy_order

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop, storage=MemoryStorage())



if __name__ == "__main__":

    from main import dp
    from bot.handlers.bot_handlers import start

    create_tables()
    create_rsa_keys()

    executor.start_polling(dp, on_startup=start)

