def get_student_by_id(db, table, student_id):
    student = db.query(table).filter(table.id == student_id).first()
    return student

def get_all_students(db, table):
    students = db.query(table).all()
    return students