from pydantic import BaseModel
from pydantic_settings import BaseSettings

class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000

class StudentPrefix(BaseModel):
    prefix: str = "/student"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: StudentPrefix = StudentPrefix()



settings = Settings()