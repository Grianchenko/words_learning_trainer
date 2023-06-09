from . local_settings import API_KEY
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(token=API_KEY, parse_mode='html')
dp = Dispatcher(bot, storage=MemoryStorage())
