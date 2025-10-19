import telebot
from telebot import types
import random

TOKEN = "8278165254:AAGnd36TKpFZEGZhXFpsQMas5rmg0NpxhVI"
bot = telebot.TeleBot(TOKEN)

# ==============================
# 📚 СЛОВАРЬ по юнитам
# ==============================
words = {
    "Unit 1 — وَصْفُ النَّاسِ / Oписание людей / Odamlarni tasvirlash": {
        # --- Внешность ---
        "مُستدِير": {"ru": "круглый", "uz": "dumaloq"},
        "بَيْضَاوِيّ": {"ru": "овальный, яйцевидный", "uz": "tuxumsimon"},
        "ناعِم": {"ru": "мягкий", "uz": "yumshoq"},
        "خَشِن": {"ru": "жесткий", "uz": "dag‘al"},
        "مُجَعَّد": {"ru": "кудрявый", "uz": "jingalak"},
        "مُمَوَّج": {"ru": "волнистый", "uz": "to‘lqinli"},
        "أَسْود": {"ru": "чёрный", "uz": "qora"},
        "أَشْيَب": {"ru": "седой", "uz": "sochlari oq"},
        "أَشْقر": {"ru": "блондин", "uz": "sariqsoch"},
        "طويل (ة)": {"ru": "высокий", "uz": "bo‘yi baland"},
        "قصير (ة)": {"ru": "короткий, низкий", "uz": "past, kalta"},
        "متوسِّط (ة) / معتدِل (ة)": {"ru": "среднего роста", "uz": "o‘rtacha bo‘yli"},
        "مُستقيم": {"ru": "стройный", "uz": "to‘g‘ri qomatli"},
        "مُنْحَنٍ": {"ru": "изогнутый", "uz": "bukilgan"},
        "قوِيّ (ة)": {"ru": "сильный", "uz": "kuchli"},
        "ضعيف (ة)": {"ru": "слабый", "uz": "zaif"},
        "ذو عَضَلات": {"ru": "мускулистый", "uz": "mushakdor"},
        "عَسَلِيَّة": {"ru": "цвета мёда", "uz": "asal rang"},
        "سوداء": {"ru": "чёрный (о глазах, волосах)", "uz": "qora"},
        "زَرْقاء": {"ru": "синий", "uz": "ko‘k"},
        "بُنِّيَّة": {"ru": "коричневый", "uz": "jigarrang"},
        "خضراء": {"ru": "зелёный", "uz": "yashil"},
        "واسِعة": {"ru": "широкий, большой", "uz": "keng"},
        "ضَيِّقَة": {"ru": "узкий", "uz": "tor"},
        "دَقِيقٌ / صَغير": {"ru": "маленький, тонкий", "uz": "kichik, ingichka"},
        "كبير / أَفْطَس": {"ru": "большой", "uz": "katta"},
        "دَاكِنة": {"ru": "тёмный", "uz": "to‘q rang"},
        "فَاتِحة": {"ru": "светлый", "uz": "och rang"},
        "قَمْحِيَّة / حِنْطِيَّة": {"ru": "светло-коричневый", "uz": "bug‘doyrang"},
        "بيضاء": {"ru": "белый", "uz": "oq"},
        "شَقْراء": {"ru": "блондин, светловолосый", "uz": "sariqsoch"},
        "شاحِبة": {"ru": "бледный", "uz": "rangi oqarib ketgan"},
        "وَسِيم": {"ru": "с родимыми пятнами", "uz": "xolga ega"},
        "قَبِيح / دَمِيم": {"ru": "уродливый", "uz": "xunuk"},
        "أَنِيق": {"ru": "красивый, элегантный", "uz": "kelishgan"},
        "سَمِين": {"ru": "толстый", "uz": "semiz"},
        "نَحِيف": {"ru": "тонкий, худой", "uz": "ozg‘in"},
        "مُتَوَسِّط الوَزْن": {"ru": "среднего веса", "uz": "o‘rtacha vaznli"},
        "حَامِل": {"ru": "беременная", "uz": "homilador"},
        "مُعَاق": {"ru": "инвалид", "uz": "nogiron"},
        "أَعْمَى / فَاقِد البَصَر / كَفِيفٌ": {"ru": "слепой", "uz": "ko‘r"},
        "أَصَمُّ / فاقِد السَّمْع": {"ru": "глухой", "uz": "kar"},
        "غَالية": {"ru": "дорогой", "uz": "qimmat"},
        "رَخيصَة": {"ru": "дешёвый", "uz": "arzon"},
        "جديدة": {"ru": "новый", "uz": "yangi"},
        "بَالِية / رَثَّة / قديمة": {"ru": "изношенный, старый", "uz": "eski"},
        "مُهَنْدَمَة / مُرَتَّبَة": {"ru": "аккуратный, опрятный", "uz": "ozoda"},
        "غير مُرَتَّبَة": {"ru": "неопрятный, небрежный", "uz": "tartibsiz"},
        "ذو شَارِب": {"ru": "усатый", "uz": "mo‘ylovli"},
        "ذو لِحْيَة / مُلْتَحٍ": {"ru": "бородатый", "uz": "soqolli"},
        # --- Одежда и особенности ---
        "مُحَجَّبَة": {"ru": "женщина в хиджабе", "uz": "ro‘mol o‘ragan ayol"},
        "مُنْتَقِبَة": {"ru": "женщина, скрывающая лицо (в никабе)", "uz": "niqobli ayol"},
        "مُتَبَرِّجَة / سَافِرَة": {"ru": "женщина без хиджаба", "uz": "ro‘molsiz ayol"},
        "عليه أثَرُ جُرُوح / نُدُوب": {"ru": "со шрамами, раненый", "uz": "chandiqli"},
        "ذو - ذات شَامَة / ذو - ذات خَالٍ": {"ru": "с родимыми пятнами", "uz": "xollari bor"},
        "أَصْلَع (صَلْعَاء)": {"ru": "лысый", "uz": "kal"},
        "أَقْرَع (قَرْعَاء)": {"ru": "плешивый", "uz": "sochi to‘kilgan"},
        # --- Возраст ---
        "طِفل": {"ru": "ребёнок", "uz": "bola"},
        "مُراهِق": {"ru": "подросток", "uz": "o‘smir"},
        "شابٌّ": {"ru": "молодой человек", "uz": "yigit"},
        "كَهْل": {"ru": "средних лет", "uz": "o‘rta yoshli"},
        "عجُوز": {"ru": "пожилая женщина", "uz": "keksa ayol"},
        "مُسِنٌّ": {"ru": "старый", "uz": "keksaygan"},
        "في العِشْرينيَّات": {"ru": "в возрасте двадцати лет", "uz": "yigirma yoshlar atrofida"},
        "في الثَّلاثِينيَّات": {"ru": "в возрасте тридцати лет", "uz": "o‘ttiz yoshlar atrofida"},
        "في الأرْبَعينيَّات": {"ru": "в возрасте сорока лет", "uz": "qirq yoshlar atrofida"},
        # --- Характер ---
        "خَجُول / اِنْطِوَائِيّ × اِجْتِمَاعِي": {"ru": "застенчивый × общительный", "uz": "uyatchan × kirishimli"},
        "ذكِيّ × غَبيّ": {"ru": "умный × глупый", "uz": "aqlli × ahmoq"},
        "مُجتهد / نشِيط × مُهْمِل / كَسْلان": {"ru": "трудолюбивый × ленивый", "uz": "mehnatsevar × dangasa"},
        "مُؤدَّب × قليل الأدب / وَقِح": {"ru": "вежливый × невежливый", "uz": "odobli × odobsiz"},
        "طَيِّب / حَنُون / عَطُوف": {"ru": "добрый, отзывчивый", "uz": "mehribon"},
        "فَظّ / غلِيظ / قاسٍ": {"ru": "грубый, жестокий", "uz": "qo‘pol, qattiqqo‘l"},
        "قَنُوع × طَمَّاع": {"ru": "неприхотливый × ненасытный", "uz": "qanoatli × ochko‘z"},
        "صادِق × كاذِب": {"ru": "честный × нечестный", "uz": "rostgo‘y × yolg‘onchi"},
        "هادئ × عَصَبِي": {"ru": "спокойный × нервный", "uz": "tinch × asabiy"},
        "شُجَاع × جَبَان": {"ru": "мужественный × трусливый", "uz": "jasur × qo‘rqoq"},
        "فَخُور / مُتَكَبِّر / مَغْرور × مُتَوَاضِع": {"ru": "тщеславный × скромный", "uz": "mag‘rur × kamtar"},
        "مُتَهَوِّر × مُتَرَدِّد": {"ru": "нетерпеливый × нерешительный", "uz": "shoshqaloq × ikkilanadigan"},
        "كريم × بخيل": {"ru": "щедрый × скупой", "uz": "saxiy × baxil"},
        "مُسَالِم × شَرِس / عُدْوَاني": {"ru": "уживчивый × неуживчивый", "uz": "tinch × tajovuzkor"},
        "صَبُور × مَلُول": {"ru": "терпеливый × нетерпеливый", "uz": "sabrli × sabrsiz"},
        "عَنِيد × مُتَفَاهم / مُطِيعٌ": {"ru": "упрямый × послушный", "uz": "qaysar × itoatli"},
        "ثَرْثَار × قليل الكلام": {"ru": "болтливый × необщительный", "uz": "gapdon × kamgap"},
        "نَهِمٌ / أَكُولٌ": {"ru": "прожорливый", "uz": "ochko‘z"},
        "خائف / مَذْعُور": {"ru": "боязливый", "uz": "qo‘rqoq"},
        "مُتضايق / غضبان": {"ru": "расстроенный, сердитый", "uz": "xafa, jahli chiqqan"},
        "حَانِق / هَائِج / مُغْتَاظ": {"ru": "разъярённый, раздражённый", "uz": "g‘azablangan"},
        "مُشْمَئِز / مُتَقَزِّز": {"ru": "брезгливый, чувствующий отвращение", "uz": "jirkanch"},
        "مَصْدُوم / مَذْهُول / مُنْدَهِش": {"ru": "потрясённый, ошеломлённый", "uz": "hayratlangan"},
        "مُشْتَاق": {"ru": "тоскующий", "uz": "sog‘ingan"},
        "اِسْتِفْزَازِي": {"ru": "провокационный, разжигающий", "uz": "qo‘zg‘atuvchi"},
  },
}

