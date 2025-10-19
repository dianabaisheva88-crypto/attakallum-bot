import telebot
from telebot import types
import random

TOKEN = "8278165254:AAGnd36TKpFZEGZhXFpsQMas5rmg0NpxhVI"
bot = telebot.TeleBot(TOKEN)

# ==============================
# 📚 СЛОВАРЬ по юнитам
# ==============================
words = {
    "Unit 1 — وَصْفُ النَّاسِ / Описание людей": {
        # --- Внешность ---
        "مُستدِير": "круглый",
        "بَيْضَاوِيّ": "овальный, яйцевидный",
        "ناعِم": "мягкий",
        "خَشِن": "жесткий",
        "مُجَعَّد": "кудрявый",
        "مُمَوَّج": "волнистый",
        "أَسْود": "чёрный",
        "أَشْيَب": "седой",
        "أَشْقر": "блондин",
        "طويل (ة)": "высокий",
        "قصير (ة)": "короткий, низкий",
        "متوسِّط (ة) / معتدِل (ة)": "среднего роста",
        "مُستقيم": "стройный",
        "مُنْحَنٍ": "изогнутый",
        "قوِيّ (ة)": "сильный",
        "ضعيف (ة)": "слабый",
        "ذو عَضَلات": "мускулистый",
        "عَسَلِيَّة": "цвета мёда",
        "سوداء": "чёрный (о глазах, волосах)",
        "زَرْقاء": "синий",
        "بُنِّيَّة": "коричневый",
        "خضراء": "зелёный",
        "واسِعة": "широкий, большой",
        "ضَيِّقَة": "узкий",
        "دَقِيقٌ / صَغير": "маленький, тонкий",
        "كبير / أَفْطَس": "большой",
        "دَاكِنة": "тёмный",
        "فَاتِحة": "светлый",
        "قَمْحِيَّة / حِنْطِيَّة": "светло-коричневый",
        "بيضاء": "белый",
        "شَقْراء": "блондин, светловолосый",
        "شاحِبة": "бледный",
        "وَسِيم": "с родимыми пятнами",
        "قَبِيح / دَمِيم": "уродливый",
        "أَنِيق": "красивый, элегантный",
        "سَمِين": "толстый",
        "نَحِيف": "тонкий, худой",
        "مُتَوَسِّط الوَزْن": "среднего веса",
        "حَامِل": "беременная",
        "مُعَاق": "инвалид",
        "أَعْمَى / فَاقِد البَصَر / كَفِيفٌ": "слепой",
        "أَصَمُّ / فاقِد السَّمْع": "глухой",
        "غَالية": "дорогой",
        "رَخيصَة": "дешёвый",
        "جديدة": "новый",
        "بَالِية / رَثَّة / قديمة": "изношенный, старый",
        "مُهَنْدَمَة / مُرَتَّبَة": "аккуратный, опрятный",
        "غير مُرَتَّبَة": "неопрятный, небрежный",
        "ذو شَارِب": "усатый",
        "ذو لِحْيَة / مُلْتَحٍ": "бородатый",

        # --- Одежда и особенности ---
        "مُحَجَّبَة": "женщина в хиджабе",
        "مُنْتَقِبَة": "женщина, скрывающая лицо (в никабе)",
        "مُتَبَرِّجَة / سَافِرَة": "женщина без головного платка (без хиджаба)",
        "عليه أثَرُ جُرُوح / نُدُوب": "со шрамами, раненый",
        "ذو - ذات شَامَة / ذو - ذات خَالٍ": "с родимыми пятнами",
        "أَصْلَع (صَلْعَاء)": "лысый, бритоголовый",
        "أَقْرَع (قَرْعَاء)": "плешивый",

        # --- Возраст ---
        "طِفل": "ребёнок",
        "مُراهِق": "подросток",
        "شابٌّ": "молодой человек",
        "كَهْل": "средних лет",
        "عجُوز": "пожилая женщина",
        "مُسِنٌّ": "старый, в возрасте",
        "في العِشْرينيَّات": "в возрасте двадцати лет",
        "في الثَّلاثِينيَّات": "в возрасте тридцати лет",
        "في الأرْبَعينيَّات": "в возрасте сорока лет",

        # --- Характер ---
        "خَجُول / اِنْطِوَائِيّ × اِجْتِمَاعِي": "застенчивый × общительный",
        "ذكِيّ × غَبيّ": "умный × глупый",
        "مُجتهد / نشِيط × مُهْمِل / كَسْلان": "трудолюбивый × ленивый",
        "مُؤدَّب × قليل الأدب / وَقِح": "вежливый × невежливый",
        "طَيِّب / حَنُون / عَطُوف": "добрый, отзывчивый",
        "فَظّ / غلِيظ / قاسٍ": "грубый, жестокий",
        "قَنُوع × طَمَّاع": "неприхотливый × ненасытный",
        "صادِق × كاذِب": "честный × нечестный",
        "هادئ × عَصَبِي": "спокойный × нервный",
        "شُجَاع × جَبَان": "мужественный × трусливый",
        "فَخُور / مُتَكَبِّر / مَغْرور × مُتَوَاضِع": "тщеславный × скромный",
        "مُتَهَوِّر × مُتَرَدِّد": "нетерпеливый × нерешительный",
        "كريم × بخيل": "щедрый × скупой",
        "مُسَالِم × شَرِس / عُدْوَاني": "уживчивый × неуживчивый",
        "صَبُور × مَلُول": "терпеливый × нетерпеливый",
        "عَنِيد × مُتَفَاهم / مُطِيعٌ": "упрямый × послушный",
        "ثَرْثَار × قليل الكلام": "болтливый × необщительный",
        "نَهِمٌ / أَكُولٌ": "прожорливый",
        "خائف / مَذْعُور": "боязливый",
        "مُتضايق / غضبان": "расстроенный, сердитый",
        "حَانِق / هَائِج / مُغْتَاظ": "разъярённый, раздражённый",
        "مُشْمَئِز / مُتَقَزِّز": "брезгливый, чувствующий отвращение",
        "مَصْدُوم / مَذْهُول / مُنْدَهِش": "потрясённый, ошеломлённый",
        "مُشْتَاق": "тоскующий",
        "اِسْتِفْزَازِي": "провокационный, разжигающий",
    },
}

