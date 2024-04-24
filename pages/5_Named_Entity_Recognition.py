import streamlit as st
from NamedEntityRecognition import namedentityrecognition as ner

st.set_page_config(page_title="NLP Project", page_icon=":book:", layout="wide")

example_text_NER = "Steve, the quick brown fox, jumps over the lazy dog, Alan. It happened yesterday in the park."

#Explanation for Named Entity Recognition
with st.expander("Learn about Named Entity Recognition:"):
    st.write("")
    
st.header("Test it out:")

# Choose a method
ner_option = st.selectbox(label="Choose a method for Named Entity Recognition", 
                            options=("Spacy", "Stanza"),
                            placeholder="Named Entity Recognition method",
                            index=None,
                            key="ner_methodSel")

if ner_option == "Spacy":
    spacy_model = st.selectbox(label="Choose a Spacy model for Named Entity Recognition", 
                                    options=("en_core_web_sm", "en_core_web_md", "en_core_web_lg", "en_core_web_trf"),
                                    placeholder="Spacy model",
                                    index=None,
                                    key="spacy_modelSel_NER")

# Area to take text input
text_inp = st.text_input(label="Enter Words in form of sentence for POS Tagging",
                            placeholder=example_text_NER,
                            key="ner_inp")

# Area to take user file upload
text_upload = st.file_uploader("Upload File", type=["txt"], key="ner_uploader")
    
ner_output = None

# If there is text input or file upload
if text_inp or text_upload is not None:
    
    # If there is text input, use that, else use the uploaded file
    if text_inp:
        content = text_inp
    else:
        content = text_upload.read().decode("utf-8")
    
    # If the user selects NLTK POS Tagger    
    if ner_option == "Spacy":
        ner_output = (ner.spacy_ner(sentence=content,model=spacy_model))
        
    if ner_option == "Stanza":
        ner_output = (ner.stanza_ner(sentence=content))
    
if ner_output:
    st.write(ner_output)
else:
    st.info("Select a method and input text or upload files to see the output.")