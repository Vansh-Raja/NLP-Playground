import streamlit as st

# Importing the custom packages
from Tokenisation import tokenisation as tkn
from Stemming import stemming as stm
from Lemmatization import lemmatization as lmt
from POS_Tagging import pos_tagging as pos
from NamedEntityRecognition import namedentityrecognition as ner

st.set_page_config(page_title="NLP Project", page_icon=":book:", layout="wide")

st.title("NLP Project")

# text = st.text_input("Enter Text for Named Entity Recognition", key="ner")
# st.write(ner.spacy_ner(text))

with st.form(key='ner'):
    text = st.text_input("Enter Text for Named Entity Recognition", key="ner")
    submit_button = st.form_submit_button(label='Submit')
    if submit_button:
        st.write(ner.spacy_ner(text))