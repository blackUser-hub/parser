from sqlalchemy import create_engine, Column, Integer, Boolean, or_
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.future import select

# Подключение к базе данных SQLite
DATABASE_URL = "sqlite+aiosqlite:///users.db"
engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=True)

# Фабрика асинхронных сессий
async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Базовый класс для моделей
Base = declarative_base()

# Модель User, представляющая таблицу users
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True)
    crypto = Column(Boolean, default=False)
    politics = Column(Boolean, default=False)
    economics = Column(Boolean, default=False)
    medias = Column(Boolean, default=False)
    digital = Column(Boolean, default=False)
    military_conflicts = Column(Boolean, default=False)
    other = Column(Boolean, default=False)

# Инициализация базы данных
async def init_db():
    async with engine.begin() as conn:
        # Создаем таблицы в базе данных
        await conn.run_sync(Base.metadata.create_all)

# Асинхронная функция для добавления нового пользователя
async def add_user(user_id: int):
    async with async_session_maker() as session:
        async with session.begin():
            existing_user = await session.execute(
                select(User).where(User.user_id == user_id)
            )
            if not existing_user.scalar_one_or_none():
                new_user = User(user_id=user_id)
                session.add(new_user)

# Асинхронная функция для получения статуса всех категорий пользователя
async def get_user_categories(user_id: int):
    async with async_session_maker() as session:
        result = await session.execute(
            select(User).where(User.user_id == user_id)
        )
        user = result.scalar_one_or_none()
        if user:
            return {
                "crypto": user.crypto,
                "politics": user.politics,
                "economics": user.economics,
                "medias": user.medias,
                "digital": user.digital,
                "military_conflicts": user.military_conflicts,
                "other": user.other,
            }
        return {}

# Асинхронная функция для переключения состояния категории
async def toggle_category(user_id: int, category: str):
    async with async_session_maker() as session:
        async with session.begin():
            result = await session.execute(
                select(User).where(User.user_id == user_id)
            )
            user = result.scalar_one_or_none()
            if user and hasattr(user, category):
                current_value = getattr(user, category)
                setattr(user, category, not current_value)
                session.add(user)
            else:
                print(f"Пользователь или категория '{category}' не найдены")

# Асинхронная функция для получения всех идентификаторов пользователей
async def get_all_user_ids():
    async with async_session_maker() as session:
        result = await session.execute(select(User.user_id))
        return [row[0] for row in result.all()]

# Асинхронная функция для получения пользователей по категории
async def get_users_by_categories(category: str):
    valid_categories = {"crypto", "politics", "economics", "other", "medias", "digital", "military_conflicts"}
    if category not in valid_categories:
        raise ValueError("Указанная категория не поддерживается.")

    async with async_session_maker() as session:
        result = await session.execute(
            select(User.user_id).where(getattr(User, category) == True)
        )
        
        return [row[0] for row in result.all()]
