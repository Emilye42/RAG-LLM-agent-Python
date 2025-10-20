import streamlit as st
from backend import handle_user_query

st.set_page_config(page_title="FP&A Agent Demo", page_icon="💼")

st.title("💬 FP&A Mini Agent")
st.write("Ask questions like 'What was June 2025 revenue vs budget?' or 'Show gross margin trend'")

query = st.text_input("Your question:")
if st.button("Submit"):
    if query.strip():
        with st.spinner("Thinking..."):
            answer = handle_user_query(query)
        st.write("**Answer:**")
        st.text(answer)
    else:
        st.warning("Please type a question first.")
