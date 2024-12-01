from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from .base import Base

class Student(Base):
    name: Mapped[str] = mapped_column(String)
    score: Mapped[str] = mapped_column(String)

