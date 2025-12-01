import asyncio
import sqlite3
import logging
import os
import sys
from datetime import datetime
from typing import Optional
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.date import DateTrigger

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log', encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Конфигурация
BOT_TOKEN = os.getenv('BOT_TOKEN', '8343415317:AAHBEnbS0fRCDU8s5Si5QLCGYkQV5azIOZI')
CHANNEL_ID = int(os.getenv('CHANNEL_ID', '-1003312644624'))
GROUP_ID = int(os.getenv('GROUP_ID', '-1003302203585'))
ADMINS = [1153580175]

# Инициализация бота, диспетчера и планировщика
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler()

# ==================== КОД БОТА (полная версия) ====================
# Вставьте сюда ВЕСЬ код из предыдущего сообщения, начиная с функции init_databases()
# и заканчивая блоком "if __name__ == "__main__":"
