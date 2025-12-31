from sqlalchemy.orm import Session
from app.db.session import engine, SessionLocal
from app.db.base import Base
from app.core.config import settings
from app.core.security import get_password_hash
from app.models.user import User

def init_db():
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.username == "admin").first()
        if not user:
            print("Creando usuario administrador inicial...")
            user_in = User(
                username="admin",
                hashed_password=get_password_hash("secret"),
                is_active=True,
            )
            db.add(user_in)
            db.commit()
            print("Usuario 'admin' creado exitosamente.")
        else:
            print("El usuario 'admin' ya existe.")
    finally:
        db.close()
