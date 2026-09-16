import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)
from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand

from apps.models import TelegramUser

dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="📱 Raqamni ulashish", request_contact=True)]],
        resize_keyboard=True,
    )
    await message.answer(
        "Ro'yxatdan o'tish uchun telefon raqamingizni ulashing:",
        reply_markup=keyboard,
    )


@dp.message(F.contact)
async def contact_handler(message: Message):
    await sync_to_async(TelegramUser.objects.update_or_create)(
        telegram_id=message.from_user.id,
        defaults={
            "full_name": message.from_user.full_name,
            "username": message.from_user.username,
            "phone_number": message.contact.phone_number,
        },
    )
    await message.answer("✅ Ma'lumotlar saqlandi", reply_markup=ReplyKeyboardRemove())


class Command(BaseCommand):
    help = "Telegram botni polling rejimida ishga tushiradi"

    def handle(self, *args, **options):
        bot = Bot(token=os.getenv("BOT_TOKEN"))
        asyncio.run(dp.start_polling(bot))