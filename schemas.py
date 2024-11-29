from pydantic import BaseModel, Field

class StudentSchema(BaseModel):
    id: int
    name: str
    score: float

    class Config:
        orm_mode = True



class ScoreUpdateSchema(BaseModel):
    score: float = Field(..., gt=0, le=100)

    


