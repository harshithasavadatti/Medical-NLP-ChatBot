import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/query"

st.title("Medical NLP Chatbot")

st.write("Ask clinical questions about patient records.")

mrd_number = st.text_input("MRD Number", "10109")
query = st.text_input("Clinical Question")

if st.button("Ask"):

    payload = {
        "mrd_number": mrd_number,
        "query": query
    }

    response = requests.post(API_URL, json=payload)

    if response.status_code == 200:

        data = response.json()

        st.subheader("Answer")
        st.write(data["answer"])

        st.subheader("Confidence")
        st.write(data["confidence"])

    else:

        st.error("API request failed")