# ==============================
# 🔹 Храним язык пользователя
# ==============================
user_language = {}

# ==============================
# 🔹 Главное меню
# ==============================
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Русский 🇷🇺"), types.KeyboardButton("Oʻzbek 🇺🇿"))
    bot.send_message(
        message.chat.id,
        "🌍 Выбери язык перевода / Tarjima tilini tanlang:",
        reply_markup=markup
    )
    bot.register_next_step_handler(message, set_language)

def set_language(message):
    if "Рус" in message.text:
        user_language[message.chat.id] = "ru"
    elif "Oʻzbek" in message.text or "Uz" in message.text:
        user_language[message.chat.id] = "uz"
    else:
        bot.send_message(message.chat.id, "Пожалуйста, выбери 🇷🇺 или 🇺🇿.")
        return start(message)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for unit in words.keys():
        markup.add(types.KeyboardButton(unit))
    bot.send_message(
        message.chat.id,
        "👋 Ассаляму алейкум! Выбери юнит для учёбы:",
        reply_markup=markup
    )

# ==============================
# 🔹 Выбор юнита
# ==============================
@bot.message_handler(func=lambda msg: msg.text in words.keys())
def select_unit(message):
    unit = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("📚 Словарь / Lugʻat"), types.KeyboardButton("🧠 Тренировка / Mashq"))
    bot.send_message(message.chat.id, f"Выбран {unit}. Что будем делать?", reply_markup=markup)
    bot.register_next_step_handler(message, mode_select, unit)

