from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional

from models import Student, Base
from schemas import StudentSchema
from database import engine, get_db


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/student/{student_id}", response_model=StudentSchema)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
    