# ==============================
# 🔹 Главное меню
# ==============================
@bot.message_handler(commands=['start'])
def start(message):
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
    markup.add(types.KeyboardButton("📚 Словарь"), types.KeyboardButton("🧠 Тренировка"))
    bot.send_message(
        message.chat.id,
        f"Выбран {unit}. Что будем делать?",
        reply_markup=markup
    )
    bot.register_next_step_handler(message, mode_select, unit)

# ==============================
# 🔹 Выбор режима
# ==============================
def mode_select(message, unit):
    if message.text == "📚 Словарь":
        vocab = "\n".join([f"{ar} — {ru}" for ar, ru in words[unit].items()])
        bot.send_message(message.chat.id, f"📖 {unit}\n\n{vocab}")
        start(message)

    elif message.text == "🧠 Тренировка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("➡️ Арабский → Русский"),
            types.KeyboardButton("⬅️ Русский → Арабский")
        )
        bot.send_message(
            message.chat.id,
            "Выбери направление тренировки:",
            reply_markup=markup
        )
        bot.register_next_step_handler(message, choose_direction, unit)
    else:
        start(message)

# ==============================
# 🔹 Выбор направления
# ==============================
def choose_direction(message, unit):
    if "Арабский" in message.text:
        send_quiz_ar_to_ru(message, unit)
    elif "Русский" in message.text:
        send_quiz_ru_to_ar(message, unit)
    else:
        start(message)

# ==============================
# 🔹 Тест: Арабский → Русский
# ==============================
def send_quiz_ar_to_ru(message, unit):
    arabic, correct = random.choice(list(words[unit].items()))
    all_answers = list(words[unit].values())
    options = [correct]
    while len(options) < 4:
        fake = random.choice(all_answers)
        if fake not in options:
            options.append(fake)
    random.shuffle(options)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for opt in options:
        markup.add(types.KeyboardButton(opt))

    bot.send_message(
        message.chat.id,
        f"🧠 Как переводится: {arabic}?",
        reply_markup=markup
    )
    bot.register_next_step_handler(message, check_answer_ar_to_ru, unit, arabic, correct)

def check_answer_ar_to_ru(message, unit, arabic, correct):
    if message.text == correct:
        bot.send_message(message.chat.id, "✅ Верно!")
    else:
        bot.send_message(message.chat.id, f"❌ Неверно. Правильный ответ: {correct}")
    next_action(message, unit)

# ==============================
# 🔹 Тест: Русский → Арабский
# ==============================
def send_quiz_ru_to_ar(message, unit):
    arabic, correct = random.choice(list(words[unit].items()))
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

    bot.send_message(
        message.chat.id,
        f"🧠 Как по-арабски: {correct}?",
        reply_markup=markup
    )
    bot.register_next_step_handler(message, check_answer_ru_to_ar, unit, correct, arabic)

def check_answer_ru_to_ar(message, unit, correct, arabic):
    if message.text == arabic:
        bot.send_message(message.chat.id, "✅ Верно!")
    else:
        bot.send_message(message.chat.id, f"❌ Неверно. Правильный ответ: {arabic}")
    next_action(message, unit)

# ==============================
# 🔹 Следующее действие
# ==============================
def next_action(message, unit):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("🧠 Ещё вопрос"), types.KeyboardButton("🏠 Меню"))
    bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)
    bot.register_next_step_handler(message, next_action_choice, unit)

def next_action_choice(message, unit):
    if message.text == "🧠 Ещё вопрос":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(
            types.KeyboardButton("➡️ Арабский → Русский"),
            types.KeyboardButton("⬅️ Русский → Арабский")
        )
        bot.send_message(
            message.chat.id,
            "Выбери направление:",
            reply_markup=markup
        )
        bot.register_next_step_handler(message, choose_direction, unit)
    else:
        start(message)

# ==============================
print("✅ Бот запущен и готов к двусторонним тестам.")
bot.polling()

