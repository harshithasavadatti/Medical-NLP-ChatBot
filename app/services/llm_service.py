import requests

from app.config import settings
from app.prompts.clinical_prompt import CLINICAL_PROMPT
from app.logger import get_logger


logger = get_logger(__name__)


class LLMService:

    def __init__(self, model=settings.OLLAMA_MODEL):
        self.model = model
        self.url = settings.OLLAMA_URL

    def generate_answer(self, context_chunks, question):

        context = "\n\n".join([chunk["text"] for chunk in context_chunks])

        prompt = CLINICAL_PROMPT.format(
            context=context,
            question=question
        )

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": False
        }

        try:

            logger.info(f"Using model: {self.model}")

            response = requests.post(
                self.url,
                json=payload,
                timeout=120
            )

            data = response.json()

            return data["message"]["content"].strip()

        except Exception as e:

            logger.error(f"Ollama error: {str(e)}")

            return "LLM service failed"