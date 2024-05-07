import streamlit as st
from Chunking import chunking as chink

import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

st.set_page_config(page_title="NLP Project", page_icon=":book:", layout="wide")

example_text_Chunking = "The quick brown fox jumps over the lazy dog."

with st.expander("Learn about Chunking:"):
    st.write("")
    
st.header("Test it out:")


# Choose a method
chunk_option = st.selectbox(label="Choose a method for Chunking", 
                            options=("NLTK", "Spacy"),
                            placeholder="Chunking method",
                            index=None,
                            key="chunk_methodSel")

if chunk_option == "Spacy":
    spacy_model = st.selectbox(label="Choose a Spacy model for Chunking", 
                                    options=("en_core_web_sm", "en_core_web_md", "en_core_web_lg", "en_core_web_trf"),
                                    placeholder="Spacy model",
                                    index=None,
                                    key="spacy_modelSel_NER")

# Area to take text input
text_inp = st.text_input(label="Enter a sentence for Chunking",
                            placeholder=example_text_Chunking,
                            key="chunk_inp")

# Area to take user file upload
text_upload = st.file_uploader("Upload File", type=["txt"], key="chunk_uploader")
    
chunk_output = None

# If there is text input or file upload
if text_inp or text_upload is not None:
    
    # If there is text input, use that, else use the uploaded file
    if text_inp:
        content = text_inp
    else:
        content = text_upload.read().decode("utf-8")
    
    # If the user selects NLTK POS Tagger    
    if chunk_option == "NLTK":
        chunk_output = chink.nltkChunking(sentence=content)

    if chunk_option == "Spacy":
        chunk_output = chink.spacyChunking(sentence=content, model=spacy_model)
    
if chunk_output:
    st.write(chunk_output)
else:
    st.info("Select a method and input text or upload files to see the output.")