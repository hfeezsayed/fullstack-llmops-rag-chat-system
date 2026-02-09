from dataclasses import dataclass #Dataclass creates structured configuration object.
import os
from dotenv import load_dotenv

load_dotenv() #Loads environment variables from .env
# #so this allows Switch LLM providers and Store secrets safely


@dataclass
class Settings: #Stores ALL configuration in one place.
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 50
    VECTOR_DB_PATH: str = "vectorstore/faiss_index"
    EMBEDDING_MODEL: str = os.getenv( #Reads environment variable.
        "EMBEDDING_MODEL",
        "sentence-transformers/all-MiniLM-L6-v2"
    )
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "local")


settings = Settings() #Creates global config object used across project.
