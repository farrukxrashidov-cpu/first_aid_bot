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
