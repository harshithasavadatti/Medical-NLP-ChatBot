# Medical NLP Chatbot (Hybrid RAG Clinical Query System)

A Retrieval-Augmented Generation (RAG) based clinical question answering
system that allows users to query patient medical records using natural
language.

The system retrieves relevant clinical information using hybrid
retrieval (SQL + semantic vector search) and generates grounded answers
using a local LLM.

------------------------------------------------------------------------

## System Architecture

Medical JSON Records │ ▼ HTML Cleaning │ ▼ Text Chunking │ ▼ Embeddings
(MiniLM) │ ▼ FAISS Vector Store │ ▼ Hybrid Retrieval (SQL + Vector
Search) │ ▼ Context Builder │ ▼ LLM (Llama3 via Ollama) │ ▼ FastAPI
Backend │ ▼ Streamlit Frontend

------------------------------------------------------------------------

## Features

-   Query patient records using natural language
-   Hybrid retrieval using SQL filtering and vector similarity
-   FAISS vector database for semantic search
-   Local LLM inference using Ollama (Llama3)
-   REST API using FastAPI
-   Interactive UI using Streamlit
-   Fully local system (no external APIs required)

------------------------------------------------------------------------

## Tech Stack

Backend - Python - FastAPI

Vector Search - FAISS - Sentence Transformers (MiniLM)

LLM - Llama3 via Ollama

Frontend - Streamlit

Database - SQLite

------------------------------------------------------------------------

## Project Structure

medical-nlp-chatbot │
├── app │ ├── api │ 
├── services │
├── retrieval │
├── processing │
├── prompts │ 
├── utils │ 
├── config.py │ 
├── data │
├── raw_json 
│ └── processed_chunks 
├──scripts │ 
├── ingest_data.py
│ └── create_index.py 
│ ├── vector_store 
├── index.faiss
│ └── metadata.pkl 
├── medical_records.db
├── dashboard.py
├── requirements.txt
└── README.md

------------------------------------------------------------------------

## Installation

Clone the repository

git clone cd Medical NLP ChatBot

Create virtual environment

python -m venv venv

Activate environment (Windows)

venv`\Scripts`{=tex}`\activate`{=tex}

Install dependencies

pip install -r requirements.txt

------------------------------------------------------------------------

## Install Ollama

Download and install Ollama: https://ollama.com

Pull the model:

ollama pull llama3

Verify installation:

ollama run llama3

------------------------------------------------------------------------

## Data Ingestion

Process raw medical JSON files:

python -m scripts.ingest_data

Create vector index:

python -m scripts.create_index

------------------------------------------------------------------------

## Run Backend API

uvicorn app.main:app --reload

API docs:

http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Run Frontend

streamlit run streamlit_app.py

Open:

http://localhost:8501


------------------------------------------------------------------------

## Example Query

MRD Number: 10109\
Question: What medications was the patient discharged with?

Example Output

Medications: - INJ EMESET 4MG - INJ NEOMOL 1GM - INJ DEXA 8MG - INJ
TRAMADOL 50MG - INJ METRO 100ML - INJ CIPLOX 100ML

------------------------------------------------------------------------

## Key Components

Hybrid Retrieval - SQL validation for MRD numbers - FAISS semantic
search for relevant chunks

Embeddings sentence-transformers/all-MiniLM-L6-v2

LLM Inference Llama3 via Ollama

------------------------------------------------------------------------

## Future Improvements

-   Add reranking for improved retrieval accuracy
-   Add authentication for patient data security
-   Dockerize the application
-   Add audit logs for compliance

------------------------------------------------------------------------

## License

This project is intended for educational and research purposes.
