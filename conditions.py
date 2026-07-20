# -*- coding: utf-8 -*-
"""
Eng ko'p uchraydigan holatlar uchun birinchi yordam bazasi (UZ / RU).
Har bir holat: nomi va bosqichma-bosqich yo'riqnoma.
"""

CONDITIONS = {
    "burn": {
        "title": {"uz": "🔥 Kuyish", "ru": "🔥 Ожог"},
        "text": {
            "uz": (
                "🔥 *Kuyish uchun birinchi yordam:*\n\n"
                "1. Kuygan joyni 10-15 daqiqa sovuq (lekin muzdek emas) suv ostida ushlang.\n"
                "2. Kiyim yopishib qolgan bo'lsa, yechishga urinmang.\n"
                "3. Pufakchalarni yorMang.\n"
                "4. Kuygan joyni toza, quruq mato bilan yoping.\n"
                "5. Yog', tishlar pastasi yoki xalq usullarini ishlatMang.\n\n"
                "⚠️ Kuyish katta maydonni egallasa yoki chuqur bo'lsa — darhol 103 ga qo'ng'iroq qiling."
            ),
            "ru": (
                "🔥 *Первая помощь при ожоге:*\n\n"
                "1. Держите обожжённое место под прохладной (не ледяной) водой 10-15 минут.\n"
                "2. Не пытайтесь снять прилипшую одежду.\n"
                "3. Не прокалывайте волдыри.\n"
                "4. Накройте ожог чистой сухой тканью.\n"
                "5. Не используйте масло, зубную пасту или народные средства.\n\n"
                "⚠️ Если ожог обширный или глубокий — немедленно звоните 103."
            ),
        },
    },
    "bleeding": {
        "title": {"uz": "🩸 Qon ketishi", "ru": "🩸 Кровотечение"},
        "text": {
            "uz": (
                "🩸 *Qon ketishida birinchi yordam:*\n\n"
                "1. Qo'lingizni yuving yoki qo'lqop kiying (imkon bo'lsa).\n"
                "2. Toza mato yoki bint bilan yaraga kuchli bosim bering.\n"
                "3. Jarohatlangan a'zoni yurakdan yuqoriroq ko'taring.\n"
                "4. Bosimni to'xtatmang, mato qonga to'lsa ustiga yana qo'shing.\n"
                "5. Qon to'xtamasa yoki juda kuchli bo'lsa — darhol 103 ga qo'ng'iroq qiling.\n\n"
                "⚠️ Jism yaraga sanchilib qolgan bo'lsa — uni sug'urib olMang."
            ),
            "ru": (
                "🩸 *Первая помощь при кровотечении:*\n\n"
                "1. Вымойте руки или наденьте перчатки (если есть).\n"
                "2. Сильно прижмите чистую ткань или бинт к ране.\n"
                "3. Приподнимите повреждённую конечность выше уровня сердца.\n"
                "4. Не прекращайте давление, при необходимости добавляйте новую ткань поверх.\n"
                "5. Если кровь не останавливается или кровотечение сильное — звоните 103.\n\n"
                "⚠️ Если в ране застрял предмет — не вытаскивайте его."
            ),
        },
    },
    "fracture": {
        "title": {"uz": "🦴 Suyak sinishi", "ru": "🦴 Перелом"},
        "text": {
            "uz": (
                "🦴 *Suyak sinishida birinchi yordam:*\n\n"
                "1. Jarohatlangan qismni harakatlantirMang.\n"
                "2. Imkon bo'lsa, uni taxta yoki qattiq material bilan mahkamlab, harakatsiz holga keltiring.\n"
                "3. Sovuq narsa (muz, mato bilan o'ralgan) qo'ying — shishni kamaytiradi.\n"
                "4. Sinish ochiq bo'lsa (suyak ko'rinib tursa), yarani toza mato bilan yoping, tekislashga urinMang.\n"
                "5. Tez yordam chaqiring — 103.\n\n"
                "⚠️ Boshqa jarohat bo'lmasa ham, kishini o'zi yurishga majburlaMang."
            ),
            "ru": (
                "🦴 *Первая помощь при переломе:*\n\n"
                "1. Не двигайте повреждённую часть тела.\n"
                "2. По возможности зафиксируйте её шиной или твёрдым материалом.\n"
                "3. Приложите что-то холодное (лёд, завёрнутый в ткань) — уменьшит отёк.\n"
                "4. Если перелом открытый (видна кость) — накройте рану чистой тканью, не пытайтесь выпрямить.\n"
                "5. Вызовите скорую — 103.\n\n"
                "⚠️ Не заставляйте человека ходить самостоятельно."
            ),
        },
    },
    "choking": {
        "title": {"uz": "😮‍💨 Bo'g'ilish (tomoqqa narsa tiqilishi)", "ru": "😮‍💨 Удушье (инородное тело)"},
        "text": {
            "uz": (
                "😮‍💨 *Bo'g'ilishda birinchi yordam (Geymlix usuli):*\n\n"
                "1. Kishi gapira olmasa yoki nafas ololmasa — orqasiga o'ting.\n"
                "2. Bir qo'lni musht qilib, kindik va ko'krak suyagi orasiga qo'ying.\n"
                "3. Ikkinchi qo'l bilan mushtni ushlab, ichkariga va yuqoriga qarab keskin siqing.\n"
                "4. Narsa chiqquncha yoki tez yordam kelguncha takrorlang.\n"
                "5. Chaqaloqlar uchun — boshini pastga qaratib, yelka orasiga yengil urish kerak (kattalar usuli emas).\n\n"
                "⚠️ Darhol 103 ga qo'ng'iroq qiling yoki qiling deb so'rang."
            ),
            "ru": (
                "😮‍💨 *Первая помощь при удушье (приём Геймлиха):*\n\n"
                "1. Если человек не может говорить или дышать — встаньте сзади него.\n"
                "2. Сожмите кулак и поместите его между пупком и грудиной.\n"
                "3. Обхватите кулак второй рукой и резко надавите внутрь и вверх.\n"
                "4. Повторяйте, пока предмет не выйдет или не приедет скорая.\n"
                "5. Для младенцев — метод другой: похлопывания по спине с опущенной головой.\n\n"
                "⚠️ Немедленно звоните 103 или попросите кого-то это сделать."
            ),
        },
    },
    "heart_attack": {
        "title": {"uz": "❤️‍🩹 Yurak xuruji belgilari", "ru": "❤️‍🩹 Признаки сердечного приступа"},
        "text": {
            "uz": (
                "❤️‍🩹 *Yurak xurujida birinchi yordam:*\n\n"
                "1. Darhol 103 ga qo'ng'iroq qiling.\n"
                "2. Kishini qulay o'tirg'izing, tor kiyimlarini bo'shating.\n"
                "3. Agar shifokor tomonidan buyurilgan bo'lsa, aspirin chaynatib berish mumkin (allergiyasi yo'qligiga ishonch hosil qiling).\n"
                "4. Kishini yolg'iz qoldirMang, holatini kuzatib turing.\n"
                "5. Hushidan ketsa va nafas olmasa — yurak-o'pka reanimatsiyasini (CPR) boshlang.\n\n"
                "⚠️ Belgilari: ko'krakda og'riq/bosim, chap qo'l/jag'ga tarqalish, nafas qisilishi, sovuq ter."
            ),
            "ru": (
                "❤️‍🩹 *Первая помощь при сердечном приступе:*\n\n"
                "1. Немедленно звоните 103.\n"
                "2. Усадите человека в удобное положение, ослабьте тесную одежду.\n"
                "3. Если назначено врачом, можно дать разжевать аспирин (убедитесь в отсутствии аллергии).\n"
                "4. Не оставляйте человека одного, следите за состоянием.\n"
                "5. Если потерял сознание и не дышит — начните СЛР (сердечно-лёгочную реанимацию).\n\n"
                "⚠️ Симптомы: боль/давление в груди, отдающая в руку/челюсть, одышка, холодный пот."
            ),
        },
    },
    "fainting": {
        "title": {"uz": "😵 Hushidan ketish", "ru": "😵 Обморок"},
        "text": {
            "uz": (
                "😵 *Hushidan ketishda birinchi yordam:*\n\n"
                "1. Kishini yerga yotqizing, oyoqlarini biroz ko'tarib qo'ying.\n"
                "2. Tor kiyimlarini bo'shating, havo yetkazing.\n"
                "3. Hushiga kelgach, sekin-asta o'tirgizib, suv bering.\n"
                "4. 1-2 daqiqada hushiga kelmasa yoki qayta-qayta yuz bersa — 103 ga qo'ng'iroq qiling.\n\n"
                "⚠️ Kishini darhol tik turg'izMang — qayta yiqilishi mumkin."
            ),
            "ru": (
                "😵 *Первая помощь при обмороке:*\n\n"
                "1. Уложите человека, слегка приподняв ноги.\n"
                "2. Ослабьте тесную одежду, обеспечьте приток воздуха.\n"
                "3. Когда придёт в сознание, медленно усадите и дайте воды.\n"
                "4. Если не приходит в себя 1-2 минуты или обмороки повторяются — звоните 103.\n\n"
                "⚠️ Не поднимайте человека сразу на ноги — возможен повторный обморок."
            ),
        },
    },
    "poisoning": {
        "title": {"uz": "☠️ Zaharlanish", "ru": "☠️ Отравление"},
        "text": {
            "uz": (
                "☠️ *Zaharlanishda birinchi yordam:*\n\n"
                "1. Darhol 103 ga qo'ng'iroq qiling, nima yeb/ichib qo'yganini ayting.\n"
                "2. Qusdirishga o'zingiz urinMang — ba'zi moddalarda bu zararli.\n"
                "3. Kishi hushida bo'lsa, og'zini suv bilan chayqating.\n"
                "4. Zaharning qutisi/idishi bo'lsa, tez yordamga ko'rsatish uchun saqlang.\n"
                "5. Hushsiz bo'lsa, uni yon tomoniga yotqizing (qusuq nafas yo'liga tushmasligi uchun).\n\n"
                "⚠️ Toksikologiya markazi yoki 103 bilan albatta bog'laning."
            ),
            "ru": (
                "☠️ *Первая помощь при отравлении:*\n\n"
                "1. Немедленно звоните 103, сообщите, что именно съел/выпил человек.\n"
                "2. Не вызывайте рвоту самостоятельно — при некоторых веществах это опасно.\n"
                "3. Если человек в сознании, прополощите ему рот водой.\n"
                "4. Сохраните упаковку/ёмкость вещества для скорой помощи.\n"
                "5. Если без сознания — положите на бок (чтобы рвотные массы не попали в дыхательные пути).\n\n"
                "⚠️ Обязательно свяжитесь с токсикологическим центром или 103."
            ),
        },
    },
    "heatstroke": {
        "title": {"uz": "☀️ Issiqlik urishi", "ru": "☀️ Тепловой удар"},
        "text": {
            "uz": (
                "☀️ *Issiqlik urishida birinchi yordam:*\n\n"
                "1. Kishini soyaga yoki salqin joyga olib o'ting.\n"
                "2. Ortiqcha kiyimlarini yeching.\n"
                "3. Tanasini nam sochiq bilan sovuting yoki muxlodor suv purkang.\n"
                "4. Hushida bo'lsa, kichik-kichik yutumlarda suv bering.\n"
                "5. Hushidan ketsa, isitmasi tushmasa yoki qusish bo'lsa — darhol 103 ga qo'ng'iroq qiling.\n\n"
                "⚠️ Sovuq suvga to'liq botirMang — bu shokka olib kelishi mumkin."
            ),
            "ru": (
                "☀️ *Первая помощь при тепловом ударе:*\n\n"
                "1. Переместите человека в тень или прохладное место.\n"
                "2. Снимите лишнюю одежду.\n"
                "3. Охлаждайте тело влажным полотенцем или прохладной водой.\n"
                "4. Если в сознании — давайте пить воду небольшими глотками.\n"
                "5. Если без сознания, температура не снижается или рвота — немедленно звоните 103.\n\n"
                "⚠️ Не погружайте полностью в холодную воду — это может вызвать шок."
            ),
        },
    },
    "seizure": {
        "title": {"uz": "⚡ Talvasa (epilepsiya xuruji)", "ru": "⚡ Судороги (приступ эпилепсии)"},
        "text": {
            "uz": (
                "⚡ *Talvasa xurujida birinchi yordam:*\n\n"
                "1. Atrofdagi qattiq/o'tkir narsalarni chetga suring.\n"
                "2. Boshi ostiga yumshoq narsa qo'ying.\n"
                "3. Kishini ushlab turishga yoki harakatini to'xtatishga urinMang.\n"
                "4. Og'ziga hech narsa tiqMang.\n"
                "5. Xuruj tugagach, uni yon tomonga o'giring.\n"
                "6. Xuruj 5 daqiqadan uzoq davom etsa yoki takrorlansa — 103 ga qo'ng'iroq qiling.\n\n"
                "⚠️ Vaqtni belgilab qo'ying — shifokorlarga foydali bo'ladi."
            ),
            "ru": (
                "⚡ *Первая помощь при судорогах (эпилепсии):*\n\n"
                "1. Уберите вокруг твёрдые/острые предметы.\n"
                "2. Подложите под голову что-то мягкое.\n"
                "3. Не пытайтесь удерживать человека или останавливать движения.\n"
                "4. Не вставляйте ничего в рот.\n"
                "5. После приступа положите человека на бок.\n"
                "6. Если приступ длится дольше 5 минут или повторяется — звоните 103.\n\n"
                "⚠️ Засеките время приступа — это пригодится врачам."
            ),
        },
    },
    "electric_shock": {
        "title": {"uz": "⚡️ Elektr toki urishi", "ru": "⚡️ Поражение электрическим током"},
        "text": {
            "uz": (
                "⚡️ *Elektr toki urganda birinchi yordam:*\n\n"
                "1. Avval o'zingizni himoya qiling — manbani o'chiring yoki quruq, o'tkazmaydigan narsa (yog'och tayoq) bilan itaring.\n"
                "2. Qo'l bilan to'g'ridan-to'g'ri teginMang.\n"
                "3. Xavfsiz bo'lgach, nafas va yurak urishini tekshiring.\n"
                "4. Nafas olmasa — CPR boshlang.\n"
                "5. Kuygan joylar bo'lsa, kuyish bo'yicha yordam bering.\n\n"
                "⚠️ Doim 103 ga qo'ng'iroq qiling — ichki jarohatlar tashqi ko'rinmasligi mumkin."
            ),
            "ru": (
                "⚡️ *Первая помощь при поражении током:*\n\n"
                "1. Сначала обеспечьте свою безопасность — отключите источник или оттолкните сухим непроводящим предметом (деревянной палкой).\n"
                "2. Не прикасайтесь к человеку голыми руками.\n"
                "3. Когда безопасно, проверьте дыхание и пульс.\n"
                "4. Если не дышит — начните СЛР.\n"
                "5. При ожогах окажите соответствующую помощь.\n\n"
                "⚠️ Всегда звоните 103 — внутренние повреждения могут быть незаметны снаружи."
            ),
        },
    },
    "allergy": {
        "title": {"uz": "🤧 Kuchli allergiya (anafilaksiya)", "ru": "🤧 Тяжёлая аллергия (анафилаксия)"},
        "text": {
            "uz": (
                "🤧 *Kuchli allergik reaksiyada birinchi yordam:*\n\n"
                "1. Darhol 103 ga qo'ng'iroq qiling.\n"
                "2. Agar shaxsiy EpiPen (adrenalin) bo'lsa, undan foydalanishga yordam bering.\n"
                "3. Kishini yotqizib, oyoqlarini ko'taring (nafas qisilishi bo'lmasa).\n"
                "4. Nafas olishga qiynalsa, o'tirgan holatda ushlang.\n"
                "5. Hushidan ketsa va nafas olmasa — CPR boshlang.\n\n"
                "⚠️ Belgilari: yuz/tomoq shishishi, nafas qisilishi, terida toshma, bosim keskin pasayishi."
            ),
            "ru": (
                "🤧 *Первая помощь при тяжёлой аллергии (анафилаксии):*\n\n"
                "1. Немедленно звоните 103.\n"
                "2. Если есть личный EpiPen (адреналин), помогите его использовать.\n"
                "3. Уложите человека, приподняв ноги (если нет затруднения дыхания).\n"
                "4. При затруднённом дыхании — держите в сидячем положении.\n"
                "5. Если без сознания и не дышит — начните СЛР.\n\n"
                "⚠️ Симптомы: отёк лица/горла, одышка, сыпь, резкое падение давления."
            ),
        },
    },
    "stroke": {
        "title": {"uz": "🧠 Insult belgilari", "ru": "🧠 Признаки инсульта"},
        "text": {
            "uz": (
                "🧠 *Insultda birinchi yordam (FAST usuli):*\n\n"
                "F — Face (Yuz): bir tomoni osilib qolganmi?\n"
                "A — Arms (Qo'llar): bir qo'lini ko'tarolmayaptimi?\n"
                "S — Speech (Nutq): so'zlari noaniq yoki tushunarsizmi?\n"
                "T — Time (Vaqt): belgilar bo'lsa, DARHOL 103 ga qo'ng'iroq qiling!\n\n"
                "Qo'shimcha:\n"
                "1. Kishini qulay joylashtiring, boshini biroz ko'taring.\n"
                "2. Ovqat yoki suv berMang (yutish qiyin bo'lishi mumkin).\n"
                "3. Belgilar boshlangan vaqtni eslab qoling — bu davolashda muhim.\n\n"
                "⚠️ Har daqiqa muhim — kechiktirmang."
            ),
            "ru": (
                "🧠 *Первая помощь при инсульте (метод FAST):*\n\n"
                "F — Face (Лицо): не опущена ли одна сторона?\n"
                "A — Arms (Руки): может ли поднять обе руки?\n"
                "S — Speech (Речь): не смазана ли, понятна ли?\n"
                "T — Time (Время): при любом признаке — НЕМЕДЛЕННО звоните 103!\n\n"
                "Дополнительно:\n"
                "1. Уложите человека удобно, слегка приподняв голову.\n"
                "2. Не давайте есть или пить (может быть трудно глотать).\n"
                "3. Запомните время начала симптомов — это важно для лечения.\n\n"
                "⚠️ Каждая минута важна — не откладывайте."
            ),
        },
    },
}

