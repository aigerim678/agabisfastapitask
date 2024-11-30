from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.student.models import Base, Student
from dotenv import load_dotenv
import os

load_dotenv()

# Получение переменных окружения
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

# Формирование строки подключения
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


students_to_add = [
    Student(name="Maral1", score=100.0),
    Student(name="Maral2", score=100.0),
    Student(name="Maral3", score=100.0),
    Student(name="Maral4", score=100.0),
    Student(name="Maral5", score=100.0)
]

session.add_all(students_to_add)
session.commit()

students = session.query(Student).all()
print("Список студентов:")
for student in students:
    print(student)

session.close()

