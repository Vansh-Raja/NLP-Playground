import streamlit as st
from Tokenisation import tokenisation as tkn

example_text_Token = "Steve, the quick brown fox, jumps over the lazy dog, Alan. It happened yesterday in the park."

st.set_page_config(page_title="NLP Project", page_icon=":book:", layout="wide")

# Code for Tab - Tokenisation
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
                            placeholder=example_text_Token,
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