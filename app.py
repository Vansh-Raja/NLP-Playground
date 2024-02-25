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
tab_Tokenisation, tab_Stemming, tab_Lemmatization, tab_POS_Tagging, tab_NamedEntityRecognition, tab_Chunking =  st.tabs(["Tokenisation", "Stemming", "Lemmatization", "POS Tagging", "Named Entity Recognition", "Chunking"])

example_text = "Steve, the quick brown fox, jumps over the lazy dog, Alan. It happened yesterday in the park."

# Code for Tab - Tokenisation
with tab_Tokenisation:
    
    with st.expander("Learn about Tokenisation: "):
        st.write("")
        
    st.header("Test it out:")
    
    #Choose a method
    tokenisation_option = st.selectbox(label="Choose a method for Tokenisation", 
                                       options=("Word based","Sentence Based"),
                                       placeholder="Tokenisation method",
                                       index=None,
                                       key="token_methodSel")
    
    # Area to take text input
    text_inp = st.text_input(label="Enter Text for Tokenisation",
                             placeholder=example_text,
                             key="token_inp")
    
    # Area to take user file upload
    text_upload = st.file_uploader("Upload File", type=["txt"], key="token_uploader")
    
    tokenisation_output = None
    
    # If there is text input or file upload
    if text_inp or text_upload is not None:
        
        # If there is text input, use that, else use the uploaded file
        if text_inp:
            content = text_inp
        else:
            content = text_upload.read().decode("utf-8")
            
        # If the user selects word based tokenisation
        if tokenisation_option == "Word based":
            tokenisation_output = (tkn.word_tokenisation(content))
            
        # If the user selects sentence based tokenisation
        elif tokenisation_option == "Sentence Based":
            tokenisation_output = (tkn.sentence_tokenisation(content))
    
    if tokenisation_output:
        st.write(tokenisation_output)
    else:
        st.info("Select a method and input text or upload files to see the output.")    
        

with tab_Stemming:
    pass

with tab_Lemmatization:
    pass

with tab_POS_Tagging:
    pass

# Code for Tab - Named Entity Recognition
with tab_NamedEntityRecognition:
    
    #Explanation for Named Entity Recognition
    with st.expander("Learn about Named Entity Recognition:"):
        st.write("")
        
    st.header("Test it out:")

    # Area to take text input 
    text_inp = st.text_input(label="Enter Text for Named Entity Recognition",
                             value=example_text,
                             key="ner_inp")
    st.write(ner.spacy_ner(text_inp))

    # Area to take user file upload
    text_upload = st.file_uploader("Upload File", type=["txt"], key="ner_uploader")

    if text_upload is not None:
        file_contents = text_upload.read().decode("utf-8")
        st.write(ner.spacy_ner((file_contents)))
        
with tab_Chunking:
    pass