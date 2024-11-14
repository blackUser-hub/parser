import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery
from database import init_db, add_user, toggle_category, get_user_categories  # Импорт функций из database.py

# Настройки бота
API_TOKEN = "8054346845:AAHNITZO28TM-RGTnDoWrCXHuc6VY-Ir8jU"  # Замените на токен вашего бота



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

def create_categories_menu(user_id):
    # Получаем текущий статус категорий пользователя из базы данных
    categories = get_user_categories(user_id)
    
    # Если нет категорий, создаем пустую клавиатуру с сообщением
    if not categories:
        return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Нет доступных категорий", callback_data="no_categories")]])

    # Создаём меню категорий
    categories_menu = InlineKeyboardMarkup(inline_keyboard=[])
    gg = {'Crypto': 'Криптовалюты', "Politics":"Политика","Economics":"Экономина","Other":"Другое", "Medias":"Медиа", "Digital":"Диджитал", "Military_conflicts":"Военные конфликты"}
    # Добавляем кнопку для каждой категории
    for category, is_enabled in categories.items():
        status = "Вкл" if is_enabled else "Выкл"
        button = InlineKeyboardButton(
            text=f"{gg[str(category.capitalize())]}: {status}",
            callback_data=f"toggle_{category}"
        )
        categories_menu.inline_keyboard.append([button])  # Добавляем кнопку в отдельный ряд

    return categories_menu

# Обработчик команды /start
@dp.message(Command("start"))
async def start_command(message: Message):
    user_id = message.from_user.id
    add_user(user_id)  # Добавляем пользователя в базу данных

    # Отправляем приветственное сообщение с главным меню
    await message.answer(
        "Добро пожаловать! Вы были добавлены в базу данных. Выберите одну из опций:",
        reply_markup=create_main_menu()
    )

# Обработчик нажатия на кнопку "Категории"
@dp.message(lambda message: message.text == "Категории")
async def show_categories(message: Message):
    user_id = message.from_user.id
    await message.answer(
        "Вот доступные категории. Нажмите на кнопку, чтобы включить или выключить нужную категорию:",
        reply_markup=create_categories_menu(user_id)
    )

@dp.message(lambda message: message.text == "Отключение рекламы")
async def show_categories(message: Message):
    user_id = message.from_user.id
    await message.answer(
        "Опять попался в ловушку сраного капитализма, на этот раз прощаю"
    )

# Обработчик для переключения состояния категорий
@dp.callback_query(lambda callback_query: callback_query.data.startswith("toggle_"))
async def toggle_category_callback(callback_query: CallbackQuery):
    user_id = callback_query.from_user.id
    category = callback_query.data.split("_")[1]  # Получаем название категории из callback_data

    # Переключаем состояние категории в базе данных
    toggle_category(user_id, category)

    # Обновляем меню категорий
    await callback_query.message.edit_reply_markup(reply_markup=create_categories_menu(user_id))
    await callback_query.answer(f"Категория '{category.capitalize()}' была обновлена")


@dp.callback_query(lambda callback_query: callback_query.data == "no_categories")
async def no_categories_callback(callback_query: CallbackQuery):
    await callback_query.answer("Категории пока недоступны", show_alert=True)

# Основная функция для запуска бота
async def main():
    init_db()  # Инициализация базы данных перед запуском бота
    await dp.start_polling(bot)

# Запуск бота
if __name__ == "__main__":
    asyncio.run(main())