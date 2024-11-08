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
from run_bot import bot

rt = Router()

@rt.message(Command("start"))
async def start(message: Message, state: FSMContext):
    await message.answer("Здрасте. Что будем делать?", reply_markup=kb.start_kb)


async def get_chat_id(username):
    chat = await bot.get_chat(username)
    chat_id = chat.id
    return chat_id


async def send_notification(debtor, lender_tg, event_name, event_date):
        await rt.send_message(chat_id=await get_chat_id(debtor), text='Hello')