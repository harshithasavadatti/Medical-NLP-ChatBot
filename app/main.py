from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Medical NLP Chatbot",
    description="Hybrid RAG Clinical Query System",
    version="1.0"
)

app.include_router(router)