# from pydantic import BaseSettings
from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    mongodb_url: str = os.environ.get('MONGODB_URL')
    database_name: str = os.environ.get('DATABASE_NAME')
    
    class Config:
        env_file = ".env"

settings = Settings()
