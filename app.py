import streamlit as st

# Importing the custom packages
from Tokenisation import tokenisation as tkn
from Stemming import stemming as stm
from Lemmatization import lemmatization as lmt
from POS_Tagging import pos_tagging as pos
from NamedEntityRecognition import namedentityrecognition as ner
from Chunking import chunking as chink

st.set_page_config(page_title="NLP Project", page_icon=":book:", layout="wide")

st.title("NLP Project")

# Adding the multiple tabs for all the different processings
tab_Tokenisation, tab_Stemming, tab_Lemmatizationst, tab_POS_Tagging, tab_NamedEntityRecognition, tab_Chunking =  st.tabs(["Tokenisation", "Stemming", "Lemmatization", "POS Tagging", "Named Entity Recognition", "Chunking"])

# Code for Tab - Named Entity Recognition
with tab_NamedEntityRecognition:
    
    #Explanation for Named Entity Recognition
    with st.expander("Learn about Named Entity Recognition:"):
        st.write("")
        
    st.header("Test it out:")
    ner_inp,ner_upload = st.columns([1,1])

    # Column to take text input 
    with ner_inp:
        text_inp = st.text_input("Enter Text for Named Entity Recognition","Apple Stocks are at a all time high in January",key="ner")
        st.write(ner.spacy_ner(text_inp))

    # Column to take user file upload
    with ner_upload:
        text_upload = st.file_uploader("Upload File", type=["txt"])

        if text_upload is not None:
            file_contents = text_upload.read().decode("utf-8")
            st.write(ner.spacy_ner((file_contents)))