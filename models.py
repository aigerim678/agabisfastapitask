from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    score = Column(Float)

    def __repr__(self):
        return f"<Student(id={self.id}, (name={self.name}, score={self.score})>"