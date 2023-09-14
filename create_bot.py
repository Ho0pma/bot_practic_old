from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()
bot = Bot('5969077198:AAHIeM4PfeH3ZmsU8h90tsb1BXuS0S5at_o')
dp = Dispatcher(bot, storage=storage)
