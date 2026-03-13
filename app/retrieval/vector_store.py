import faiss
import numpy as np
import pickle


class VectorStore:

    def __init__(self, dim):
        self.index = faiss.IndexFlatL2(dim)
        self.metadata = []

    def add(self, embeddings, metadata):

        self.index.add(np.array(embeddings).astype("float32"))
        self.metadata.extend(metadata)

    def search(self, query_embedding, top_k=5):

        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"),
            top_k
        )

        results = []

        for i, idx in enumerate(indices[0]):
            results.append({
                "score": float(distances[0][i]),
                "metadata": self.metadata[idx]
            })

        return results

    def save(self, path):

        faiss.write_index(self.index, f"{path}/index.faiss")

        with open(f"{path}/metadata.pkl", "wb") as f:
            pickle.dump(self.metadata, f)