# ==============================
# 🔹 Выбор режима
# ==============================
def mode_select(message, unit):
    if "Словарь" in message.text or "Lugʻat" in message.text:
        lang = user_language.get(message.chat.id, "ru")
        vocab = "\n".join([f"{ar} — {data[lang]}" for ar, data in words[unit].items()])
        bot.send_message(message.chat.id, f"📖 {unit}\n\n{vocab}")
        start(message)

    elif "Тренировка" in message.text or "Mashq" in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("➡️ Арабский → Перевод"),
            types.KeyboardButton("⬅️ Перевод → Арабский")
        )
        bot.send_message(message.chat.id, "Выбери направление:", reply_markup=markup)
        bot.register_next_step_handler(message, choose_direction, unit)
    else:
        start(message)

# ==============================
# 🔹 Выбор направления
# ==============================
def choose_direction(message, unit):
    if "Арабский" in message.text:
        send_quiz_ar_to_lang(message, unit)
    elif "Перевод" in message.text:
        send_quiz_lang_to_ar(message, unit)
    else:
        start(message)

# ==============================
# 🔹 Тест: Арабский → Перевод (RU/UZ)
# ==============================
def send_quiz_ar_to_lang(message, unit):
    lang = user_language.get(message.chat.id, "ru")
    arabic, correct = random.choice(list(words[unit].items()))
    correct = correct[lang]
    all_answers = [w[lang] for w in words[unit].values()]
    options = [correct]
    while len(options) < 4:
        fake = random.choice(all_answers)
        if fake not in options:
            options.append(fake)
    random.shuffle(options)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for opt in options:
        markup.add(types.KeyboardButton(opt))

    bot.send_message(message.chat.id, f"🧠 Как переводится: {arabic}?", reply_markup=markup)
    bot.register_next_step_handler(message, check_answer_ar_to_lang, unit, arabic, correct)

