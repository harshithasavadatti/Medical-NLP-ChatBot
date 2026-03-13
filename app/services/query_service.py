from app.retrieval.hybrid_retriever import HybridRetriever
from app.services.llm_service import LLMService
from app.logger import get_logger


logger = get_logger(__name__)


class QueryService:

    def __init__(self):

        self.retriever = HybridRetriever()
        self.llm = LLMService()

    def query(self, mrd_number, question):

        logger.info(f"Query received: {question}")

        chunks = self.retriever.retrieve(
            mrd_number=mrd_number,
            query=question
        )

        if not chunks:

            logger.warning("No relevant chunks found")

            return {
                "answer": "No relevant information found in patient records.",
                "confidence": "Low"
            }

        answer = self.llm.generate_answer(
            context_chunks=chunks,
            question=question
        )

        confidence = "High" if len(chunks) >= 3 else "Medium"

        logger.info("Answer generated successfully")

        return {
            "answer": answer,
            "confidence": confidence
        }