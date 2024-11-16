from sqlalchemy import create_engine, Column, Integer, Boolean, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение к базе данных SQLite
DATABASE_URL = "sqlite:///users.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Модель User, представляющая таблицу users
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True, nullable=False)
    crypto = Column(Boolean, default=False)
    politics = Column(Boolean, default=False)
    economics = Column(Boolean, default=False)
    other = Column(Boolean, default=False)
    medias = Column(Boolean, default=False)
    digital = Column(Boolean, default=False)
    military_conflicts = Column(Boolean, default=False)

# Создание таблиц в базе данных
def init_db():
    Base.metadata.create_all(bind=engine)

# Функция для добавления нового пользователя
def add_user(user_id: int):
    session = SessionLocal()
    try:
        if not session.query(User).filter(User.user_id == user_id).first():
            new_user = User(user_id=user_id)
            session.add(new_user)
            session.commit()
    finally:
        session.close()

# Функция для получения статуса всех категорий пользователя
def get_user_categories(user_id: int):
    session = SessionLocal()
    categories = {}
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if user:
            categories ={
                "crypto": user.crypto,
                "politics": user.politics,
                "economics": user.economics,
                "medias": user.medias,
                "digital": user.digital,
                "military_conflicts": user.military_conflicts,
                "other": user.other,
            }
            return categories
    finally:
        session.close()
    

# Функция для переключения состояния категории
def toggle_category(user_id: int, category: str):
    session = SessionLocal()
    try:
        user = session.query(User).filter(User.user_id == user_id).first()
        if user and hasattr(user, category):
            current_value = getattr(user, category)
            setattr(user, category, not current_value)
            session.commit()
        else:
            print(f"Пользователь или категория '{category}' не найдены")
    finally:
        session.close()

def get_all_user_ids(): 
    session = SessionLocal() 
    try: 
        user_ids = session.query(User.user_id).all() 
        return [user_id[0] for user_id in user_ids] 
    finally:
        session.close()





def get_users_by_categories(category):
    session = SessionLocal()
    # Проверяем, что категории валидны
    valid_categories = {"crypto", "politics", "economics", "other", "medias", "digital", "military_conflicts"}
    if category not in valid_categories:
        raise ValueError("Указанная категория не поддерживается.")

    try:
        users = session.query(User.user_id  ).filter(getattr(User, category) == True).distinct().all()
        session.close()
        return [user.user_id for user in users]
    finally:
        session.close()
    