def check_answer_ar_to_lang(message, unit, arabic, correct):
    if message.text == correct:
        bot.send_message(message.chat.id, "✅ Верно!")
    else:
        bot.send_message(message.chat.id, f"❌ Неверно. Правильный ответ: {correct}")
    next_action(message, unit)

# ==============================
# 🔹 Тест: Перевод (RU/UZ) → Арабский
# ==============================
def send_quiz_lang_to_ar(message, unit):
    lang = user_language.get(message.chat.id, "ru")
    arabic, correct_data = random.choice(list(words[unit].items()))
    correct = correct_data[lang]
    all_arabic = list(words[unit].keys())
    options = [arabic]
    while len(options) < 4:
        fake = random.choice(all_arabic)
        if fake not in options:
            options.append(fake)
    random.shuffle(options)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for opt in options:
        markup.add(types.KeyboardButton(opt))

    bot.send_message(message.chat.id, f"🧠 Как по-арабски: {correct}?", reply_markup=markup)
    bot.register_next_step_handler(message, check_answer_lang_to_ar, unit, correct, arabic)

def check_answer_lang_to_ar(message, unit, correct, arabic):
    if message.text == arabic:
        bot.send_message(message.chat.id, "✅ Верно!")
    else:
        bot.send_message(message.chat.id, f"❌ Неверно. Правильный ответ: {arabic}")
    next_action(message, unit)

# ==============================
# 🔹 Действие после ответа
# ==============================
def next_action(message, unit):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🧠 Ещё вопрос"), types.KeyboardButton("🏠 Меню"))
    bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)
    bot.register_next_step_handler(message, next_action_choice, unit)

def next_action_choice(message, unit):
    if "Ещё" in message.text:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("➡️ Арабский → Перевод"),
            types.KeyboardButton("⬅️ Перевод → Арабский")
        )
        bot.send_message(message.chat.id, "Выбери направление:", reply_markup=markup)
        bot.register_next_step_handler(message, choose_direction, unit)
    else:
        start(message)

# ==============================
print("✅ Бот запущен с поддержкой русского и узбекского перевода.")
bot.polling()

