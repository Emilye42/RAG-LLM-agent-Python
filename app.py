import streamlit as st
from backend import process_query

st.set_page_config(page_title="AI Query Demo", page_icon="🤖", layout="centered")

st.title("💬 Simple Streamlit Frontend-Backend Skeleton")

# Input box
user_input = st.text_input("Enter your question:")

# When user submits
if st.button("Submit"):
    if user_input.strip():
        with st.spinner("Processing..."):
            response = process_query(user_input)
        st.success("Response received!")
        st.markdown(f"**Answer:** {response}")
    else:
        st.warning("Please enter a question before submitting.")


