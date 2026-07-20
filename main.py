# -*- coding: utf-8 -*-
"""
Birinchi Yordam Boti / Бот Первой Помощи
------------------------------------------
- Tayyor holatlar ro'yxati (tugmalar) + erkin savolga AI javobi
- UZ / RU til qo'llab-quvvatlash
- Kutubxona: aiogram 3.x
- AI: Anthropic Claude API

O'RNATISH:
    pip install -r requirements.txt

ISHGA TUSHIRISH:
    1. .env faylini to'ldiring (BOT_TOKEN va ANTHROPIC_API_KEY)
    2. python main.py
"""

import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

from conditions import CONDITIONS, EMERGENCY_INFO
from ai_helper import ask_ai

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = Router()

# Foydalanuvchi tilini xotirada saqlash: {user_id: "uz"/"ru"}
user_lang: dict[int, str] = {}


class UserState(StatesGroup):
    choosing_language = State()
    main_menu = State()


TEXTS = {
    "choose_lang": "🌐 Tilni tanlang / Выберите язык:",
    "welcome": {
        "uz": (
            "👋 Assalomu alaykum!\n\n"
            "Men *Birinchi Yordam Boti*man. Sizga turli holatlarda birinchi tibbiy "
            "yordam bo'yicha ma'lumot beraman.\n\n"
            "📋 Quyidagi ro'yxatdan holatni tanlashingiz mumkin,\n"
            "✍️ yoki savolingizni to'g'ridan-to'g'ri yozib yuboring — men AI yordamida javob beraman.\n\n"
            "⚠️ *Diqqat:* Men shifokorning o'rnini bosolmayman. Og'ir holatlarda "
            "darhol 103 raqamiga qo'ng'iroq qiling!"
        ),
        "ru": (
            "👋 Здравствуйте!\n\n"
            "Я *Бот Первой Помощи*. Расскажу вам о первой медицинской помощи "
            "при различных ситуациях.\n\n"
            "📋 Вы можете выбрать ситуацию из списка ниже,\n"
            "✍️ или написать свой вопрос напрямую — отвечу с помощью ИИ.\n\n"
            "⚠️ *Внимание:* Я не заменяю врача. В серьёзных случаях "
            "немедленно звоните 103!"
        ),
    },
    "menu_button": {"uz": "📋 Holatlar ro'yxati", "ru": "📋 Список ситуаций"},
    "emergency_button": {"uz": "🚨 Favqulodda raqamlar", "ru": "🚨 Экстренные номера"},
    "lang_button": {"uz": "🌐 Tilni almashtirish", "ru": "🌐 Сменить язык"},
    "back_button": {"uz": "⬅️ Orqaga", "ru": "⬅️ Назад"},
    "choose_condition": {
        "uz": "Quyidagi ro'yxatdan holatni tanlang:",
        "ru": "Выберите ситуацию из списка ниже:",
    },
    "ai_thinking": {"uz": "🤔 O'ylanyapman...", "ru": "🤔 Думаю..."},
    "ai_disclaimer": {
        "uz": "\n\n⚠️ _Bu AI tomonidan berilgan umumiy ma'lumot, shifokor tashxisi emas. Og'ir holatda 103 ga qo'ng'iroq qiling._",
        "ru": "\n\n⚠️ _Это общая информация от ИИ, а не диагноз врача. В серьёзной ситуации звоните 103._",
    },
}


def lang_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="lang_uz"),
                InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
            ]
        ]
    )


def main_reply_keyboard(lang: str) -> ReplyKeyboardMarkup:
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=TEXTS["menu_button"][lang])],
            [
                KeyboardButton(text=TEXTS["emergency_button"][lang]),
                KeyboardButton(text=TEXTS["lang_button"][lang]),
            ],
        ],
        resize_keyboard=True,
    )


def conditions_keyboard(lang: str) -> InlineKeyboardMarkup:
    buttons = []
    row = []
    for key, data in CONDITIONS.items():
        row.append(InlineKeyboardButton(text=data["title"][lang], callback_data=f"cond_{key}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_lang(user_id: int) -> str:
    return user_lang.get(user_id, "uz")


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(UserState.choosing_language)
    await message.answer(TEXTS["choose_lang"], reply_markup=lang_keyboard())


@router.callback_query(F.data.startswith("lang_"))
async def set_language(callback: CallbackQuery, state: FSMContext):
    lang = callback.data.split("_")[1]
    user_lang[callback.from_user.id] = lang
    await state.set_state(UserState.main_menu)
    await callback.message.edit_text(TEXTS["welcome"][lang], parse_mode="Markdown")
    await callback.message.answer(
        TEXTS["choose_condition"][lang], reply_markup=main_reply_keyboard(lang)
    )
    await callback.answer()


@router.message(Command("menu"))
@router.message(F.text.in_([TEXTS["menu_button"]["uz"], TEXTS["menu_button"]["ru"]]))
async def show_menu(message: Message):
    lang = get_lang(message.from_user.id)
    await message.answer(
        TEXTS["choose_condition"][lang], reply_markup=conditions_keyboard(lang)
    )


@router.message(F.text.in_([TEXTS["emergency_button"]["uz"], TEXTS["emergency_button"]["ru"]]))
async def show_emergency(message: Message):
    lang = get_lang(message.from_user.id)
    await message.answer(EMERGENCY_INFO[lang], parse_mode="Markdown")


@router.message(F.text.in_([TEXTS["lang_button"]["uz"], TEXTS["lang_button"]["ru"]]))
async def change_language(message: Message, state: FSMContext):
    await state.set_state(UserState.choosing_language)
    await message.answer(TEXTS["choose_lang"], reply_markup=lang_keyboard())


@router.callback_query(F.data.startswith("cond_"))
async def show_condition(callback: CallbackQuery):
    lang = get_lang(callback.from_user.id)
    key = callback.data.replace("cond_", "")
    condition = CONDITIONS.get(key)
    if condition:
        await callback.message.answer(condition["text"][lang], parse_mode="Markdown")
    await callback.answer()


@router.message(Command("emergency"))
async def emergency_cmd(message: Message):
    lang = get_lang(message.from_user.id)
    await message.answer(EMERGENCY_INFO[lang], parse_mode="Markdown")


# Erkin matn — AI orqali javob
@router.message(F.text)
async def handle_free_text(message: Message):
    lang = get_lang(message.from_user.id)
    thinking_msg = await message.answer(TEXTS["ai_thinking"][lang])

    try:
        ai_response = await ask_ai(message.text, lang)
        full_response = ai_response + TEXTS["ai_disclaimer"][lang]
        await thinking_msg.edit_text(full_response, parse_mode="Markdown")
    except Exception as e:
        logger.error(f"AI error: {e}")
        error_text = {
            "uz": "❌ Kechirasiz, hozir javob berolmayapman. Keyinroq urinib ko'ring yoki /menu dan foydalaning.",
            "ru": "❌ Извините, сейчас не могу ответить. Попробуйте позже или используйте /menu.",
        }
        await thinking_msg.edit_text(error_text[lang])


async def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN topilmadi! .env faylini tekshiring.")

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    logger.info("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
