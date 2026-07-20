# -*- coding: utf-8 -*-
"""
Super Doctor Bot / Бот Super Doctor
------------------------------------------
- Tayyor holatlar ro'yxati (tugmalar) + erkin savolga AI javobi
- 100 ta eng ko'p uchraydigan kasallik (belgilari, davolash, birinchi yordam) — AI orqali
- Eng yaqin kasalxonalarni topish (joylashuv orqali, OpenStreetMap)
- Statistika bo'limi
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
import math
import os

import httpx
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

from conditions import CONDITIONS, EMERGENCY_INFO, DISEASE_LIST
from ai_helper import ask_ai, get_disease_info

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_NAME = "Super Doctor"
ADMIN_ID = os.getenv("ADMIN_ID")
ADMIN_ID = int(ADMIN_ID) if ADMIN_ID else None

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = Router()

# Foydalanuvchi tilini xotirada saqlash: {user_id: "uz"/"ru"}
user_lang: dict[int, str] = {}

# --- Statistika (xotirada, server qayta ishga tushganda 0 ga qaytadi) ---
stats = {
    "users": set(),          # unikal foydalanuvchi id'lari
    "total_messages": 0,     # jami xabarlar soni
    "disease_queries": {},   # {disease_key: count}
    "ai_free_queries": 0,    # erkin savollar soni
    "hospital_searches": 0,  # kasalxona qidiruvlari soni
}

DISEASES_PER_PAGE = 10


class UserState(StatesGroup):
    choosing_language = State()
    main_menu = State()


TEXTS = {
    "choose_lang": "🌐 Tilni tanlang / Выберите язык:",
    "welcome": {
        "uz": (
            f"👋 Assalomu alaykum!\n\n"
            f"Men *{BOT_NAME}*man. Sizga 100 dan ortiq kasallik bo'yicha "
            f"belgilari, davolash va birinchi yordam haqida ma'lumot beraman.\n\n"
            "📋 Quyidagi tugmalardan birini tanlang,\n"
            "✍️ yoki savolingizni to'g'ridan-to'g'ri yozib yuboring — men AI yordamida javob beraman.\n\n"
            "⚠️ *Diqqat:* Men shifokorning o'rnini bosolmayman. Og'ir holatlarda "
            "darhol 103 raqamiga qo'ng'iroq qiling!"
        ),
        "ru": (
            f"👋 Здравствуйте!\n\n"
            f"Я *{BOT_NAME}*. Расскажу вам о симптомах, лечении и первой помощи "
            "при более чем 100 заболеваниях.\n\n"
            "📋 Выберите одну из кнопок ниже,\n"
            "✍️ или напишите свой вопрос напрямую — отвечу с помощью ИИ.\n\n"
            "⚠️ *Внимание:* Я не заменяю врача. В серьёзных случаях "
            "немедленно звоните 103!"
        ),
    },
    "menu_button": {"uz": "📋 Holatlar ro'yxati", "ru": "📋 Список ситуаций"},
    "diseases_button": {"uz": "🩺 Kasalliklar (100+)", "ru": "🩺 Болезни (100+)"},
    "hospital_button": {"uz": "🏥 Eng yaqin kasalxona", "ru": "🏥 Ближайшая больница"},
    "stats_button": {"uz": "📊 Statistika", "ru": "📊 Статистика"},
    "emergency_button": {"uz": "🚨 Favqulodda raqamlar", "ru": "🚨 Экстренные номера"},
    "lang_button": {"uz": "🌐 Tilni almashtirish", "ru": "🌐 Сменить язык"},
    "back_button": {"uz": "⬅️ Orqaga", "ru": "⬅️ Назад"},
    "choose_condition": {
        "uz": "Quyidagi ro'yxatdan holatni tanlang:",
        "ru": "Выберите ситуацию из списка ниже:",
    },
    "choose_disease": {
        "uz": "Kasallikni tanlang (sahifa {page}/{total}):",
        "ru": "Выберите заболевание (страница {page}/{total}):",
    },
    "send_location": {
        "uz": "📍 Eng yaqin kasalxonalarni topish uchun joylashuvingizni yuboring:",
        "ru": "📍 Отправьте свою геолокацию, чтобы найти ближайшие больницы:",
    },
    "location_button": {"uz": "📍 Joylashuvni yuborish", "ru": "📍 Отправить геолокацию"},
    "searching_hospitals": {"uz": "🔍 Qidirilmoqda...", "ru": "🔍 Ищем..."},
    "no_hospitals": {
        "uz": "😕 Yaqin atrofda kasalxona topilmadi. Qidiruv radiusi 10 km edi.",
        "ru": "😕 Поблизости больницы не найдены. Радиус поиска был 10 км.",
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


def main_reply_keyboard(lang: str, is_admin: bool = False) -> ReplyKeyboardMarkup:
    keyboard = [
        [KeyboardButton(text=TEXTS["menu_button"][lang])],
        [KeyboardButton(text=TEXTS["diseases_button"][lang])],
        [KeyboardButton(text=TEXTS["hospital_button"][lang], request_location=True)],
    ]
    if is_admin:
        keyboard.append([
            KeyboardButton(text=TEXTS["emergency_button"][lang]),
            KeyboardButton(text=TEXTS["stats_button"][lang]),
        ])
    else:
        keyboard.append([KeyboardButton(text=TEXTS["emergency_button"][lang])])
    keyboard.append([KeyboardButton(text=TEXTS["lang_button"][lang])])
    return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)


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


def diseases_keyboard(lang: str, page: int = 0) -> InlineKeyboardMarkup:
    total_pages = math.ceil(len(DISEASE_LIST) / DISEASES_PER_PAGE)
    start = page * DISEASES_PER_PAGE
    end = start + DISEASES_PER_PAGE
    page_items = list(enumerate(DISEASE_LIST))[start:end]

    buttons = []
    row = []
    for idx, disease in page_items:
        row.append(InlineKeyboardButton(text=disease[lang], callback_data=f"dz_{idx}"))
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)

    nav_row = []
    if page > 0:
        nav_row.append(InlineKeyboardButton(text="⬅️", callback_data=f"dzpage_{page - 1}"))
    nav_row.append(InlineKeyboardButton(text=f"{page + 1}/{total_pages}", callback_data="noop"))
    if page < total_pages - 1:
        nav_row.append(InlineKeyboardButton(text="➡️", callback_data=f"dzpage_{page + 1}"))
    buttons.append(nav_row)

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_lang(user_id: int) -> str:
    return user_lang.get(user_id, "uz")


def haversine_km(lat1, lon1, lat2, lon2) -> float:
    R = 6371.0
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


async def find_nearby_hospitals(lat: float, lon: float, radius_m: int = 10000, limit: int = 5):
    """OpenStreetMap Overpass API orqali yaqin atrofdagi kasalxonalarni topadi (API kalit shart emas)."""
    query = f"""
    [out:json][timeout:15];
    (
      node["amenity"="hospital"](around:{radius_m},{lat},{lon});
      way["amenity"="hospital"](around:{radius_m},{lat},{lon});
    );
    out center;
    """
    async with httpx.AsyncClient(timeout=20) as client:
        resp = await client.post(
            "https://overpass-api.de/api/interpreter", data={"data": query}
        )
        resp.raise_for_status()
        data = resp.json()

    results = []
    for el in data.get("elements", []):
        el_lat = el.get("lat") or el.get("center", {}).get("lat")
        el_lon = el.get("lon") or el.get("center", {}).get("lon")
        name = el.get("tags", {}).get("name")
        if not (el_lat and el_lon and name):
            continue
        distance = haversine_km(lat, lon, el_lat, el_lon)
        results.append({"name": name, "lat": el_lat, "lon": el_lon, "distance": distance})

    results.sort(key=lambda x: x["distance"])
    return results[:limit]


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.set_state(UserState.choosing_language)
    await message.answer(TEXTS["choose_lang"], reply_markup=lang_keyboard())


@router.callback_query(F.data.startswith("lang_"))
async def set_language(callback: CallbackQuery, state: FSMContext):
    lang = callback.data.split("_")[1]
    user_lang[callback.from_user.id] = lang
    stats["users"].add(callback.from_user.id)
    await state.set_state(UserState.main_menu)
    await callback.message.edit_text(TEXTS["welcome"][lang], parse_mode="Markdown")
    await callback.message.answer(
        TEXTS["choose_condition"][lang],
        reply_markup=main_reply_keyboard(lang, is_admin=(callback.from_user.id == ADMIN_ID)),
    )
    await callback.answer()


@router.message(Command("menu"))
@router.message(F.text.in_([TEXTS["menu_button"]["uz"], TEXTS["menu_button"]["ru"]]))
async def show_menu(message: Message):
    lang = get_lang(message.from_user.id)
    await message.answer(
        TEXTS["choose_condition"][lang], reply_markup=conditions_keyboard(lang)
    )


@router.message(F.text.in_([TEXTS["diseases_button"]["uz"], TEXTS["diseases_button"]["ru"]]))
async def show_diseases(message: Message):
    lang = get_lang(message.from_user.id)
    total_pages = math.ceil(len(DISEASE_LIST) / DISEASES_PER_PAGE)
    text = TEXTS["choose_disease"][lang].format(page=1, total=total_pages)
    await message.answer(text, reply_markup=diseases_keyboard(lang, 0))


@router.callback_query(F.data == "noop")
async def noop_callback(callback: CallbackQuery):
    await callback.answer()


@router.callback_query(F.data.startswith("dzpage_"))
async def paginate_diseases(callback: CallbackQuery):
    lang = get_lang(callback.from_user.id)
    page = int(callback.data.replace("dzpage_", ""))
    total_pages = math.ceil(len(DISEASE_LIST) / DISEASES_PER_PAGE)
    text = TEXTS["choose_disease"][lang].format(page=page + 1, total=total_pages)
    await callback.message.edit_text(text, reply_markup=diseases_keyboard(lang, page))
    await callback.answer()


@router.callback_query(F.data.startswith("dz_"))
async def show_disease_info(callback: CallbackQuery):
    lang = get_lang(callback.from_user.id)
    idx = int(callback.data.replace("dz_", ""))
    if idx >= len(DISEASE_LIST):
        await callback.answer()
        return

    disease = DISEASE_LIST[idx]
    disease_name = disease[lang]

    await callback.answer(TEXTS["ai_thinking"][lang])
    thinking_msg = await callback.message.answer(TEXTS["ai_thinking"][lang])

    stats["total_messages"] += 1
    stats["disease_queries"][disease["key"]] = stats["disease_queries"].get(disease["key"], 0) + 1

    try:
        info = await get_disease_info(disease_name, lang)
        full_text = f"🩺 *{disease_name}*\n\n{info}"
        await thinking_msg.edit_text(full_text, parse_mode="Markdown")
    except Exception as e:
        logger.error(f"Disease info error: {e}")
        error_text = {
            "uz": "❌ Kechirasiz, hozir ma'lumot olib bo'lmadi. Keyinroq urinib ko'ring.",
            "ru": "❌ Извините, не удалось получить информацию. Попробуйте позже.",
        }
        await thinking_msg.edit_text(error_text[lang])


@router.message(F.text.in_([TEXTS["emergency_button"]["uz"], TEXTS["emergency_button"]["ru"]]))
async def show_emergency(message: Message):
    lang = get_lang(message.from_user.id)
    await message.answer(EMERGENCY_INFO[lang], parse_mode="Markdown")


@router.message(Command("id"))
async def show_my_id(message: Message):
    await message.answer(f"🆔 Sizning Telegram ID: `{message.from_user.id}`", parse_mode="Markdown")


@router.message(F.text.in_([TEXTS["stats_button"]["uz"], TEXTS["stats_button"]["ru"]]))
async def show_stats(message: Message):
    lang = get_lang(message.from_user.id)

    if ADMIN_ID is None or message.from_user.id != ADMIN_ID:
        denied = {
            "uz": "⛔ Bu bo'lim faqat admin uchun.",
            "ru": "⛔ Этот раздел только для администратора.",
        }
        await message.answer(denied[lang])
        return

    top_diseases = sorted(stats["disease_queries"].items(), key=lambda x: x[1], reverse=True)[:5]
    top_text_lines = []
    for key, count in top_diseases:
        name = next((d[lang] for d in DISEASE_LIST if d["key"] == key), key)
        top_text_lines.append(f"  • {name} — {count}")
    top_text = "\n".join(top_text_lines) if top_text_lines else "  —"

    if lang == "uz":
        text = (
            "📊 *Bot statistikasi:*\n\n"
            f"👥 Foydalanuvchilar soni: {len(stats['users'])}\n"
            f"💬 Jami xabarlar: {stats['total_messages']}\n"
            f"🏥 Kasalxona qidiruvlari: {stats['hospital_searches']}\n"
            f"✍️ Erkin savollar: {stats['ai_free_queries']}\n\n"
            f"🔝 *Eng ko'p so'ralgan kasalliklar:*\n{top_text}\n\n"
            "_Eslatma: statistika server qayta ishga tushganda nolga qaytadi._"
        )
    else:
        text = (
            "📊 *Статистика бота:*\n\n"
            f"👥 Пользователей: {len(stats['users'])}\n"
            f"💬 Всего сообщений: {stats['total_messages']}\n"
            f"🏥 Поисков больниц: {stats['hospital_searches']}\n"
            f"✍️ Свободных вопросов: {stats['ai_free_queries']}\n\n"
            f"🔝 *Самые частые запросы:*\n{top_text}\n\n"
            "_Примечание: статистика сбрасывается при перезапуске сервера._"
        )
    await message.answer(text, parse_mode="Markdown")


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


# Joylashuv yuborilganda — eng yaqin kasalxonalarni qidirish
@router.message(F.location)
async def handle_location(message: Message):
    lang = get_lang(message.from_user.id)
    stats["hospital_searches"] += 1
    searching_msg = await message.answer(TEXTS["searching_hospitals"][lang])

    try:
        hospitals = await find_nearby_hospitals(
            message.location.latitude, message.location.longitude
        )
        if not hospitals:
            await searching_msg.edit_text(TEXTS["no_hospitals"][lang])
            return

        lines = ["🏥 " + ("Eng yaqin kasalxonalar:" if lang == "uz" else "Ближайшие больницы:"), ""]
        for h in hospitals:
            maps_link = f"https://www.google.com/maps/dir/?api=1&destination={h['lat']},{h['lon']}"
            dist_text = f"{h['distance']:.1f} km"
            lines.append(f"📍 *{h['name']}* — {dist_text}\n[{'Yo\u02bcnalish' if lang=='uz' else 'Маршрут'}]({maps_link})\n")

        await searching_msg.edit_text(
            "\n".join(lines), parse_mode="Markdown", disable_web_page_preview=True
        )
    except Exception as e:
        logger.error(f"Hospital search error: {e}")
        error_text = {
            "uz": "❌ Kasalxonalarni qidirishda xatolik yuz berdi. Keyinroq urinib ko'ring.",
            "ru": "❌ Ошибка при поиске больниц. Попробуйте позже.",
        }
        await searching_msg.edit_text(error_text[lang])


# Erkin matn — AI orqali javob
@router.message(F.text)
async def handle_free_text(message: Message):
    lang = get_lang(message.from_user.id)
    stats["total_messages"] += 1
    stats["ai_free_queries"] += 1
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

    logger.info(f"{BOT_NAME} ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
