import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
from tqdm import tqdm

from app.processing.html_parser import clean_html
from app.processing.chunking import chunk_text
from app.processing.embeddings import EmbeddingModel
from app.retrieval.vector_store import VectorStore
from app.database.models import create_tables, insert_document
from app.config import settings


DATA_PATH = "data/raw_json"
VECTOR_PATH = settings.VECTOR_DB_PATH

def load_json_files():
    """
    Load all JSON files from data folder
    """

    records = []

    for file in os.listdir(DATA_PATH):

        if file.endswith(".json"):

            file_path = os.path.join(DATA_PATH, file)

            with open(file_path, "r", encoding="utf-8") as f:

                data = json.load(f)

                records.extend(data)

    return records


def main():

    print("Loading JSON records...")

    records = load_json_files()

    print(f"Total records found: {len(records)}")

    # Create SQL tables
    create_tables()

    embedder = EmbeddingModel()

    texts = []
    metadata = []

    print("Processing records...")

    for record in tqdm(records):

        # Insert structured metadata into SQL
        insert_document(record)

        description = record.get("description", "")

        if not description:
            continue

        # Clean HTML
        cleaned_text = clean_html(description)

        # Chunk text
        chunks = chunk_text(cleaned_text)

        for chunk in chunks:

            texts.append(chunk)

            metadata.append({
                "mrd_number": record.get("mrd_number"),
                "visit_id": record.get("visit_id"),
                "document_type": record.get("document_type"),
                "doctor_name": record.get("doctor_name"),
                "text": chunk
            })

    print("Creating embeddings...")

    embeddings = embedder.encode(texts)

    dim = embeddings.shape[1]

    store = VectorStore(dim)

    store.add(embeddings, metadata)

    os.makedirs(VECTOR_PATH, exist_ok=True)

    store.save(VECTOR_PATH)

    print("Vector index created successfully!")


if __name__ == "__main__":
    main()