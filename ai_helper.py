# -*- coding: utf-8 -*-
"""
Claude API bilan bog'lanish uchun yordamchi modul.
Foydalanuvchi erkin savol yozganda shu yerdan javob olinadi.
"""

import os
from anthropic import AsyncAnthropic

client = AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = {
    "uz": (
        "Sen tibbiy birinchi yordam bo'yicha ma'lumot beruvchi yordamchisan. "
        "Foydalanuvchi biror kasallik, jarohat yoki holat haqida so'raganda, "
        "unga umumiy, xavfsiz va amaliy birinchi yordam bo'yicha ko'rsatmalar ber. "
        "Javobni o'zbek tilida, qisqa va tushunarli qismlarga bo'lib, raqamlangan "
        "qadamlar shaklida yoz. Og'ir yoki hayotga xavfli holatlarda albatta "
        "103 raqamiga (tez yordam) qo'ng'iroq qilishni tavsiya qil. "
        "Aniq dori dozasi yoki retsept talab qiladigan tavsiyalar berma — "
        "buning o'rniga shifokorga murojaat qilishni tavsiya qil. "
        "Sen shifokor emassan va tashxis qo'ymaysan, faqat umumiy yo'l-yo'riq berasan."
    ),
    "ru": (
        "Ты помощник, предоставляющий информацию о первой медицинской помощи. "
        "Когда пользователь спрашивает о болезни, травме или состоянии, "
        "дай общие, безопасные и практичные рекомендации по первой помощи. "
        "Отвечай на русском языке, коротко и понятно, в виде пронумерованных шагов. "
        "В серьёзных или опасных для жизни ситуациях обязательно рекомендуй "
        "немедленно звонить 103 (скорая помощь). "
        "Не давай точных дозировок лекарств или рецептурных рекомендаций — "
        "вместо этого советуй обратиться к врачу. "
        "Ты не врач и не ставишь диагноз, а даёшь только общие рекомендации."
    ),
}


DISEASE_INFO_PROMPT = {
    "uz": (
        "Sen tibbiy ma'lumot beruvchi yordamchisan. Foydalanuvchi berilgan kasallik nomi "
        "haqida to'liq, tuzilgan ma'lumot so'raydi. Javobni aynan shu formatda ber (o'zbek tilida):\n\n"
        "📋 *Ta'rifi:* (1-2 gap bilan qisqacha)\n\n"
        "🔍 *Belgilari:* (3-6 ta asosiy belgi, ro'yxat ko'rinishida)\n\n"
        "🚑 *Birinchi yordam:* (agar tegishli bo'lsa, uy sharoitida qilinadigan birinchi qadamlar)\n\n"
        "💊 *Davolash:* (umumiy davolash yondashuvi, aniq dori nomi yoki dozasi bermang, shifokorga murojaat qilishni tavsiya qiling)\n\n"
        "Javob qisqa, aniq va tushunarli bo'lsin. Oxirida albatta shifokorga murojaat qilish "
        "tavsiyasini qo'shing. Sen shifokor emassan, tashxis qo'ymaysan."
    ),
    "ru": (
        "Ты медицинский информационный помощник. Пользователь просит полную, структурированную "
        "информацию о названной болезни. Ответь строго в этом формате (на русском языке):\n\n"
        "📋 *Описание:* (кратко, 1-2 предложения)\n\n"
        "🔍 *Симптомы:* (3-6 основных симптомов, списком)\n\n"
        "🚑 *Первая помощь:* (если применимо, что можно сделать в домашних условиях)\n\n"
        "💊 *Лечение:* (общий подход к лечению, без точных названий лекарств или дозировок, "
        "рекомендуй обратиться к врачу)\n\n"
        "Ответ должен быть коротким, точным и понятным. В конце обязательно добавь рекомендацию "
        "обратиться к врачу. Ты не врач и не ставишь диагноз."
    ),
}


async def get_disease_info(disease_name: str, lang: str = "uz") -> str:
    """
    Berilgan kasallik nomi bo'yicha AI orqali tuzilgan ma'lumot oladi
    (ta'rifi, belgilari, birinchi yordam, davolash).
    """
    system_prompt = DISEASE_INFO_PROMPT.get(lang, DISEASE_INFO_PROMPT["uz"])

    response = await client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=800,
        system=system_prompt,
        messages=[{"role": "user", "content": disease_name}],
    )

    text_parts = [block.text for block in response.content if block.type == "text"]
    return "\n".join(text_parts) if text_parts else (
        "Kechirasiz, ma'lumot topilmadi." if lang == "uz" else "Извините, информация не найдена."
    )


async def ask_ai(user_question: str, lang: str = "uz") -> str:
    """
    Foydalanuvchi savoliga Claude API orqali javob oladi.
    """
    system_prompt = SYSTEM_PROMPT.get(lang, SYSTEM_PROMPT["uz"])

    response = await client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=800,
        system=system_prompt,
        messages=[{"role": "user", "content": user_question}],
    )

    # Javobdagi matn qismlarini yig'ish
    text_parts = [block.text for block in response.content if block.type == "text"]
    return "\n".join(text_parts) if text_parts else (
        "Kechirasiz, javob topilmadi." if lang == "uz" else "Извините, ответ не найден."
    )
