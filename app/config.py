class Settings:

    # Database
    SQL_DB_PATH = "medical_records.db"

    # Vector store
    VECTOR_DB_PATH = "vector_store"

    # Embedding model
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    # Ollama
    OLLAMA_URL = "http://localhost:11434/api/chat"
    OLLAMA_MODEL = "llama3"

    # Retrieval
    TOP_K_RESULTS = 5

    # Chunking
    CHUNK_SIZE = 500
    CHUNK_OVERLAP = 100


settings = Settings()