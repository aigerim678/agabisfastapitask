from pydantic import BaseModel

class StudentSchema(BaseModel):
    id: int
    name: str
    score: float

    class Config:
        orm_mode = True
