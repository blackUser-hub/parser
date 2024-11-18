from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram import types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery
from database import init_db, add_user, toggle_category, get_user_categories
import asyncio

# Настройки бота
API_TOKEN = "8054346845:AAHNITZO28TM-RGTnDoWrCXHuc6VY-Ir8jU"  # Убедитесь, что API_TOKEN указан верно
gg = {'Crypto': 'Криптовалюты', "Politics": "Политика", "Economics": "Экономика", "Other": "Другое", 
      "Medias": "Медиа", "Digital": "Диджитал", "Military_conflicts": "Конфликты"}


# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Функция для создания главного меню
def create_main_menu():
    button_categories = KeyboardButton(text="Категории")
    button_payments = KeyboardButton(text="Отключение рекламы")
    main_menu = ReplyKeyboardMarkup(keyboard=[[button_categories, button_payments]], resize_keyboard=True)
    return main_menu

# Функция для создания меню категорий с кнопками для включения/выключения
async def create_categories_menu(user_id):
    categories = await get_user_categories(user_id)  # Асинхронный вызов
    
    if not categories:
        return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Нет доступных категорий", callback_data="no_categories")]])

    categories_menu = InlineKeyboardMarkup(inline_keyboard=[])
    for category, is_enabled in categories.items():
        status = "Вкл" if is_enabled else "Выкл"
        button = InlineKeyboardButton(
            text=f"{category.capitalize()}: {status}",
            callback_data=f"toggle_{category.lower().replace(' ', '_')}"
        )
        categories_menu.inline_keyboard.append([button])

    return categories_menu

# Обработчик команды /start
async def start_command(message: Message):
    user_id = message.from_user.id
    await add_user(user_id)  # Асинхронный вызов

    await message.answer(
        "Добро пожаловать! Вы были добавлены в базу данных. Выберите одну из опций:",
        reply_markup=create_main_menu()
    )

# Обработчик нажатия на кнопку "Категории"
async def show_categories(message: Message):
    user_id = message.from_user.id
    categories_menu = await create_categories_menu(user_id)  # Асинхронный вызов
    await message.answer(
        "Вот доступные категории. Нажмите на кнопку, чтобы включить или выключить нужную категорию:",
        reply_markup=categories_menu
    )

async def show_ads_options(message: Message):
    await message.answer("Опять попался в ловушку капитализма, на этот раз прощаю")

# Обработчик для переключения состояния категорий
async def toggle_category_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    category = callback_query.data.split("_", 1)[1]

    await toggle_category(user_id, category)  # Асинхронный вызов
    new_reply_markup = await create_categories_menu(user_id)  # Асинхронный вызов
    await callback_query.message.edit_reply_markup(reply_markup=new_reply_markup)

async def no_categories_callback(callback_query: CallbackQuery):
    await callback_query.answer("Категории пока недоступны", show_alert=True)

# Основная функция для запуска бота
async def bot_main():
    await init_db()  # Инициализация базы данных перед запуском бота
    print('бот стартовал')
    # Добавление обработчиков
    dp.message.register(start_command, Command("start"))
    dp.message.register(show_categories, F.text == "Категории")
    dp.message.register(show_ads_options, F.text == "Отключение рекламы")
    dp.callback_query.register(toggle_category_callback, F.data.startswith("toggle_"))
    dp.callback_query.register(no_categories_callback, F.data == "no_categories")

    await dp.start_polling(bot)
