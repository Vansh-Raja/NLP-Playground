import streamlit as st
from Chunking import chunking as chink

st.set_page_config(page_title="NLP Project", page_icon=":book:", layout="wide")

example_text_Chunking = ""

with st.expander("Learn about Chunking:"):
    st.write("")
    
st.header("Test it out:")