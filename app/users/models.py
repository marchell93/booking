from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

# Старое представление модели
# class Users(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     email = Column(String, nullable=False)
#     hashed_password = Column(String, nullable=False)

class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]
