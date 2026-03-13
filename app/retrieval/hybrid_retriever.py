import os
import pickle
import faiss
import numpy as np

from app.retrieval.sql_retriever import SQLRetriever
from app.processing.embeddings import EmbeddingModel
from app.config import settings
from app.logger import get_logger


logger = get_logger(__name__)

VECTOR_PATH = settings.VECTOR_DB_PATH


class HybridRetriever:

    def __init__(self):

        logger.info("Loading hybrid retriever")

        self.sql_retriever = SQLRetriever()
        self.embedder = EmbeddingModel()

        index_path = os.path.join(VECTOR_PATH, "index.faiss")
        metadata_path = os.path.join(VECTOR_PATH, "metadata.pkl")

        self.index = faiss.read_index(index_path)

        with open(metadata_path, "rb") as f:
            self.metadata = pickle.load(f)

    def retrieve(self, mrd_number, query, top_k=settings.TOP_K_RESULTS):

        logger.info(f"Running retrieval for MRD: {mrd_number}")

        # Validate MRD exists
        if not self.sql_retriever.validate_mrd(mrd_number):
            raise ValueError("Invalid MRD number")

        query_embedding = self.embedder.encode([query])[0]

        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"),
            100
        )

        results = []

        for idx in indices[0]:

            if idx == -1:
                continue

            meta = self.metadata[idx]

            if str(meta["mrd_number"]) == str(mrd_number):
                results.append(meta)

            if len(results) >= top_k:
                break

        logger.info(f"Retrieved {len(results)} chunks")

        return results