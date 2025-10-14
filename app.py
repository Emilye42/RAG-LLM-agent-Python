import streamlit as st
from backend.query_handler import process_query

st.title("💼  Copilot")

user_query = st.text_input("Ask a question:")
if st.button("Submit"):
    with st.spinner("Thinking..."):
        result = process_query(user_query)
    st.success(result)
