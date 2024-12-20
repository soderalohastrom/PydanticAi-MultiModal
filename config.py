from pydantic_settings import BaseSettings
from pydantic import ConfigDict
import os

class Settings(BaseSettings):
    LLM_MODEL: str = "gpt-4o-mini"
    OPENAI_API_KEY: str
    
    model_config = ConfigDict(
        env_file=".env",
        extra="allow",
        arbitrary_types_allowed=True,
    )
    
settings = Settings()