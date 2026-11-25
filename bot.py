import asyncio, os
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = os.getenv("BOT_TOKEN")
ADMIN = "Gigi_bro"
P1 = "40 000 so'm"
P6 = "290 000 so'm"

bot = Bot(token=TOKEN)
dp = Dispatcher()

def main_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="⭐ 1 oylik obuna", callback_data="m1")
    kb.button(text="⭐ 6 oylik obuna", callback_data="m6")
    kb.button(text="💰 Narx", callback_data="price")
    kb.adjust(1)
    return kb.as_markup()

def buy_menu():
    kb = InlineKeyboardBuilder()
    kb.button(text="✅ Sotib olish", url=f"https://t.me/{ADMIN}")
    kb.button(text="⬅️ Orqaga", callback_data="back")
    kb.adjust(1)
    return kb.as_markup()

@dp.message(CommandStart())
async def start(m: types.Message):
    await m.answer(
        "Telegram Premium xizmati 👇\nKerakli bo'limni tanlang:",
        reply_markup=main_menu(),
    )

@dp.callback_query(F.data == "m1")
async def m1(c: types.CallbackQuery):
    await c.message.edit_text(
        f"⭐ 1 oylik Premium\nNarxi: {P1}\n\nSotib olish uchun tugmani bosing 👇",
        reply_markup=buy_menu(),
    )
    await c.answer()

@dp.callback_query(F.data == "m6")
async def m6(c: types.CallbackQuery):
    await c.message.edit_text(
        f"⭐ 6 oylik Premium\nNarxi: {P6}\n\nSotib olish uchun tugmani bosing 👇",
        reply_markup=buy_menu(),
    )
    await c.answer()

@dp.callback_query(F.data == "price")
async def price(c: types.CallbackQuery):
    await c.message.edit_text(
        f"💰 Narxlar:\n\n1 oy: {P1}\n6 oy: {P6}",
        reply_markup=buy_menu(),
    )
    await c.answer()

@dp.callback_query(F.data == "back")
async def back(c: types.CallbackQuery):
    await c.message.edit_text("Kerakli bo'limni tanlang:", reply_markup=main_menu())
    await c.answer()

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
