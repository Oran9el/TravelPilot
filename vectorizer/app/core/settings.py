from os import environ
from dotenv import load_dotenv


load_dotenv()

class Config:
    OPENAI_API_KEY: str = environ.get("OPENAI_API_KEY", "")
    OPENAI_BASE_URL: str = environ.get(
        "OPENAI_BASE_URL", "https://dashscope.aliyuncs.com/compatible-mode/v1"
    )
    OPENAI_CHAT_MODEL: str = environ.get("OPENAI_CHAT_MODEL", "qwen-plus")
    OPENAI_EMBEDDING_MODEL: str = environ.get(
        "OPENAI_EMBEDDING_MODEL", "text-embedding-v2"
    )
    EMBEDDING_DIMENSION: int = int(environ.get("EMBEDDING_DIMENSION", "1536"))
    SQLITE_DB_PATH: str = environ.get("SQLITE_DB_PATH", "./customer_support_chat/data/travel2.sqlite")
    QDRANT_URL: str = environ.get("QDRANT_URL", "http://localhost:6333")

def get_settings():
    return Config()
