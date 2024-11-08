from aiogram import Bot, Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import keyboards as kb
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from typing import Optional
from aiogram.filters.callback_data import CallbackData
from collections import defaultdict

rt = Router()

@rt.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer("Здрасте. Что будем делать?", reply_markup=kb.start_kb)