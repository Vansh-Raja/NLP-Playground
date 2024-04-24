import streamlit as st

import Tokenisation as tkn
from Stemming import stemming as stm

st.set_page_config(page_title="NLP Project", page_icon=":book:", layout="wide")

example_text_Stemming = "Connects Connecting Connections Connected Connection Connectings Connect"

#TODO - Add option to display output while comparing all Stemmers

with st.expander("Learn about Stemming: "):
    st.write("")
    
st.header("Test it out:")

#Choose a method
stemming_option = st.selectbox(label="Choose a method for Stemming", 
                                    options=("Porter Stemmer",
                                            "Snowball Stemmer",
                                            "Lancaster Stemmer",
                                            "Regexp Stemmer"),
                                    placeholder="Stemming method",
                                    index=None,
                                    key="stem_methodSel")

if stemming_option == "Regexp Stemmer":
    regex = st.text_input(label="Enter the Regex for Regexp Stemmer",
                            value="ing$|s$|e$|able$",
                            key="regex_inp")
    
    minWordLength = st.number_input(label="Enter the minimum word length for Regexp Stemmer",
                                    min_value=1,
                                    max_value=100,
                                    value=4,
                                    step=1,
                                    key="minWordLength_inp")

# Area to take text input
text_inp = st.text_input(label="Enter Words in form of sentence for Stemming",
                            placeholder=example_text_Stemming,
                            key="stem_inp")

# Area to take user file upload
text_upload = st.file_uploader("Upload File", type=["txt"], key="stem_uploader")

stemming_output = None

# If there is text input or file upload
if text_inp or text_upload is not None:
    
    # If there is text input, use that, else use the uploaded file
    if text_inp:
        content = text_inp
    else:
        content = text_upload.read().decode("utf-8")
        
    content = tkn.word_tokenisation(content)
        
    # If the user selects Porter Stemmer
    if stemming_option == "Porter Stemmer":
        stemming_output = (stm.Porter_Stemmer(content))
        
    # If the user selects Snowball Stemmer
    elif stemming_option == "Snowball Stemmer":
        stemming_output = (stm.SnowBall_Stemmer(content))
    
    # If the user selects Lancaster Stemmer
    elif stemming_option == "Lancaster Stemmer":
        stemming_output = (stm.Lancaster_Stemmer(content))
        
    # If the user selects Regexp Stemmer
    elif stemming_option == "Regexp Stemmer":
        stemming_output = (stm.Regexp_Stemmer(content, regex, minWordLength))
    
if stemming_output:
    st.write(stemming_output)
else:
    st.info("Select a method and input text or upload files to see the output.")    
