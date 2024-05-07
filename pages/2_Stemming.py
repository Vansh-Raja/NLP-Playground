import streamlit as st

import Tokenisation as tkn
from Stemming import stemming as stm

st.set_page_config(page_title="NLP Playground", page_icon=":video_game:", layout="wide")
st.title("Stemming")
example_text_Stemming = "Connects Connecting Connections Connected Connection Connectings Connect"

intro_text = """ 
*Stemming is the process of reducing words to their root or base form, known as the stem.*

Stemmers eliminate word suffixes by running input word tokens against a predefined list of common suffixes. Performing this text-processing technique is often useful for dealing with sparsity and/or standardizing vocabulary. Stemming not only helps with reducing redundancy, as most of the time the word stem and their inflected words have the same meaning. There are several kinds of stemming algorithms, and all of them are included in Python NLTK:

- **Porter Stemmer**
- **Snowball Stemmer**
- **Lancaster Stemmer**
- **Regexp Stemmer**

The Snowball and Porter stemmer algorithms have a more mathematical method of eliminating suffixes than other stemmers.

**Try it out with the following example:**

*Connects Connecting Connections Connected Connection Connectings Connect*
"""
with st.expander("Learn about Stemming: "):
    st.markdown(intro_text)
    
st.markdown("### Try it out:")

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
