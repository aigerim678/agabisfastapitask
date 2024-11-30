from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.models import Student, Base
from app.schemas import ScoreUpdateSchema, StudentSchema
from app.database import engine, get_db
from app.crud import get_student_by_id, get_all_students


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/student/{student_id}", response_model=StudentSchema)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    student = get_student_by_id(db, Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


@app.post("/student/{student_id}/update_score", response_model=StudentSchema)
async def update_student_score(student_id: int, score_update: ScoreUpdateSchema, db: Session = Depends(get_db)):
    student = get_student_by_id(db, Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    student.score = score_update.score
    db.commit()
    return student


@app.get("/students", response_model=List[StudentSchema])
async def get_students(db: Session = Depends(get_db)):
    students = get_all_students(db, Student)
    if not students:
        raise HTTPException(status_code=404, detail="Students not found")
    return students
    