# Emergency numbers (Uzbekistan)
EMERGENCY_INFO = {
    "uz": "🚑 Tez yordam: *103*\n🚒 Yong'in: *101*\n👮 Politsiya: *102*",
    "ru": "🚑 Скорая помощь: *103*\n🚒 Пожарная: *101*\n👮 Полиция: *102*",
}

# 100 ta eng ko'p uchraydigan kasallik ro'yxati (nomi UZ/RU).
# Har biri uchun batafsil ma'lumot (belgilari, davolash, birinchi yordam) AI orqali generatsiya qilinadi.
DISEASE_LIST = [
    {"key": "flu", "uz": "Gripp", "ru": "Грипп"},
    {"key": "ards", "uz": "SORS (shamollash)", "ru": "ОРВИ"},
    {"key": "angina", "uz": "Angina", "ru": "Ангина"},
    {"key": "bronchitis", "uz": "Bronxit", "ru": "Бронхит"},
    {"key": "pneumonia", "uz": "Pnevmoniya", "ru": "Пневмония"},
    {"key": "asthma", "uz": "Astma", "ru": "Астма"},
    {"key": "tuberculosis", "uz": "Sil (tuberkulyoz)", "ru": "Туберкулёз"},
    {"key": "covid", "uz": "COVID-19", "ru": "COVID-19"},
    {"key": "sinusitis", "uz": "Sinusit", "ru": "Синусит"},
    {"key": "otitis", "uz": "Otit (quloq yallig'lanishi)", "ru": "Отит"},
    {"key": "pharyngitis", "uz": "Faringit", "ru": "Фарингит"},
    {"key": "laryngitis", "uz": "Laringit", "ru": "Ларингит"},
    {"key": "gastritis", "uz": "Gastrit", "ru": "Гастрит"},
    {"key": "stomach_ulcer", "uz": "Oshqozon yarasi", "ru": "Язва желудка"},
    {"key": "duodenal_ulcer", "uz": "O'n ikki barmoqli ichak yarasi", "ru": "Язва двенадцатиперстной кишки"},
    {"key": "pancreatitis", "uz": "Pankreatit", "ru": "Панкреатит"},
    {"key": "cholecystitis", "uz": "Xoletsistit", "ru": "Холецистит"},
    {"key": "hepatitis_a", "uz": "Gepatit A", "ru": "Гепатит A"},
    {"key": "hepatitis_b", "uz": "Gepatit B", "ru": "Гепатит B"},
    {"key": "hepatitis_c", "uz": "Gepatit C", "ru": "Гепатит C"},
    {"key": "cirrhosis", "uz": "Jigar sirrozi", "ru": "Цирроз печени"},
    {"key": "appendicitis", "uz": "Appenditsit", "ru": "Аппендицит"},
    {"key": "colitis", "uz": "Kolit", "ru": "Колит"},
    {"key": "enteritis", "uz": "Enterit", "ru": "Энтерит"},
    {"key": "hemorrhoids", "uz": "Gemorroy", "ru": "Геморрой"},
    {"key": "diarrhea", "uz": "Diareya (ich ketishi)", "ru": "Диарея"},
    {"key": "constipation", "uz": "Qabziyat", "ru": "Запор"},
    {"key": "dysentery", "uz": "Dizenteriya", "ru": "Дизентерия"},
    {"key": "salmonellosis", "uz": "Salmonellyoz", "ru": "Сальмонеллёз"},
    {"key": "rotavirus", "uz": "Rotavirus infeksiyasi", "ru": "Ротавирусная инфекция"},
    {"key": "diabetes1", "uz": "Qandli diabet (1-tur)", "ru": "Сахарный диабет 1 типа"},
    {"key": "diabetes2", "uz": "Qandli diabet (2-tur)", "ru": "Сахарный диабет 2 типа"},
    {"key": "hypertension", "uz": "Gipertoniya", "ru": "Гипертония"},
    {"key": "hypotension", "uz": "Gipotoniya", "ru": "Гипотония"},
    {"key": "angina_pectoris", "uz": "Stenokardiya", "ru": "Стенокардия"},
    {"key": "arrhythmia", "uz": "Aritmiya", "ru": "Аритмия"},
    {"key": "atherosclerosis", "uz": "Ateroskleroz", "ru": "Атеросклероз"},
    {"key": "varicose", "uz": "Varikoz", "ru": "Варикоз"},
    {"key": "thrombosis", "uz": "Tromboz", "ru": "Тромбоз"},
    {"key": "anemia", "uz": "Anemiya (kamqonlik)", "ru": "Анемия"},
    {"key": "leukemia", "uz": "Leykemiya", "ru": "Лейкемия"},
    {"key": "hypothyroidism", "uz": "Gipotireoz", "ru": "Гипотиреоз"},
    {"key": "hyperthyroidism", "uz": "Gipertireoz", "ru": "Гипертиреоз"},
    {"key": "kidney_stones", "uz": "Buyrak toshi", "ru": "Почечнокаменная болезнь"},
    {"key": "pyelonephritis", "uz": "Pielonefrit", "ru": "Пиелонефрит"},
    {"key": "cystitis", "uz": "Sistit", "ru": "Цистит"},
    {"key": "prostatitis", "uz": "Prostatit", "ru": "Простатит"},
    {"key": "uti", "uz": "Siydik yo'li infeksiyasi", "ru": "Инфекция мочевыводящих путей"},
    {"key": "kidney_failure", "uz": "Buyrak yetishmovchiligi", "ru": "Почечная недостаточность"},
    {"key": "osteochondrosis", "uz": "Osteoxondroz", "ru": "Остеохондроз"},
    {"key": "arthritis", "uz": "Artrit", "ru": "Артрит"},
    {"key": "arthrosis", "uz": "Artroz", "ru": "Артроз"},
    {"key": "gout", "uz": "Podagra", "ru": "Подагра"},
    {"key": "osteoporosis", "uz": "Osteoporoz", "ru": "Остеопороз"},
    {"key": "scoliosis", "uz": "Skolioz", "ru": "Сколиоз"},
    {"key": "spinal_hernia", "uz": "Bel churrasi (gryja)", "ru": "Грыжа позвоночника"},
    {"key": "radiculitis", "uz": "Radikulit", "ru": "Радикулит"},
    {"key": "migraine", "uz": "Migren", "ru": "Мигрень"},
    {"key": "vertigo", "uz": "Bosh aylanishi", "ru": "Головокружение"},
    {"key": "epilepsy2", "uz": "Epilepsiya", "ru": "Эпилепсия"},
    {"key": "stroke2", "uz": "Insult", "ru": "Инсульт"},
    {"key": "parkinson", "uz": "Parkinson kasalligi", "ru": "Болезнь Паркинсона"},
    {"key": "alzheimer", "uz": "Alsgeymer kasalligi", "ru": "Болезнь Альцгеймера"},
    {"key": "multiple_sclerosis", "uz": "Rasseyanniy skleroz", "ru": "Рассеянный склероз"},
    {"key": "depression", "uz": "Depressiya", "ru": "Депрессия"},
    {"key": "anxiety", "uz": "Tashvish buzilishi", "ru": "Тревожное расстройство"},
    {"key": "insomnia", "uz": "Insomniya (uyqusizlik)", "ru": "Бессонница"},
    {"key": "conjunctivitis", "uz": "Kon'yunktivit", "ru": "Конъюнктивит"},
    {"key": "cataract", "uz": "Katarakta", "ru": "Катаракта"},
    {"key": "glaucoma", "uz": "Glaukoma", "ru": "Глаукома"},
    {"key": "myopia", "uz": "Miopiya", "ru": "Миопия"},
    {"key": "herpes", "uz": "Gerpes", "ru": "Герпес"},
    {"key": "psoriasis", "uz": "Psoriaz", "ru": "Псориаз"},
    {"key": "eczema", "uz": "Ekzema", "ru": "Экзема"},
    {"key": "dermatitis", "uz": "Dermatit", "ru": "Дерматит"},
    {"key": "acne", "uz": "Akne", "ru": "Акне"},
    {"key": "fungal_infection", "uz": "Zamburug' infeksiyasi", "ru": "Грибковая инфекция кожи"},
    {"key": "scabies", "uz": "Qichima (skabiyoz)", "ru": "Чесотка"},
    {"key": "alopecia", "uz": "Alopetsiya (soch to'kilishi)", "ru": "Алопеция"},
    {"key": "endometriosis", "uz": "Endometrioz", "ru": "Эндометриоз"},
    {"key": "uterine_fibroids", "uz": "Bachadon miomasi", "ru": "Миома матки"},
    {"key": "mastopathy", "uz": "Mastopatiya", "ru": "Мастопатия"},
    {"key": "menopause", "uz": "Menopauza belgilari", "ru": "Симптомы менопаузы"},
    {"key": "infertility", "uz": "Bepushtlik", "ru": "Бесплодие"},
    {"key": "prostate_adenoma", "uz": "Prostata adenomasi", "ru": "Аденома простаты"},
    {"key": "measles", "uz": "Qizamiq", "ru": "Корь"},
    {"key": "chickenpox", "uz": "Suvchechak", "ru": "Ветряная оспа"},
    {"key": "mumps", "uz": "Parotit (svinka)", "ru": "Паротит"},
    {"key": "scarlet_fever", "uz": "Skarlatina", "ru": "Скарлатина"},
    {"key": "diphtheria", "uz": "Difteriya", "ru": "Дифтерия"},
    {"key": "pertussis", "uz": "Ko'kyo'tal", "ru": "Коклюш"},
    {"key": "botulism", "uz": "Botulizm", "ru": "Ботулизм"},
    {"key": "tetanus", "uz": "Qoqshol (stolbnyak)", "ru": "Столбняк"},
    {"key": "malaria", "uz": "Bezgak (malyariya)", "ru": "Малярия"},
    {"key": "rabies", "uz": "Quturuv", "ru": "Бешенство"},
    {"key": "heart_failure", "uz": "Yurak yetishmovchiligi", "ru": "Сердечная недостаточность"},
    {"key": "myocarditis", "uz": "Miokardit", "ru": "Миокардит"},
    {"key": "pericarditis", "uz": "Perikardit", "ru": "Перикардит"},
    {"key": "asthma_attack", "uz": "Bronxial astma xuruji", "ru": "Приступ бронхиальной астмы"},
    {"key": "allergic_dermatitis", "uz": "Allergik dermatit", "ru": "Аллергический дерматит"},
]
